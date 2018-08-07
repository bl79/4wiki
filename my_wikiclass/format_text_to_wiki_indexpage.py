#!/usr/bin/env python3
# coding: utf-8
from io import StringIO
from xml.etree import ElementTree as ET
import re
# import mwparserfromhell
from pywikibot import xmlreader
from vladi_commons.file_helpers import file_readtext, filepaths_of_directory
from my_wikiclass.parse_to_wiki import Parse_to_wiki
import roman


class FormatText_to_WikiIndexPage:

    def formatting_output_page(self, page, range_pages_metric, colontitul_center_only=False, wrap_to_VARtpl=False,
                               do_precorrection=True):
        text = page.parsed_text
        # section_text = mkindexpage.wrap_to_section_tag(page.parsed_text, subpagename)
        if do_precorrection:
            text = self.precorrection(text)
        if wrap_to_VARtpl:
            text = self.wrap_to_VARtpl(text)
        book_pn = self.calc_bookpagenum_by_scanpagenum(page.scanpagenum, range_pages_metric)

        if colontitul_center_only:
            colontitul = self.make_colontitul_center_only(book_pn) if book_pn else ''
        else:
            # todo ? range_pages_metric.subpagename
            colontitul = self.make_colontitul(roman.toRoman(book_pn), range_pages_metric.subpagename)

        scanpagetext = self.make_pagetext(text, colontitul, colontitul_on_top=True)
        return scanpagetext

    @staticmethod
    def make_pagetext(text, colontitul='', colontitul_on_top=True, header=None, footer=None):
        header_begin = f'<noinclude><pagequality level="1" user="TextworkerBot" /><div class="pagetext">' \
                       f'__NOEDITSECTION__<div class="serif">'
        header_end = f'<div class="indent"></noinclude>'
        if colontitul_on_top:
            if not header:
                header = f'{header_begin}{colontitul}{header_end}'
            # '<!--<div style="text-align:justify">-->'
            if not footer:
                footer = '<noinclude><!-- -->\n<references /></div></div></div></noinclude>'
        else:
            if not header:
                header = f'{header_begin}{header_end}'
            if not footer:
                footer = f'<noinclude><!-- -->\n<references />{colontitul}</div></div></div></noinclude>'
        scanpagetext = f'{header}{text}{footer}'
        return scanpagetext

    @staticmethod
    def make_colontitul(book_pn, subpagename=''):

        def label_interpages(number: int, string_chet: str, str_nechet: str) -> str:
            """Возвращает строку в зависимости чётная ли страница"""
            return str(string_chet) if not number % 2 else str(str_nechet)

        # colontitul = 'Народная Русь' if not scan_pn % 2 else subpagename  # чередующийся на чётных/нечётных страницах
        # colontitul = (colontitul + '.').upper()  # в верхнем регистре с точкой
        # colontitul = str(page_pn)  # колонтитул — номер страницы
        # чередующийся на чётных/нечётных страницах

        # colontitul = ''
        first_pages_without_colontitul = True  # на первых страницах без колонтитула

        colontitul_center = subpagename.upper()
        # colontitul_center = colontitul_center.replace(' (ПЛАТОН/КАРПОВ)', '').replace(' (ПСЕВДО-ПЛАТОН/КАРПОВ)', '').replace('КАРПОВ В. Н., ', '').replace('ПОЛИТИКА ИЛИ ГОСУДАРСТВО. ','')
        # if re.search(r'[цкнгшщзхфвпрлджчсмтбѳ]$', colontitul_center, re.I):
        # colontitul_center = colontitul_center + 'ъ'

        # colontitul_center = colontitul_center.replace('СОДЕРЖАНИЕ ', '').replace('ПЕРВОЙ КНИГИ', 'КНИГА ПЕРВАЯ').replace('ВТОРОЙ КНИГИ', 'КНИГА ВТОРАЯ').replace('ТРЕТЬЕЙ КНИГИ', 'КНИГА ТРЕТЬЯ').replace('ЧЕТВЕРТОЙ КНИГИ', 'КНИГА ЧЕТВЕРТАЯ').replace('ПЯТОЙ КНИГИ', 'КНИГА ПЯТАЯ').replace('ШЕСТОЙ КНИГИ', 'КНИГА ШЕСТАЯ').replace('СЕДЬМОЙ КНИГИ', 'КНИГА СЕДЬМАЯ').replace('ВОСЬМОЙ КНИГИ', 'КНИГА ВОСЬМАЯ').replace('ДЕВЯТОЙ КНИГИ', 'КНИГА ДЕВЯТАЯ').replace('ДЕСЯТОЙ КНИГИ', 'КНИГА ДЕСЯТАЯ')

        # colontitul_center = 'Платона.'
        # colontitul_center = label_interpages(page_pn, 'жизнь', colontitul_center)
        # colontitul_center = label_interpages(page_pn, 'О сочинениях', colontitul_center)
        # colontitul_center = label_interpages(page_pn, 'политика или государство', colontitul_center)
        # colontitul_center = 'ПРЕДИСЛОВІЕ'
        colontitul_center = colontitul_center.upper()
        # colontitul_center = colontitul_center + '.'
        colontitul_center = ''
        # colontitul_center = label_interpages(page_pn, (subpagename + '.').upper().replace(' ВВЕДЕНИЕ (КАРПОВ).', ''), '')
        # if colontitul_center == '':  colontitul_center = 'ВВЕДЕНІЕ.'

        book_pn_int = book_pn
        try:
            if not re.match('^\d+$', str(book_pn)):
                book_pn_int = roman.fromRoman(book_pn)
        except:
            pass

        colontitul_left = label_interpages(book_pn_int, book_pn, '')
        colontitul_right = label_interpages(book_pn_int, '', book_pn)
        # римские цифры
        # label_interpages(book_pn, roman.toRoman(book_pn+32), ''),	colontitul_center, label_interpages(book_pn, '', roman.toRoman(book_pn+32))
        # '',	'— ' + str(book_pn) + ' —',	''

        colontitul = f'{{{{колонтитул|{colontitul_left}|{colontitul_center}|{colontitul_right}}}}}'

        # на первых страницах без колонтитула
        # if first_pages_without_colontitul and page_pn == page[1]:
        # 	colontitul = ''

        return colontitul

    @staticmethod
    def make_colontitul_center_only(string):
        colontitul = f'{{{{колонтитул||{str(string)}|}}}}'
        return colontitul

    @staticmethod
    def wrap_to_section_tag(text, sectionname=''):
        return f'<section begin="{sectionname}" />{text}<section end="{sectionname}" />'

    @staticmethod
    def wrap_to_VARtpl(text=''):
        text = text.strip()
        return f'{{{{ВАР\n|{text}\n|{text}}}}}'

    @staticmethod
    def make_pwb_page(pagename, pagetext):
        pwb_post_page = "{{-start-}}\n" \
                        "'''%s'''\n" \
                        "%s\n" \
                        "{{-stop-}}\n" % (pagename, pagetext)
        return pwb_post_page

    @staticmethod
    def precorrection(text):
        text = re.sub('(\w+)-$', r'{{перенос|\1|}}', text, flags=re.MULTILINE)
        return text

    @staticmethod
    def scan_page_name(workpagename: str, scan_pn, volume_num=None):
        pagename = f'Страница:{workpagename}/{str(scan_pn)}'
        if '%s' in workpagename:
            pagename = pagename % volume_num
        return pagename

    @staticmethod
    def pagenum_to_scanpagenum(pagenum, offset: int) -> int:
        scanpagenum = int(pagenum) + offset
        return scanpagenum

    @staticmethod
    def scanpagenum_to_pagenum(scanpnum, offset: int) -> int:
        scanpagenum = int(scanpnum) + offset
        return scanpagenum

    @staticmethod
    def calc_scanpagenum_by_bookpagenum(book_pn, range_pages_metric: list) -> dict:
        book_pn = int(book_pn)
        scan_pn = ''
        for rangemetric in range_pages_metric:
            offset, start, end = rangemetric
            if start <= book_pn <= end:
                scan_pn = book_pn + offset
                break
        return scan_pn

    @staticmethod
    def calc_bookpagenum_by_scanpagenum(scan_pn, range_pages_metric: list):
        scan_pn = int(scan_pn)
        book_pn = ''
        for rangemetric in range_pages_metric:
            offset, start, end = rangemetric
            if start <= scan_pn <= end:
                book_pn = scan_pn + offset
                break
        return book_pn
