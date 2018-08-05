#!/usr/bin/env python3
# coding: utf-8
from io import StringIO
from xml.etree import ElementTree as ET
import re
# import mwparserfromhell
from pywikibot import xmlreader
from vladi_commons.file_helpers import file_readtext, filepaths_of_directory
from my_wikiclass.parse_to_wiki import Parse_to_wiki


class Pagedata:
    re_get_section = re.compile('<section>\s*(.*?)\s*</section>', flags=re.DOTALL)
    re_tag_b = re.compile('</?b>')
    re_tag_emphasis = re.compile('</?emphasis>')

    def __init__(self, filepath=''):

        filepath = '/home/vladislav/var/platon-fedon-fb2/platon-fedon - 0009.fb2'
        self.filepath = filepath
        self.filename = filepath.split('/')[-1]
        pagenum = re.search('(\d+)\.\w*$', 'laton-fedon - 0009.fb2')
        self.pagenum = pagenum.group(1) if pagenum else None
        self.text_source = file_readtext(filepath)
        # self.parsed_xml = self.work_xml_wikidump(filepath)
        # self.parsed_xml = self.parseBookXML(self.text_source)
        self.parsed_xml = self.parseFB2XMLasText(self.text_source)

        pass
        print()

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

    def parseBookXML(self, xml):
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

    re_tag_p = re.compile(r'<p>\s*(.*?)\s*</p>', flags=re.DOTALL)

    def parseFB2XMLasText(self, xml):
        # section = re.search('<section>(.*?)</section>', xml, flags=re.DOTALL)
        section = self.re_get_section.search(xml)
        if not section:
            return
        text = section.group(1)
        text = self.re_tag_b.sub("'''", text)
        text = self.re_tag_emphasis.sub("''", text)
        text = self.re_tag_p.sub(r'\1\n\n', text)

        text = re.sub(r'^\s+$', r'', text, flags=re.MULTILINE)
        text = re.sub(r' {2,}', r' ', text)
        text = re.sub(r'\n{2,}', r'\n\n', text)

        return text


if __name__ == '__main__':
    parse_to_wiki = Parse_to_wiki()
    filepaths = filepaths_of_directory('/home/vladislav/var/platon-fedon-fb2', '.fb2')
    for fp in filepaths:
        page = Pagedata(fp)
        print()
