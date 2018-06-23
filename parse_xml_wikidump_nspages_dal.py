# -*- coding: utf-8 -*-
from lxml import etree
from io import StringIO
# !/usr/bin/env python
# coding: utf-8
import requests
from urllib.parse import urlencode, quote
# import vladi_commons
# from vladi_commons import vladi_commons
from vladi_commons.vladi_helpers import csv_read_dict, csv_save_dict, json_store_to_file, json_data_from_file, \
    file_readtext, listdic_pop, csv_save, file_savelines, read_list_interlines
import sqlite3
import json
from lxml.html import fromstring
import lxml.html
import re
# import html5lib
from urllib.parse import urlparse, parse_qs, parse_qsl, unquote, quote
from wikiclass import WikiMethods
from toDO.toDO import ToDO

# Путь к файлу wikidump
# PATHTOXML = '/home/vladislav/var/wikidumps/ruwikisource-20180301-pages-meta-current.xml'
PATHTOXML = '/home/vladislav/var/dal/Викитека-20180409165247.xml'

txt = ''


def parseBookXML(xmlFile):
    # with open(xmlFile) as fobj:
    # 	xml = fobj.read()
    xml = txt
    root = etree.fromstring(xml)
    # root = etree.parse('path_to_file')

    from xml.etree import ElementTree as EET

    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse(StringIO(xml), parser)

    from xml.etree import ElementTree

    # namespaces
    NS_MAIN = 2
    NS_PAGE = 104

    book_dict = {}
    books = []
    for book in root.getchildren():
        for elem in book.getchildren():
            if elem.tag != 'page': continue  # work only on pages
            if int(elem.ns) not in [NS_PAGE]: continue
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + " => " + text)
            book_dict[elem.tag] = text

            if book.tag == "book":
                books.append(book_dict)
                book_dict = {}

    return books


# out = open("/tmp/output.txt", "w", encoding="utf-8")


import re
from pywikibot import output, xmlreader
from urllib.parse import urlparse, parse_qs, parse_qsl, unquote, quote

# namespaces
NS_MAIN = 2
NS_PAGE = 104

wikilink_re1 = re.compile(r"\[\[РСКД/([^]|]+)")
wikilink_re2 = re.compile(r"\[\[../([^]|]+)")
wikilink_re3 = re.compile(r"{[{([wW]l\|([^}|]+)")
redirect_target_re = re.compile(r"#перенаправление \[\[([^]]+)")

all_found_titles = []
titles_and_links = []
redirects = []


