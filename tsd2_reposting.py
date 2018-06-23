#!/usr/bin/env python
# coding: utf-8
import requests
from urllib.parse import urlencode, quote
# import vladi_commons
# from vladi_commons import vladi_commons
from vladi_commons.vladi_commons import csv_read_dict, csv_save_dict, json_store_to_file, json_data_from_file, file_readtext
import sqlite3
import json
from lxml.html import fromstring
import re
# import html5lib
from urllib.parse import urlparse, parse_qs, parse_qsl, unquote, quote

d = csv_read_dict('/home/vladislav/var/Даль словарь/tsd2_from_classess_ru.csv')
for a in d:
    txt, title, url = a['text'], a['title'], a['url']
    title_l = title.lower()
    txt = re.sub('^\s*(<strong>)(.)(.+?)(</strong>)',
                   lambda m: m.group(1) + m.group(2).upper() + m.group(3).lower() + m.group(4),
                   txt)
    pass





import re
from pywikibot import output, xmlreader
from urllib.parse import urlparse, parse_qs, parse_qsl, unquote, quote

wikilink_re1 = re.compile(r"\[\[РСКД/([^]|]+)")
wikilink_re2 = re.compile(r"\[\[../([^]|]+)")
wikilink_re3 = re.compile(r"\{[\{([wW]l\|([^}|]+)")
redirect_target_re = re.compile(r"#перенаправление \[\[([^]]+)")

all_found_titles = []
titles_and_links = []
redirects = []


def main():
    dump = xmlreader.XmlDump(PATHTOXML)
    # readPagesCount = 0
    for entry in dump.parse():
        if int(entry.ns) not in [0] \
                or not entry.title.startswith('РСКД/') \
                or 'РСКД/Словник' in entry.title \
                or 'РСКД/Русский указатель статей' == entry.title \
                or 'РСКД/Список сокращений названий трудов античных авторов' == entry.title:
            continue
        if entry.isredirect:
            redirects.append(dict(t=entry.title, r=redirect_target_re.search(entry.text).group(1)))

        if 'РСКД/Цезарь' in entry.title:
            print(entry.title)
        all_found_titles.append(entry.title)

        links = []
        links.extend(wikilink_re1.findall(entry.text))
        links.extend(wikilink_re2.findall(entry.text))
        links.extend(wikilink_re3.findall(entry.text))
        links = [f'РСКД/{l}' for l in links]
        if links:
            print({'t': entry.title, 're': links})
            titles_and_links.append({'t': entry.title, 're': links})

        # readPagesCount += 1
        # if readPagesCount % 10000 == 0:
        #     output("%i pages read..." % readPagesCount)

    pass
    # a = [links['re'] for links in titles_and_links]
    # all_links = {l for ls in a for l in ls}
    all_links = {l.rsplit('#')[0] for links in titles_and_links for l in links['re']}
    error_links = {l for l in all_links if l not in all_found_titles}
    # ltxt = '\n'.join([f'# [[{e}]]' for e in error_links])
    ltxt = '\n'.join([f'# [[{e}]] - [[Служебная:Ссылки сюда/{quote(e)}|ссылки сюда]]' for e in error_links])
    pass

    # ссылки у которых есть похожие названия страниц с окончаниями (вроде "РСКД/Корон" и "РСКД/Корона"). для поиска ошибочных ссылок\
    # [[s:ru:Обсуждение:Реальный словарь классических древностей#Викиссылки]]
    links_and_likes_titles = [(l, t) for l in all_links for t in all_found_titles if t.startswith(l) and t != l]
    # только в редиректах
    g = [(l, r['t']) for l in all_links for r in redirects if r['t'].startswith(l) and r['t'] != l]

    # find_entry =  [i['t'] for i in titles_and_links if 'РСКД/Ilya' in i['re']]

    # remove entry in dict by found value
    # [titles_and_links.remove(i) for i in titles_and_links if i['t'] == 'РСКД/Русский указатель статей']
    pass

if __name__ == "__main__":
    # parseBookXML(xml_path_wikidump)
    # pass
    main()
