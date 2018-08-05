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

    def __init__(self, cls_parse_to_wiki, filepath=''):
        self.filepath = filepath
        self.filename = filepath.split('/')[-1]
        pagenum = re.search('(\d+)\.\w*$', filepath)
        self.pagenum = int(pagenum.group(1)) if pagenum else None
        self.text_source = file_readtext(filepath)
        # self.parsed_xml = cls_parse_to_wiki.work_xml_wikidump(filepath)
        # self.parsed_xml = cls_parse_to_wiki.parseBookXML(self.text_source)
        self.parsed_text = cls_parse_to_wiki.parseFB2XMLasText(self.text_source)

        pass
        print()

if __name__ == '__main__':
    cls_parse_to_wiki = Parse_to_wiki()
    filepaths = filepaths_of_directory('/home/vladislav/var/platon-fedon-fb2', '.fb2')
    filepaths = ['/home/vladislav/var/platon-fedon-fb2/platon-fedon - 0009.fb2']
    pages = []
    for fp in filepaths:
        page = Pagedata(cls_parse_to_wiki, fp, )
        pages.append(page)
        print()