class Main(WikiMethods, ToDO):
    entries = []
    articles_with_perenos = []
    articles_with_perenos_all = []
    no_articles = []
    articles_with_akut = []

    def __init__(self):
        super().__init__()
        # self.to_do = ToDO()

    # def reposting_from_classesru(self):
    #     # изменение и постинг статей
    #     for pagename in self.pagelists_titles:
    #         self.process_page(pagename)
    #
    #     # не залитые статьи
    #     json_store_to_file('/home/vladislav/var/dal/tsd2_from_classess_ru-dontreposted.json', self.dic_from_classesru)
    #     # не залитые статьи с переносом
    #     json_store_to_file('/home/vladislav/var/dal/tsd2_from_classess_ru-perenos.json', self.articles_with_perenos)
    #     json_store_to_file('/home/vladislav/var/dal/tsd2_from_classess_ru-perenos_all.json',
    #                        self.articles_with_perenos_all)
    #     # залитые статьи с {{акут}}
    #     json_store_to_file('/home/vladislav/var/dal/tsd2_from_classess_ru-akut.json', self.articles_with_akut)
    #     # статьи не найденые в self.dic_from_classesru
    #     json_store_to_file('/home/vladislav/var/dal/tsd2_from_classess_ru-no_articles.json', self.no_articles)
    #
    #     # self.main()
    #     pass

    def work_xml_wikidump(self, PATHTOXML):
        dump = xmlreader.XmlDump(PATHTOXML)

        # readPagesCount = 0
        for entry in dump.parse():
            if int(entry.ns) not in [NS_PAGE] \
                    or not entry.title.startswith('Страница:Толковый словарь Даля (2-е издание)'):
                # or not entry.title.startswith('РСКД/') \
                # or 'РСКД/Словник' in entry.title \
                # or 'РСКД/Русский указатель статей' == entry.title \
                # or 'РСКД/Список сокращений названий трудов античных авторов' == entry.title:
                continue
            # if entry.isredirect:
            #     redirects.append(dict(t=entry.title, r=redirect_target_re.search(entry.text).group(1)))

            # if 'РСКД/Цезарь' in entry.title:
            #     print(entry.title)

            # all_found_titles.append(entry.title)

            e = dict(page_title=entry.title, page_text=entry.text, )

            self.entries.append(e)

            # links = []
            # links.extend(wikilink_re1.findall(entry.text))
            # links.extend(wikilink_re2.findall(entry.text))
            # links.extend(wikilink_re3.findall(entry.text))
            # links = [f'РСКД/{l}' for l in links]
            # if links:
            #     print({'t': entry.title, 're': links})
            #     titles_and_links.append({'t': entry.title, 're': links})

            # readPagesCount += 1
            # if readPagesCount % 10000 == 0:
            #     output("%i pages read..." % readPagesCount)

            # new_text_page = self.process_page(entry)

        # self.find_sections_on_few_pages()

        pass
        #
        # while (self.dic_from_classesru):
        #     a = self.dic_from_classesru.pop()
        #
        #     for e in self.entries:
        #         page_title, page_text = e['page_title'], e['page_text']
        #         sections_so = re.findall(r'(<section begin="([^"]+)\+" */>(.+?)<section end="\2\+" */>)', page_text)
        #         for s in sections_so:
        #             s_full, s_name, s_text = s
        #             if s_name.lower() == a['title'].lower():
        #                 s_text_new = s_text
        #
        #                 page_text = re.sub(s_full, s_full.replace(s_text, s_text_new), page_text)
        #         if page_text != e['page_text']:
        #             page_obj = self.open_page(page_title)
        #             self.wiki_posting_page(page_obj, page_text, '')
        #
        #         break
        #
        # pass

        #
        # pass
        # # a = [links['re'] for links in titles_and_links]
        # # all_links = {l for ls in a for l in ls}
        # all_links = {l.rsplit('#')[0] for links in titles_and_links for l in links['re']}
        # error_links = {l for l in all_links if l not in all_found_titles}
        # # ltxt = '\n'.join([f'# [[{e}]]' for e in error_links])
        # ltxt = '\n'.join([f'# [[{e}]] - [[Служебная:Ссылки сюда/{quote(e)}|ссылки сюда]]' for e in error_links])
        # pass
        #
        # # ссылки у которых есть похожие названия страниц с окончаниями (вроде "РСКД/Корон" и "РСКД/Корона"). для поиска ошибочных ссылок\
        # # [[s:ru:Обсуждение:Реальный словарь классических древностей#Викиссылки]]
        # links_and_likes_titles = [(l, t) for l in all_links for t in all_found_titles if t.startswith(l) and t != l]
        # # только в редиректах
        # g = [(l, r['t']) for l in all_links for r in redirects if r['t'].startswith(l) and r['t'] != l]
        #
        # # find_entry =  [i['t'] for i in titles_and_links if 'РСКД/Ilya' in i['re']]
        #
        # # remove entry in dict by found value
        # # [titles_and_links.remove(i) for i in titles_and_links if i['t'] == 'РСКД/Русский указатель статей']
        # pass

    def find_sections_on_few_pages(self):
        pages_and_sections_titles = [(p['page_title'], re.findall(r'begin="([^"]+\+)"', p['page_text'])) for p in
                                     self.entries]
        doubles = []
        for p in pages_and_sections_titles:
            for a in p[1]:
                for p1 in pages_and_sections_titles:
                    if p1[0] == p[0]: continue
                    if a in p1[1]:
                        s = (p1[0], a)
                        if s not in doubles:
                            doubles.append(s)

    def process_page(self, pagename):
        page = self.open_page(pagename, wmp=False)

        pagename, article_name, page_obj = page['pagename'], page['article_name'], page['obj']
        page_text, page_text_original = page_obj.text, page_obj.text
        # page_title, page_text = e['page_title'], e['page_text']
        # if 'Толковый словарь Даля (2-е издание). Том 1 (1880).pdf/117' in pagename:
        #     return

        if 'pagequality level="4"' in page_text or 'pagequality level="3"' in page_text:
            return

        sections_so = re.findall(r'(<section begin="([^"]+)\+"[^>]*/>(.+?)<section end="\2\+" */>)(?! *{{tq)',
                                 page_text)
        for s in sections_so:
            s_full, s_name, s_text = s
            a = listdic_pop(self.dic_from_classesru, 'title', s_name, ignorecase=True)
            if a is None or a['text'].startswith("<strong>I</strong>"):
                self.no_articles.append([pagename, s_name, s_text])
                continue

            s_text_new = self.process_article(a)
            if '{{перенос2' in s_text:
                self.articles_with_perenos.append([pagename, s_name, s_text, s_text_new])
                continue
            if '{{перенос' in s_text:
                self.articles_with_perenos_all.append([pagename, s_name, s_text, s_text_new])

            # if '{{акут' in s_text or '{{Акут' in s_text:
            #     self.articles_with_akut.append([pagename, s_name, s_text, s_text_new])
            #     continue

            # repl = f'<section begin="{s_name}+" />{s_text_new}<section end="{s_name}+" />'
            # repl1 = '<section begin="{0}+" />{1}<section end="{0}+" />'.format(s_name, s_text_new)
            # p1 = page_text.replace(s_full, repl)
            # page_text = page_text.replace(s_full, repl)
            page_text = page_text.replace(s_full,
                                          f'<section begin="{s_name}+" reposted />{s_text_new}<section end="{s_name}+" />')
            # page_text = re.sub(s_full, f'<section begin="{s_name}+" />{s_text_new}<section end="{s_name}+" />', page_text)
            pass

        self.wiki_posting_page(page_obj, page_text, 'reposting from classes.ru')

    def process_article(self, a):
        title = a['title']
        txt = a['text']

        txt = re.sub(' - ', ' — ', txt)
        txt = re.sub(r'(\d)-(\d)', r'\1—\2 ', txt)
        txt = txt.replace('́', '{{акут}}')
        txt = txt.replace(' и пр.', ' ипр.')

        txt = re.sub('^\s*(<strong>)\s*(\w)(.+?)(</strong>)',
                     lambda m: m.group(1) + m.group(2).upper() + m.group(3).lower() + m.group(4),
                     txt)
        txt = self.html2wiki(txt)

        # To <small>
        # s2small = r' (м|ср|[Ии]сланд|[Мм]н|ч|[Оо]днократн|[Мм]ногокр|Ботан|[Зз]одческ|[Нн]аум|[Мм]онгольск|[Сс] офенск|[Уу]чен|[Вв]заимн|[Вв]озвр|[Ии]носказат|[Бб]езличн|[Бб]ол|[Дд]етск|[Уу]корит|[Уу]велич|[Сс]острадат|[Лл]ьстит|[Уу]низит|[Пп]резрит|[Лл]аскат|[Зз]ырянск|[АА]кад. Сл|грчск|[Пп]ольск|[Пп]ереводн|[Гг]рчск|[Тт]атарск|[Пп]ерсидск|[Уу]мад|[Пп]слт|[Чч]еляб|[Жж]ивотн|[Нн]апр|[Мм]адьярск|возм|о челов|ошибч),? '
        # s2small_strings = ['ярс.', 'яросл.', 'южн.', 'черноморск.', 'челяб.', 'церк.', 'фрнц.', 'фрн.', 'франц.', 'физич.', 'физ.',
        #      'учен.', 'урал.-казач.', 'унизит.', 'умад.', 'укорит.', 'увелич.', 'тмб.', 'татарск.', 'тамб.', 'стар.',
        #      'ср.', 'сострадат.', 'собират.', 'сев. вост.', 'сев-вост.', 'сар.', 'с франц.', 'с офенск.', 'с лат.',
        #      'с греч.', 'ряз.', 'пслт.', 'пск.', 'противопол.', 'прм.', 'презрит.', 'польск.', 'политч.',
        #      'персидск.', 'перм.', 'переводн.', 'ошибч.', 'особ.', 'оренб.', 'однократн.', 'об.', 'о челов.', 'немецк.',
        #      'нем.', 'нвг.', 'научн.', 'нареч.', 'нар. уф.', 'напр.', 'морск.', 'монгольск.', 'многокр.', 'мн. ч.',
        #      'мждмт.', 'мжд.', 'межд.', 'мед.', 'математ.', 'матем.', 'мадьярск.', 'м.', 'льстит.', 'латн.', 'лат.',
        #      'ласкат.', 'кур.', 'кмч.', 'католич.', 'как немецк.', 'каз.', 'кавк.', 'исланд.', 'ипр.', 'иносказат.', 'зырянск.',
        #      'зодческ.', 'зап.', 'животн.', 'ж.', 'детск.', 'грчск.', 'греч.', 'вят.', 'врчб.', 'врач.',
        #      'вост. тмб.', 'вост.', 'вор.', 'возм.', 'возвр.', 'воен.', 'влд.', 'влад.', 'взаимн.', 'бран.', 'ботан.',
        #      'более употреб. мн. ч.', 'бол.', 'безличн.', 'астроном.', 'арх.-мез.', 'арх.-кем.', 'арх.', 'акад. сл.',
        #      '(на длинной)', '(Наум.)']   # '(на длинной)', '(Наум.)'
        s2small_strings = ['ярс.', 'яросл.', 'южн.', 'черноморск.', 'челяб.', 'церк.', 'фрнц.', 'фрн.', 'франц.',
                           'физич.', 'физ.',
                           'учен.', 'урал.-казач.', 'унизит.', 'умад.', 'укорит.', 'увелич.', 'тмб.', 'татарск.',
                           'тамб.', 'стар.',
                           'ср.', 'сострадат.', 'собират.', 'сев-вост.', 'сар.', 'с франц.', 'с офенск.', 'с лат.',
                           'с греч.', 'ряз.', 'пслт.', 'пск.', 'противопол.', 'прм.', 'презрит.', 'польск.', 'политч.',
                           'персидск.', 'перм.', 'переводн.', 'ошибч.', 'особ.', 'оренб.', 'однократн.', 'об.',
                           'о челов.', 'немецк.',
                           'нем.', 'нвг.', 'научн.', 'нареч.', 'нар. уф.', 'напр.', 'морск.', 'монгольск.', 'многокр.',
                           'мн. ч.',
                           'мждмт.', 'мжд.', 'межд.', 'мед.', 'математ.', 'матем.', 'мадьярск.', 'м.', 'льстит.',
                           'латн.', 'лат.',
                           'ласкат.', 'кур.', 'кмч.', 'католич.', 'как немецк.', 'каз.', 'кавк.', 'исланд.', 'ипр.',
                           'иносказат.', 'зырянск.',
                           'зодческ.', 'зап.', 'животн.', 'ж.', 'детск.', 'грчск.', 'греч.', 'вят.',
                           'врчб.', 'врач.',
                           'вост. тмб.', 'вост.', 'вор.', 'возм.', 'возвр.', 'воен.', 'влд.', 'влад.', 'взаимн.',
                           'бран.', 'ботан.',
                           'более употреб. мн. ч.', 'бол.', 'безличн.', 'астроном.', 'арх.-мез.', 'арх.-кем.', 'арх.',
                           'акад. сл.', ]
        s2small = self.list_strings2re(s2small_strings, space_frap=True)
        # txt = re.sub('(?<!<small>)' + s2small + '(?!</small>)', 'tttt', ' ярс. <small>ярс.</small> (Наум.) ненн ярсг')
        # txt = re.sub(s2small, r' <small>\1.</small> ', txt)
        # txt = re.sub('(?:<small>)?(более употреб\.)(?:</small>)? *(?:<small>)?(мн\.(?: ч\.)?)(?:</small>)', '<small>$1 $2</small>', txt)
        txt = re.sub('(?<!<small>)' + s2small + '(?!</small>)', r'<small>\1</small>', txt)

        txt = re.sub('<a href="russian-dictionary-Dal-term-[^>]+?>(.+?)</a>', r'{{tsdl|\1|\1|so}}', txt)

        return txt

    def html2wiki(self, txt):
        txt = txt.replace('|', '{{!}}')
        txt = re.sub('</?em>', "''", txt)
        txt = re.sub('</?strong>', "'''", txt)
        # txt = txt.replace('<em>', "''").replace('</em>', "''")
        # txt = txt.replace('<strong>', "'''").replace('</strong>', "'''")
        return txt

    def list_strings2re(self, lst, space_frap=False):
        """Замена в списке строк спецсимволов для re.sub() замен"""
        s1 = "|".join(map(lambda s: s.replace('.', r'\.').replace('(', r'\(').replace(')', r'\)'), lst))
        if space_frap:
            return r'(?<= )(\b(?:%s)(?= ))' % s1
        else:
            return r'(\b(?:%s))' % s1

    def reposting_from_classesru(self):
        # изменение и постинг статей
        for pagename in self.pagelists_titles:
            self.process_page(pagename)

    def process_page_reposting_do(self, pagename):
        page = self.open_page(pagename, wmp=False)

        pagename, article_name, page_obj = page['pagename'], page['article_name'], page['obj']
        page_text = page_obj.text

        if 'pagequality level="4"' in page_text or 'pagequality level="3"' in page_text:
            return

        sections_so_reposted = re.findall(
            r'(<section begin="([^"]+)\+" +reposted[^>]*>(.+?)<section end="\2\+" */>)(?! *{{tq)',
            page_text)
        for s in sections_so_reposted:
            s_full, s_name, s_text = s

            s_text = re.sub(r'({{tsdl\|[^|}]*\|[^|}]*)\|so(}})', r'\1\2', s_text)  # убрать 3й параметр из {{tsdl}}
            page_text = re.sub(
                # r'<section begin="{s_name}"[^>]*>.+?<section end="{s_name}" */>(?! *\{\{tq)'.format(s_name=s_name),
                fr'<section begin="{s_name}"[^>]*>.+?<section end="{s_name}" */>(?! *{{tq)',
                f'<section begin="{s_name}" reposted />{self.convert(s_text)}<section end="{s_name}" />',
                page_text)
            pass

        page_text = re.sub(r'tsdl\|([^|}]+)\|\1(?= *[|}])', r'tsdl|\1|',
                           page_text)  # убрать 2й параметр-дубль из {{tsdl}}

        self.wiki_posting_page(page_obj, page_text, 'reposting the reconverted DO')


