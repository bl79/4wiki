#!/usr/bin/env python3
# coding: utf-8
import requests
from urllib.parse import quote
from lxml import etree
from lxml.html import fromstring, tostring
from lxml import cssselect
from io import StringIO
from xml.etree import ElementTree as ET
import re
# import mwparserfromhell
import pywikibot
from pywikibot import output, xmlreader
from vladi_commons.file_helpers import file_savetext, file_readtext, filepaths_of_directory


class Parse_to_wiki:
    re_get_section = re.compile('<section>\s*(.*?)\s*</section>', flags=re.DOTALL)

    # теги p, b, emphasis
    re_tag_b = re.compile('</?b>')
    re_tag_emphasis = re.compile('</?emphasis>')
    re_tag_p = re.compile(r'<p>\s*(.*?)\s*</p>', flags=re.DOTALL)

    # чистка пробелов и абзацев
    re_tag_clean_emptylines = re.compile(r'^\s+$', flags=re.MULTILINE)
    re_tag_clean_spaces = re.compile(r' {2,}')
    re_tag_clean_newlines = re.compile(r'\n{2,}')


    def parseFB2XMLasText(self, xml: str):
        section = self.re_get_section.search(xml)
        if not section:
            return
        text = section.group(1)

        # теги p, b, emphasis
        text = self.re_tag_b.sub("'''", text)
        text = self.re_tag_emphasis.sub("''", text)
        text = self.re_tag_p.sub(r'\1\n\n', text)

        # чистка пробелов и абзацев
        text = self.re_tag_clean_emptylines.sub(r'', text)
        text = self.re_tag_clean_spaces.sub(r' ', text)
        text = self.re_tag_clean_newlines.sub(r'\n\n', text)

        return text

    def work_xml_wikidump(self, PATHTOXML: str):
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

    def parseBookXML(self, xml: str):
        # with open(xmlFile) as fobj:
        # 	xml = fobj.read()
        # xml = txt

        root = ET.fromstring(xml)
        # root = etree.parse('path_to_file')

        ns = {'t': "http://www.gribuser.ru/xml/fictionbook/2.0",
              'l': "http://www.w3.org/1999/xlink"}

        # b = root.find(".//t:description//t:genre", ns)
        # b = root.find(".//t:description", ns)
        # a = b.find(".//t:genre", ns).text

        for ab in root.findall("t:body", ns):
            for s in ab.find('t:section', ns):
                a = s.text

        parser = ET.XMLParser(ns_clean=True)
        tree = ET.parse(StringIO(xml), parser)

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
