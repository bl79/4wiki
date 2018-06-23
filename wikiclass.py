# -*- coding: utf-8 -*-
import re
import sqlite3
from collections import namedtuple
import pywikibot
import mwparserfromhell as mwp
import requests
from urllib.parse import urlparse, parse_qs, parse_qsl, unquote, quote
from lxml.html import fromstring
# import vladi_commons.vladi_commons
# from vladi_commons import vladi_commons
from vladi_commons.vladi_helpers import csv_read_dict, csv_save_dict, json_store_to_file, json_data_from_file, \
    file_readtext, listdic_pop, file_readlines, lines2list, file_savelines
import vladi_commons.lib_for_mwparserfromhell


class WikiMethods():
    # LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки
    EDITION = 3
    wiki_lang = 'ru'
    wiki_project = 'wikisource'
    SITE = pywikibot.Site(wiki_lang, wiki_project)
    FI = '/home/vladislav/var/tsd%s_worlists.txt' % EDITION
    FO = FI + '_pages_to_rename'
    # FI_pagelist = '/home/vladislav/var/tsd%s_doubles_tagpages.txt' % EDITION
    # FO_pagelist = FI_pagelist + '_pages_to_rename'
    FI_listpages = '/home/vladislav/var/tsd%s_listpages.txt' % EDITION
    FI_wordlists_list = '/home/vladislav/var/tsd%s_worlists.txt' % EDITION
    FO_wl_list = FI_wordlists_list + '_pages_to_rename'
    FI_wl_text = '/home/vladislav/var/tsd%s_worlists.txt' % EDITION
    FO_wl_text = FI_wl_text + '_pages_to_rename'
    PATH_DB = '/home/vladislav/var/tsd.sqlite'
    TEXTOVKA_FROM_FILE = 0  # or from wikipage
    LIST_OF_WORDLISTS_FROM_FILE = 1  # or from wikipage
    PAGELIST_TITLES = []
    REWRITE_EXIST_PAGES = None
    CLEAN_TEXT_FROM_POSTED = None  # Не ясен смысл и алгоритм очистки текстовки от залитых
    MAKE_REDIRECTS = None
    PAGENAME_PREFIX = ''
    PAGENAME_POSTFIX = ''
    SUMMARY = 'заливка'
    wordlists_text = []
    lat_redirects = []
    list2rename = []
    WORDLIST_TITLES = []
    wordlist_title = ''
    wordlist_text = ''
    wordlists = []
    page = ''  # pywikibot object
    page_wikicode = ''  # mwp object
    pagename = ''
    cur_article_name = ''
    pagelists_titles = ''
    pagelist = ''
    stock_redirects = False
    redirects = []
    log = set()  # already_exists_pages
    re_pagename_from_wikilink = re.compile(r'\[\[%s/(.*?)\s*(?:\||\]\])' % PAGENAME_PREFIX)

    def __init__(self, *args, use_db=False):
        # self.PAGELIST_TITLES = str2list(args[0])
        self.con = sqlite3.connect(self.PATH_DB) if use_db else False

    # self.get_pagelists()
    # self.parse_wordlist()
    # self.operate_wordlist_pagelinks()

    def get_pagelists(self, from_file=True, path=''):
        """PAGELIST_FROM_FILE = True or from wikipage"""
        if from_file:
            self.pagelists_titles = file_readlines(path)
        else:
            for WORDLIST_TITLE in lines2list(self.PAGELIST_TITLES):
                self.pagelist = pywikibot.Page(self.SITE, WORDLIST_TITLE)
                self.pagelists_titles.append(self.pagelist.get())

    def get_lists_of_wordlists(self):
        if self.LIST_OF_WORDLISTS_FROM_FILE == 1:
            self.wordlists_titles = file_readlines(self.FI_wordlists_list)
        else:
            for WORDLIST_TITLE in lines2list(self.WORDLIST_TITLES):
                self.wordlist_page_obj = pywikibot.Page(self.SITE, WORDLIST_TITLE)
                self.wordlists_titles.append(self.wordlist_page_obj.get())

    def get_text_of_wordlist(self):
        if self.TEXTOVKA_FROM_FILE == 1:
            self.wordlist_text = file_readlines(self.FI)
        else:
            self.wordlist = pywikibot.Page(self.SITE, self.wordlist_title)
            self.wordlist_text = self.wordlist.text

    def get_wordlists(self, use_pywikibot=True, use_mwparser=True, get_html=False):
        self.get_lists_of_wordlists()
        # self.parse_wordlist()
        # self.operate_wordlist_pagelinks()
        if get_html:
            self.open_reqsession()
        self.wordlists = []
        for wordlist_title in self.wordlists_titles:
            # for TEXTOVKA_TITLE in lines2list(self.WORDLIST_TITLES):
            # if self.TEXTOVKA_FROM_FILE == 1:
            # 	self.get_text_of_wordlists()
            # self.get_text_of_wordlist()
            w = {
                'title': wordlist_title,
                'obj': None,
                'text': None,
                'wikicode': None,
                'html': None,
                'html_parsed': None,
            }
            if use_pywikibot:
                w['obj'] = page_obj = pywikibot.Page(self.SITE, wordlist_title)
                w['text'] = text_of_wordlist = page_obj.text if self.TEXTOVKA_FROM_FILE != 1 \
                    else file_readlines(self.FI_wl_text)
                w['wikicode'] = mwp.parse(text_of_wordlist) if use_mwparser else None
            if get_html:
                r = requests.get(self.make_wiki_url(wordlist_title), params={"action": "render"},
                                 headers={'user-agent': 'user:textworkerBot'})
                if r.status_code == 200:
                    w['html'] = r.text
                    w['html_parsed'] = fromstring(r.text)
            self.wordlists.append(w)

    def make_wiki_url(self, title):
        return 'https://' + self.wiki_lang + '.' + self.wiki_project + '.org/wiki/' + quote(title)

    def open_reqsession(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0',
            # 'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
            # 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.79 Chrome/61.0.3163.79 Safari/537.36',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            # 'Accept': 'application/json, text/javascript, */*; q=0.01'
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            # 'Content-Type': 'x-www-form-urlencoded',
            'Content-Type': 'text/plain;charset=UTF-8',
            # 'Host': 'www.site.ru',
            # 'Referer': 'http://www.site.ru/index.html',
        }
        proxyDict = {
            "http": 'http://212.161.91.178:65103',
            "https": 'https://212.161.91.178:65103',
            # "http": 'http://92.27.91.253:53281',
            # "https": 'https://92.27.91.253:53281',
            # "ftp"   : ftp_proxy
        }
        s = requests.Session()
        s.headers = headers
        s.proxies.update(proxyDict)
        return s

    def get_cur_article_name(self, pagename):
        return self.string_strip(pagename.split('/')[1])

    def open_page(self, pagename, switch_to_RedirectTarget=True, mark_RedirectPages_category=False, wmp=True):
        self.page_data = {}
        page_obj = pywikibot.Page(self.SITE, pagename)
        if page_obj.exists():
            if page_obj.isRedirectPage():
                # для редиректов создание файл-списка переименования для pwb
                RedirectTarget = page_obj.getRedirectTarget()
                if self.stock_redirects:
                    self.redirects.append(pagename)
                    self.redirects.append(RedirectTarget)
                if switch_to_RedirectTarget:
                    page_obj = RedirectTarget
                    pagename = RedirectTarget.title()
                if mark_RedirectPages_category:
                    page_obj.text = page_obj.text + '\n[[Категория:%s]]' % mark_RedirectPages_category
            page_data = {
                'pagename': pagename,
                'article_name': self.get_cur_article_name(pagename),
                'obj': page_obj,
            }
            if wmp:
                page_data['wikicode'] = mwp.parse(page_obj.text)
            return page_data
        else:
            return False

    def parse_page(self, page_obj):
        pagename = page_obj.title()
        self.page_data = {
            'pagename': pagename,
            'article_name': self.get_cur_article_name(pagename),
            'obj': page_obj,
            'wikicode': mwp.parse(page_obj.text),
        }

    def get_args_from_tagPages(self):
        """парсинг тэга <pages>"""
        tagsPages = [tag for tag in self.page_data['wikicode'].filter_tags() if tag.tag.matches('pages')]
        if len(tagsPages) > 1:
            print('%s: len(count_tags) > 1' % self.page_data['pagename'])
            return

        elif len(tagsPages) == 1:
            self.page_data.update({
                'tag_pages': tagsPages[0],
                # 'indexpage': str(tagsPages[0].get('index').value.strip()),
                'volume': self.tsd_calc_volume(tagsPages[0].get('index').value, self.EDITION),
                'onlysection': str(tagsPages[0].get('onlysection').value) if tagsPages[0].has('onlysection') else '',
                # 'fromsection': str(tagsPages[0].get('fromsection').value) if tagsPages[0].has('fromsection') else '',
                # 'tosection': str(tagsPages[0].get('tosection').value) if tagsPages[0].has('tosection') else '',
                'numscan_from_in_tag': str(tagsPages[0].get('from').value.strip()),
                'numscan_to_in_tag': str(tagsPages[0].get('to').value.strip()),
            })
            # self.page_data['offset'] = self.calc_pagenum_offset(str(self.page_data['indexpage']))
            # self.page_data['booknum_from'] = int(self.page_data['numscan_from_in_tag']) - self.page_data['offset']
            # self.page_data['booknum_to'] = int(self.page_data['numscan_to_in_tag']) - self.page_data['offset']
            self.page_data['do'] = True if 'ДО' in self.page_data['pagename'].split('/') else False

    def get_pagestags(self, wikicode):
        return [tag for tag in wikicode.filter_tags() if tag.tag.matches('pages')]

    def add_param_SECTION_in_headertpl(self, sectionname_new):
        """добавление параметра СЕКЦИЯ в шаблон-шапку, иначе удаление параметра"""
        for pagetpl in self.page_data['wikicode'].filter_templates():
            if pagetpl.name.matches('ТСД'):
                if sectionname_new != self.cur_article_name:
                    pagetpl.add('СЕКЦИЯ', sectionname_new)
                else:
                    if pagetpl.has('СЕКЦИЯ'):
                        pagetpl.remove('СЕКЦИЯ')

    def tsd_section_name(self, pagename):
        articlename = pagename.split('/')[1]
        sectionname_new = ''
        if 'ДО' in pagename.split('/'):
            sectionname_new = articlename
        else:
            if articlename.endswith((' 1', ' 2', ' 3', ' 4')):
                sectionname_new = articlename + '-1'
            else:
                sectionname_new = articlename + '1'
        return sectionname_new

    def tsd_calc_pagenum_offset(self, indexpage):
        offsets = {
            'Толковый словарь. Том 1 (Даль 1903).djvu': 17,
            'Толковый словарь. Том 2 (Даль 1905).djvu': 2,
            'Толковый словарь. Том 3 (Даль 1907).djvu': 2,
            'Толковый словарь. Том 4 (Даль 1909).djvu': 4,
            'Толковый словарь Даля (2-е издание). Том 1 (1880).pdf': 90,
            'Толковый словарь Даля (2-е издание). Том 2 (1881).pdf': 9,
            'Толковый словарь Даля (2-е издание). Том 3 (1882).pdf': 8,
            'Толковый словарь Даля (2-е издание). Том 4 (1882).pdf': 8,
            'Толковый словарь Даля (1-е издание). Часть 1 (1863).pdf': 2,
            'Толковый словарь Даля (1-е издание). Часть 2 (1865).pdf': -626,
            'Толковый словарь Даля (1-е издание). Часть 3 (1865).pdf': 1,
            'Толковый словарь Даля (1-е издание). Часть 4 (1866).pdf': 3,
        }
        return offsets[indexpage]

    def tsd_calc_volume(self, indexpage, edition):
        v = None
        volumes = [
            {'Толковый словарь Даля (1-е издание). Часть 1 (1863).pdf': 1,
             'Толковый словарь Даля (1-е издание). Часть 2 (1865).pdf': 2,
             'Толковый словарь Даля (1-е издание). Часть 3 (1865).pdf': 3,
             'Толковый словарь Даля (1-е издание). Часть 4 (1866).pdf': 4, },
            {'Толковый словарь Даля (2-е издание). Том 1 (1880).pdf': 1,
             'Толковый словарь Даля (2-е издание). Том 2 (1881).pdf': 2,
             'Толковый словарь Даля (2-е издание). Том 3 (1882).pdf': 3,
             'Толковый словарь Даля (2-е издание). Том 4 (1882).pdf': 4, },
            {'Толковый словарь. Том 1 (Даль 1903).djvu': 1,
             'Толковый словарь. Том 2 (Даль 1905).djvu': 2,
             'Толковый словарь. Том 3 (Даль 1907).djvu': 3,
             'Толковый словарь. Том 4 (Даль 1909).djvu': 4, }
        ]
        try:
            v = volumes[edition - 1][self.string_strip(indexpage)]
        except:
            print('Ошибка при определении тома по названию индексной страницы из тега <pages>: %s' % self.page_data[
                'pagename'])
            pass
        return v

    def string_strip(self, s):
        return str(s).replace('\u200e', '').replace('&lrm;', '').replace('&#8206;', '').strip()

    def update_wordlist_item(self, tpl, wordlist_data, use_pagenum_instead_scannum=True):
        """параметры: tpl - шаблон словника из mwparserfromhell, {{tsds}} и т.п.; p - словарь"""
        # self.page_data['pagination_in_tpl'] = re.findall('\d+', self.cur_wl_tpl.get(3).value.strip())
        if use_pagenum_instead_scannum:
            booknum_from = 'booknum_from'
            booknum_to = 'booknum_to'
            if booknum_from in wordlist_data and booknum_to in wordlist_data:
                b_from = wordlist_data[booknum_from]
                b_to = wordlist_data[booknum_to]
                if b_from is None or b_to is None:
                    print('проблема с пагинацией страницы в БД, is None')
                    return
                pagination_book_new = b_from if b_from == b_to else '%s—%s' % (b_from, b_to)
                if tpl.has(3):
                    tpl.get(3).value = pagination_book_new
                else:
                    tpl.add(3, pagination_book_new)
            else:
                pass
            pass
        else:
            # 4-й параметр, страницы скана
            numscan_from_in_tag = 'numscan_from_in_tag'
            numscan_to_in_tag = 'numscan_to_in_tag'
            if numscan_from_in_tag in wordlist_data and numscan_to_in_tag in wordlist_data:
                s_from = wordlist_data[numscan_from_in_tag]
                s_to = wordlist_data[numscan_to_in_tag]
                if s_from is None or s_to is None:
                    print('проблема с пагинацией скана в БД, is None')
                    return
                params_pagination_scan_new = s_from if s_from == s_to else '%s/%s' % (s_from, s_to)
                if tpl.has(4):
                    tpl.get(4).value = params_pagination_scan_new
                else:
                    tpl.add(4, params_pagination_scan_new)
            else:
                pass

        # сдвиг 'p=' в конец
        if tpl.has('p'):
            v = tpl.get('p').value.strip()
            tpl.remove('p')
            tpl.add('p', v)
        pass

    def db_save_pagedata(self, data, table, path=''):
        d = {
            # 'index': self.page_data.get('index', 'NULL'),
            'pagename': self.page_data.get('pagename'),
            'article_name': self.page_data.get('article_name'),
            'volume': self.page_data.get('volume'),
            # 'indexpage': self.page_data.get('indexpage'),
            'onlysection': self.page_data.get('onlysection'),
            # 'fromsection': self.page_data.get('fromsection'),
            # 'tosection': self.page_data.get('tosection'),
            'numscan_from_in_tag': self.page_data.get('numscan_from_in_tag'),
            'numscan_to_in_tag': self.page_data.get('numscan_to_in_tag'),
            # 'offset': self.page_data.get('offset'),
            'booknum_from': self.page_data.get('booknum_from'),
            'booknum_to': self.page_data.get('booknum_to'),
            'do': self.page_data.get('do'),
            # --'obj': self.page_data.get('obj')
            # --'wikicode': self.page_data.get('wikicode')
            # --'tag_pages': self.page_data.get('tag_pages')
        }
        # con = sqlite3.connect(self.PATH_DB)
        with self.con:
            cur = self.con.cursor()
            # cur.execute("""	""")
            # q = "INSERT INTO %s VALUES(%s);" % (table, ','.join(['?'] * len(d.keys())))
            # k = ','.join(['"%s"' % k for k in list(d.values())])
            # v = ','.join(['"%s"' % k for k in list(d.values())])
            # q = "INSERT INTO %s (%s) VALUES(%s);" % (table, k, v)
            q = "INSERT INTO %s (%s) VALUES(%s);" % (table, d.keys(), d.values())
            # cur.executemany(q, d)
            # cur.execute("INSERT INTO %s VALUES(%s);" % (table, ','.join(['?'] * len(d.keys()))), d)
            cur.execute("INSERT INTO %s VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);" % table,
                        list(d.values()))  # [d]

    def db_get_article_data(self, articlename, tablename):
        self.page_data = {}
        with self.con:
            cursor = self.con.cursor()
            # cursor.execute(
            # 	"UPDATE tsd1 SET do = 1 WHERE pagename LIKE '%/ДО'; UPDATE tsd1 SET do = 0 WHERE pagename NOT LIKE '%/ДО';")
            # cursor.execute("""
            # 	UPDATE tsd1 SET scan_from = NULL WHERE scan_from LIKE '';
            # 	UPDATE tsd1 SET book_from = NULL WHERE book_from LIKE '';
            # 	UPDATE tsd1 SET scan_to = NULL WHERE scan_to LIKE '';
            # 	UPDATE tsd1 SET book_to = NULL WHERE book_to LIKE '';
            # 	UPDATE tsd1 SET volume = NULL WHERE volume LIKE '';	""")
            pn_ = self.PAGENAME_PREFIX + '/' + articlename
            for pn in [pn_, pn_ + '/ДО']:
                cursor.execute("SELECT * FROM %s WHERE pagename = ?" % tablename, (pn,))
                r = cursor.fetchall()
                if len(r):
                    # если нет данных по статье СО попробовать ДО
                    break

            for p in r:
                self.page_data = {
                    'pagename': p[0],
                    'numscan_from_in_tag': p[1],
                    'booknum_from': p[2],
                    'numscan_to_in_tag': p[3],
                    'booknum_to': p[4],
                    'volume': p[5],
                    'do': p[6],
                    'onlysection': p[7],
                    'article_name': p[8],
                }
            pass

    def wiki_posting_page(self, page_obj, text_new, summary, remove_more_newlines=False):
        if remove_more_newlines:
            text_new = re.sub('\n\n+', '\n\n', text_new)
        if page_obj.text != text_new:
            page_obj.text = text_new
            page_obj.save(summary=summary)

    def savelist2rename(self, filename):
        file_savelines(filename, self.list2rename)
        file_savelines('lat_redirects', self.lat_redirects)