def replaces_for_pwb():
    t = """\
    ж.
    ж.
    м.
    м.
    арх.-кем.
    арх.-кем.
    арх-кол.
    арх-кол.
    арх.-пин.
    арх.-пин.     
    влд-прсл.
    влд-прсл.  
    Вост.-сиб.
    Вост.-сиб.   
    вост-<small>сиб.</small>
    вост-сиб.
    дат. пад.
    дат. пад.
    зпд-<small>сиб.
    зпд-сиб.
    зпд-сиб.
    зпд-сиб.
    ирк-нрч.
    ирк-нрч.
    калужск.-мас.
    кал.-мас.
    каз.-цыв.
    каз.-цыв.
    моск.-вер.
    моск.-вер.
    ниж.-бал.
    ниж.-бал.
    <small>ниж.</small>-вос.
    ниж.-вос.
    ниж.-вос.
    ниж.-вос.
    ниж.-мак.
    ниж.-мак.
    нвг-брч.
    нвг-брч.
    новг.-кир.
    новг.-кир.
    нвг.-кир.
    нвг.-кир.
    орл-мц.
    орл-мц.
    петерб.-гдов.
    петерб.-гдов.
    ряз.-кас.
    ряз.-кас.
    сар-хвал.
    сар-хвал.
    симб.-корс.
    смб.-корс.
    <small>сев.</small>-вост.
    сев.-вост.
    сев.-вост.
    сев.-вост.
    урал.-казач.
    ур-казч.
    Урал.- ?<small>каз.</small>
    Урал.-каз.
    Уложение. Ал. Мх.
    Уложн. Ал. Мх.
    уптрб. также вм.
    уптрб. также вм.
    Ошибчн. говор. вм.
    Ошибчн. говор. вм.
    ошибочно вм.
    ошибочно вм.
    иногда употребл. вм.
    иногда употребл. вм.
    Иногда употребляется вм.
    Иногда употребл. вм.
    употребл. вм.
    употребл. вм.
    говор. иногда вм.
    говор. иногда вм.
    говор. вм.
    говор. вм.
    иногда вм.
    иногда вм.
    ошибочн. вм.
    ошибочн. вм.
    говор. вм.
    говор. вм.
    Англ.
    Англ.
    Астрах.
    Астрх.
    Арх.
    Арх.     
    безличн. 
    безлич.
    вм.
    вм.
    глаг.
    гл.
    Гнедич.
    Гнедич.
    горн.
    горн.
    грчск.
    грчск.
    длит. 
    дл.
    днепровск. 
    днепрв.
    донск.
    донс.
    донс.
    донс.
    влад. 
    влд.
    влд.
    влд.
    волжск. 
    волжс.
    волжс.
    волжс.
    вологодск.    
    влгд.
    влгд.
    влгд.
    Вологод. 
    Влгд.
    вологд.
    влгд.
    вор.
    вор.
    воен.
    воен.
    вост.
    вост.
    врач.
    врчб.
    вятс.
    вят.
    вят.
    вят.
    ипр.
    ипр.
    ирк.
    ирк.
    итал.
    итал.
    кавк.
    кавк.
    казач.
    казач.
    каз.
    каз.
    калужск. 
    кал.
    кем.
    кем.
    кмч.
    кмч.
    костр. 
    кстр.
    карельск.
    карел.
    крым.
    крым.
    Кур.
    Кур.    
    малорос. 
    млрс.    
    моск.
    мск.    
    мск.    
    мск.    
    морск. 
    морс.
    междомет.
    мждм.
    мн.
    мн.       
    нареч.
    нар.     
    новорос. 
    нврс.
    немецк. 
    нем.
    нем.
    нем.
    несклон. 
    нескл.    
    ниж.
    ниж.
    новг.
    нвг.
    нвг.
    нвг.      
    окончат. 
    окн.  
    олон. 
    ол. 
    ол. 
    ол. 
    оренб. 
    орнб.  
    остяцк.
    остяцк.
    Ошибчн.
    Ошибчн.    
    более употреб. 
    бол. уптрб.
    противопол.
    противоп.
    страдат.
    страдат.    
    собират.
    собир.            
    пенз.
    пен.    
    перм.
    прм.
    прм.
    прм.
    персидск.
    персидс.
    персидс.
    персидс.
    повелит.
    повлт.
    пск.
    пск.
    сар.
    сар.
    свадебн.
    свадебн.    
    сев.
    сев.
    симб.
    смб.
    смб.
    смб.
    смол. 
    смл.
    смл.
    смл.
    сиб. 
    сиб.        
    союз 
    со.    
    солдатское 
    солд.
    Стар.
    Стар.
    судебн.
    судебн.
    сущ.
    сущ.
    орл.
    орл.
    охотнич. 
    охотн.
    тамб. 
    тмб.
    тмб.
    тмб.
    татарск. 
    татр.
    твер. 
    твр.
    твр.
    твр.
    Тоб.
    Тоб.
    тул.
    тул.
    турецк.
    турец.
    турец.
    турец.
    увелич.
    увелич.
    умалит.
    умал.
    употреб. 
    уптрб.
    урал.
    урал.
    ряз.
    ряз.
    зап.
    зап.    
    южн. 
    юж.
    юж.
    юж.    
    франц.
    фрнц.
    шведск.
    шведс. 
    шуточн.
    шуточ.   
    церк. 
    црк.
    черноморск. 
    чернмр.
    чувашск.
    чувшс.
    Яросл. 
    Ярс.
    Ярс.
    Ярс."""

    # урал.-казач.
    # ур-казч.
    # урал.-казч.

    t1 = """\
    \(Шейн\)
    (Шейн)
    \(Наум\.\?\)
    (Наум.?)
    \(Наумов\)
    (Наумов)
    растен.
    раст.
    <small>сев.</small>-<small>вост.</small>
    <small>сев.-вост.</small>
    иногда говор. <small>вм.</small>
    иногда говор. вм.
    иногда употребл. <small>вм.</small>
    иногда употребл. вм.
    <small>уптрб.</small> <small>вм.</small>   
    употр. вм. 
    <small>уптрб.</small> вм.
    уптрб. вм.
    употребл. <small>вм.</small>
    употребл. вм.
    уптреб. и <small>вм.</small>
    уптреб. и вм.
    <small>уптрб.</small> также <small>вм.</small>
    уптрб. также вм.
    <small>Уптрб.</small> также вм.
    <small>Уптрб.</small> также вм.
    <small>уптрб.</small> также вм.
    уптрб. также вм.
    <small>также</small> вм.
    также вм.
    иногда <small>вм.</small>
    иногда вм.
    <small>страдат.</small> и <small>возвр.</small>
    стрд. и взв."""

    t2 = """\
    действ. по глаг.
    дейст. по гл.
    действ. по знач. глаг. 
    дейст. по знч. гл.
    действ. по <small>гл.</small>
    дейст. по гл.
    состояние по значению прилаг. 
    сост. по знач. прлг.
    страдат. и <small>возвр.</small> 
    <small>страдат. и возвр.</small>    
    в <small>противопол.</small> 
    <small>в противоп.</small>   
    <small>страдат.</small> и <small>возвр.</small>
    <small>страдат. и возвр.</small>    
    <small>умал.</small> и унизит.
    <small>умал.</small> и унизит.
    вообще действие <small>гл.</small> 
    вообще действие <small>гл.</small> """

    # '''(?<!{{!}}){{!}}(?!{{!}})
    #     {{!}}{{!}}'''

    lst = t.split('\n')
    lst1 = t1.split('\n')

    # замены с тегом <small> и регистром первой буквы
    e = read_list_interlines(lst, strip_lines=True)
    # r = [(r'([%s%s])%s' % (s[0][0].upper(), s[0][0].lower(), s[0][1:].replace('.', r'\.')), s[1]) for s in e]
    # r = [(r'([%s%s])%s' % (s[0][0].upper(), s[0][0].lower(), s[0][1:].replace('.', r'\.').replace(',', r'[.,]')), s[1]) for s in e]
    r = []
    for s in e:
        a = r'([%s%s])%s' % (s[0][0].upper(), s[0][0].lower(), s[0][1:])
        # a = re.sub(r'[.,]', r'[.,]', a)
        a = a.replace('.', r'\.')
        b = (a, s[1])
        r.append(b)

    # простые замены
    e1 = read_list_interlines(lst1, strip_lines=True)
    # e1 = [(s[0], s[1]) for s in e1]

    r1 = []
    for s in e1:
        # a = r'([%s%s])%s' % (s[0][0].upper(), s[0][0].lower(), s[0][1:])
        a = re.sub(r'[.,]', r'[.,]', s[0])
        b = (a, s[1])
        r1.append(b)

    y = []

    # простые замены со <small>
    # for s in r1:
    #     e = r'(begin=")([^"]+\+)(" *reposted[ /]*>.+?)\b%s(.+?<section end="\2"[ /]*>)' % s[0]
    #     y.append(e)
    #     e = r'\1\2\3<small>%s</small>\4' % s[1]
    #     y.append(e)

    # простые замены
    # for s in r1:
    #     e = r'(begin=")([^"]+\+)(" *reposted[ /]*>.+?)\b%s(.+?<section end="\2"[ /]*>)' % s[0]
    #     y.append(e)
    #     e = r'\1\2\3%s\4' % s[1]
    #     y.append(e)

    # коррекция "слово''." → "слово.''"
    # for s in r:
    #     if s[0].endswith('.') or s[0].endswith('[.,]'):
    #         w = r'''(begin=")([^"]+\+)(" *reposted[ /]*>.+?)\b%s''\.([^'].+?<section end="\2"[ /]*>)''' % s[0][:-1]
    #         y.append(w)
    #         w = r'\1\2\3%s\5' % (r"\4%s.''" % s[1][1:-1])
    #         y.append(w)

    # # <small>
    for s in r:
        e = r'(begin=")([^"]+\+)(" *reposted[ /]*>.+?)(?<!\<small>)\b%s(?!</small>)(.+?<section end="\2"[ /]*>)' % s[0]
        y.append(e)
        e = r'\1\2\3%s\5' % (r'<small>\4%s</small>' % s[1][1:])
        y.append(e)

    for s in r:
        e = r'(begin=")([^"]+\+)(" *reposted[ /]*>.+?)\b%s(.+?<section end="\2"[ /]*>)' % s[0]
        y.append(e)
        e = r'\1\2\3%s\5' % (r'\4%s' % s[1][1:])
        y.append(e)

    # y=y*10

    # v = '\n'.join(y)
    file_savelines('/home/vladislav/var/dal/repl2.txt', y)


if __name__ == "__main__":
    # parseBookXML(xml_path_wikidump)
    # pass

    main = Main()
    main.get_pagelists(from_file=True, path='/home/vladislav/var/dal/dal_indexpages.txt')
    # main.pagelists_titles = ['Страница:Толковый словарь Даля (2-е издание). Том 1 (1880).pdf/584', ]

    # main.work_xml_wikidump()
    # main.dic_from_classesru = list(csv_read_dict('/home/vladislav/var/dal/tsd2_from_classess_ru.csv'))
    # main.reposting_from_classesru()

    # репостинг ДО секций, новой конвертаций из секций СО на этих же страницах
    for pagename in main.pagelists_titles:
        main.process_page_reposting_do(pagename)

    pass

    # replaces_for_pwb()
