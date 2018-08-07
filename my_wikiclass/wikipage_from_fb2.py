#!/usr/bin/env python3
# coding: utf-8
from io import StringIO
from xml.etree import ElementTree as ET
import re
import operator
# import mwparserfromhell
from pywikibot import xmlreader
from vladi_commons.file_helpers import file_readtext, filepaths_of_directory, file_savetext
from my_wikiclass.parse_to_wiki import Parse_to_wiki
from my_wikiclass.format_text_to_wiki_indexpage import FormatText_to_WikiIndexPage

range_pages_metric = [
    [-1, 7, 157],
]


class Pagedata:

    def __init__(self, cls_parse_to_wiki, filepath, workpagename, bookvolume_num='', parse_from_fb2_file=False):
        self.filepath = filepath
        self.filename = filepath.split('/')[-1]
        scanpagenum = re.search('(\d+)\.\w*$', filepath)
        self.scanpagenum = int(scanpagenum.group(1)) if scanpagenum else None
        self.pagename = mkindexpage.scan_page_name(workpagename, self.scanpagenum, volume_num=bookvolume_num)
        self.text_source = file_readtext(filepath)
        if parse_from_fb2_file:
            # self.parsed_xml = cls_parse_to_wiki.work_xml_wikidump(filepath)
            # self.parsed_xml = cls_parse_to_wiki.parseBookXML(self.text_source)
            self.parsed_text = cls_parse_to_wiki.parseFB2XMLasText(self.text_source)
        self.posttext = ''


if __name__ == '__main__':
    cls_parse_to_wiki = Parse_to_wiki()
    mkindexpage = FormatText_to_WikiIndexPage()
    filepaths = filepaths_of_directory('/home/vladislav/var/platon-fedon-fb2', '.fb2')
    # filepaths = ['/home/vladislav/var/platon-fedon-fb2/fedon - 0006.fb2']
    workpagename = 'Федон (Платон, Лебедев).pdf'
    pages = []
    for fp in filepaths:
        page = Pagedata(cls_parse_to_wiki, fp, workpagename, parse_from_fb2_file=True)

        # # section_text = mkindexpage.wrap_to_section_tag(page.parsed_text, subpagename)
        # text = mkindexpage.precorrection(page.parsed_text)
        # text = mkindexpage.wrap_to_VARtpl(text)
        # book_pn = mkindexpage.calc_bookpagenum_by_scanpagenum(page.scanpagenum, range_pages_metric)
        # # colontitul= mkindexpage.make_colontitul(roman.toRoman(book_pn), subpagename)
        # colontitul = mkindexpage.make_colontitul_center_only(book_pn) if book_pn else ''
        # scanpagetext = mkindexpage.make_pagetext(text, colontitul, colontitul_on_top=True)
        # page.posttext = mkindexpage.formatting_output_page(
        # page, range_pages_metric, do_precorrection=True, colontitul_center_only=True, wrap_to_VARtpl=True)

        pages.append(page)

    # pages_sorted = sorted(pages, key=key)
    pages.sort(key=operator.attrgetter('scanpagenum'))

    re_perenos_start = re.compile('(\w+)-$')
    re_perenos_second = re.compile('^(\w+)')
    for i, p in enumerate(pages):
        perenos_begin_re = re_perenos_start.search(p.parsed_text)
        if perenos_begin_re:
            text_next_page = pages[i + 1].parsed_text
            perenos_begin = perenos_begin_re.group(1)
            perenos_end_re = re_perenos_second.search(text_next_page)
            perenos_end = perenos_end_re.group(1) if perenos_end_re else ''
            p.parsed_text = re_perenos_start.sub(r'{{перенос|%s|%s}}' % (perenos_begin, perenos_end), p.parsed_text)
            text_next_page = re_perenos_second.sub(r'{{перенос2|%s|%s}}' % (perenos_begin, perenos_end), text_next_page)
            pages[i + 1].parsed_text = text_next_page
        #     print()
        # print()

    for page in pages:
        page.posttext = mkindexpage.formatting_output_page(
            page, range_pages_metric, do_precorrection=True, colontitul_center_only=True, wrap_to_VARtpl=True)
    topost = [mkindexpage.make_pwb_page(p.pagename, p.posttext) for p in pages]
    topostall = '\n'.join(topost)

    file_savetext('/tmp/fedon.txt', topostall)
    print()
