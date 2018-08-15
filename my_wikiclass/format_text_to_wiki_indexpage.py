#!/usr/bin/env python3
# coding: utf-8
from io import StringIO
from xml.etree import ElementTree as ET
import re
# import mwparserfromhell
from pywikibot import xmlreader
from vladi_commons.file_helpers import file_readtext, filepaths_of_directory
from my_wikiclass.parse_to_wiki import Parse_to_wiki
from my_wikiclass.deyatificator import deyatificator
import roman


class FormatText_to_WikiIndexPage:

    def formatting_output_page(self, page, range_pages_metric, colontitul_center_only=False, wrap_to_VARtpl=False,
                               deyatification=False, do_precorrection=True, colontitul_on_top=True):
        text = page.parsed_text
        # section_text = mkindexpage.wrap_to_section_tag(page.parsed_text, subpagename)

        if do_precorrection:
            text = self.precorrection(text)

        # Конвертировать текст в современную орфографию
        page.neworph_text = deyatificator(text) if deyatification else ''

        if wrap_to_VARtpl:
            text = self.wrap_to_VARtpl(text, page.neworph_text)
        book_pn, is_roman = self.calc_bookpagenum_by_scanpagenum(page.scanpagenum, range_pages_metric)

        if colontitul_center_only:
            colontitul = self.make_colontitul_center_only(book_pn, is_roman) if book_pn else ''
        else:
            # todo ? range_pages_metric.subpagename
            subpagename = ''
            colontitul = self.make_colontitul(book_pn, is_roman, subpagename)

        scanpagetext = self.make_pagetext(text, colontitul, colontitul_on_top=colontitul_on_top)
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
    def make_colontitul(book_pn, subpagename='', is_roman=False):

        def label_interpages(number: int, string_chet: str, str_nechet: str) -> str:
            """Возвращает строку в зависимости чётная ли страница"""
            return str(string_chet) if not number % 2 else str(str_nechet)

        colontitul = ''
        colontitul_center = ''
        colontitul_left = ''
        colontitul_right = ''

        # colontitul = 'Народная Русь' if not scan_pn % 2 else subpagename  # чередующийся на чётных/нечётных страницах
        # colontitul = (colontitul + '.').upper()  # в верхнем регистре с точкой
        # colontitul = str(page_pn)  # колонтитул — номер страницы
        # чередующийся на чётных/нечётных страницах

        # colontitul = ''
        first_pages_without_colontitul = True  # на первых страницах без колонтитула

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

        # colontitul_center = label_interpages(page_pn, (subpagename + '.').upper().replace(' ВВЕДЕНИЕ (КАРПОВ).', ''), '')
        # if colontitul_center == '':  colontitul_center = 'ВВЕДЕНІЕ.'

        if book_pn != '':
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

        if colontitul_center == colontitul_left == colontitul_right == '':
            return ''

        if is_roman:
            # todo: toRoman need int
            colontitul_center = roman.toRoman(colontitul_center)
            colontitul_left = roman.toRoman(colontitul_left)
            colontitul_right = roman.toRoman(colontitul_right)

        colontitul = f'{{{{колонтитул|{colontitul_left}|{colontitul_center}|{colontitul_right}}}}}'

        # на первых страницах без колонтитула
        # if first_pages_without_colontitul and page_pn == page[1]:
        # 	colontitul = ''

        return colontitul

    @staticmethod
    def make_colontitul_center_only(string, is_roman=False):
        if is_roman:
            string = roman.toRoman(int(string))
        colontitul = f'{{{{колонтитул||{str(string)}|}}}}'
        return colontitul

    @staticmethod
    def wrap_to_section_tag(text, sectionname=''):
        return f'<section begin="{sectionname}" />{text}<section end="{sectionname}" />'

    @staticmethod
    def wrap_to_VARtpl(text_oldorph='', text_neworph=''):
        return '{{ВАР\n|%s\n|%s}}' % (text_oldorph, text_neworph)

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
        text = text.replace('&apos;', "'")
        text = re.sub('([„”«»]|&quot;)', '"', text)

        text = text.replace('</ref>\)', '</ref>')

        return text

    @staticmethod
    def perenos_slov(pages: list):
        """Расстановка шаблона {{перенос}} на страницы со словом, и {{перенос2}} на след. страницы"""
        re_perenos_start = re.compile('(\w+)-$')
        re_perenos_second = re.compile('^(\w+)')
        for i, p in enumerate(pages):
            perenos_begin_re = re_perenos_start.search(p.parsed_text)
            if perenos_begin_re:
                perenos_begin = perenos_begin_re.group(1)
                text_next_page = pages[i + 1].parsed_text
                perenos_end_re = re_perenos_second.search(text_next_page)
                perenos_end = perenos_end_re.group(1) if perenos_end_re else ''
                p.parsed_text = re_perenos_start.sub(r'{{перенос|%s|%s}}' % (perenos_begin, perenos_end), p.parsed_text)
                text_next_page = re_perenos_second.sub(r'{{перенос2|%s|%s}}' % (perenos_begin, perenos_end),
                                                       text_next_page)
                pages[i + 1].parsed_text = text_next_page

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
        is_roman = False
        for rangemetric in range_pages_metric:
            offset, start, end, is_roman = rangemetric
            if start <= scan_pn <= end:
                book_pn = scan_pn + offset
                break
        return book_pn, is_roman
