#!/usr/bin/env python3
# coding: utf-8
# from io import StringIO
# from xml.etree import ElementTree as ET
import re
import operator
# import mwparserfromhell
# from pywikibot import xmlreader
from vladi_commons.file_helpers import file_readtext, filepaths_of_directory, file_savetext
from my_wikiclass.parse_to_wiki import Parse_to_wiki
from my_wikiclass.format_text_to_wiki_indexpage import FormatText_to_WikiIndexPage
import my_wikiclass.wikiworks_data as metaw


class Pagedata:

    def __init__(self, cls_parse_to_wiki, filepath, workpagename, bookvolume_num='', parse_from_fb2_file=False):
        self.filepath = filepath
        self.filename = filepath.split('/')[-1]
        scanpagenum = re.search('(\d+)\.\w*$', filepath)
        self.scanpagenum = int(scanpagenum.group(1)) if scanpagenum else None
        # if scanpagenum:
        #     pn = int(scanpagenum.group(1))
        #     pn += 1
        #     if pn >= 6:
        #         pn -= 1
        #     if pn >= 7:
        #         pn -= 1
        #     self.scanpagenum = pn
        # else:
        #     scanpagenum = None

        self.pagename = mkindexpage.scan_page_name(workpagename, self.scanpagenum, volume_num=bookvolume_num)
        self.text_source = file_readtext(filepath)
        self.parsed_text = cls_parse_to_wiki.parseFB2XMLasText(self.text_source) if parse_from_fb2_file else None
        self.posttext = ''


if __name__ == '__main__':
    m = metaw.Meta_platon_protagor()
    cls_parse_to_wiki = Parse_to_wiki()
    mkindexpage = FormatText_to_WikiIndexPage()
    filepaths = filepaths_of_directory(m.directory, '.fb2')
    # filepaths = ['/home/vladislav/var/platon-timeykritiy1883-fb2/timeykritiy1883 - 0132.fb2']
    # filepaths = ['/home/vladislav/var/platon-pir-fb2-fr12/pir - 0057.fb2']
    pages = [Pagedata(cls_parse_to_wiki, fp, m.workpagename, parse_from_fb2_file=m.parse_from_fb2_file)
             for fp in filepaths]

    pages.sort(key=operator.attrgetter('scanpagenum'))

    # расстановка шаблона {{перенос}} на страницы со словом, и {{перенос2}} на след. страницы
    mkindexpage.perenos_slov(pages)

    # форматировать страницы для ПИ Страница
    for page in pages:
        page.posttext = mkindexpage.formatting_output_page(
            page, m.range_pages_metric,
            do_precorrection=m.do_precorrection,
            colontitul_center_only=m.colontitul_center_only,
            colontitul_on_top=m.colontitul_on_top,
            deyatification=m.deyatification,
            wrap_to_VARtpl=m.wrap_to_VARtpl)
    # форматировать файл для pwb
    topost = [mkindexpage.make_pwb_page(p.pagename, p.posttext) for p in pages]
    topostall = '\n'.join(topost)
    file_savetext(m.filepaths_output_pwb, topostall)
