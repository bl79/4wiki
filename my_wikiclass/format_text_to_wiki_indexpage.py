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


    @staticmethod
    def make_pagetext(text, sectionname='', colontitul='', colontitul_up=True, header='', footer=''):
        header_begin = f'<noinclude><pagequality level="1" user="TextworkerBot" /><div class="pagetext">' \
                       f'__NOEDITSECTION__<div class="serif">'
        header_end = f'<div class="indent"></noinclude>'
        if colontitul_up:
            if header == '':
                header = f'{header_begin}{colontitul}{header_end}<section begin="{sectionname}" />'
            # '<!--<div style="text-align:justify">-->'
            if footer == '':
                footer = '<section end="%s" /><noinclude><!-- -->\n<references /></div></div></div></noinclude>'
        else:
            if header == '':
                header = f'{header_begin}{header_end}'
            if footer == '':
                # footer = f'<section end="{sectionname}" /><noinclude><references />{colontitul}</div></noinclude>'
                footer = f'<noinclude><!-- -->\n<references />{colontitul}</div></div></div></noinclude>'
        # {{свр}}
        scanpagetext = header + text + footer
        return scanpagetext

    @staticmethod
    def make_colontitul(book_pn, subpagename):

        def label_interpages(number, string_chet, str_nechet):
            """Возвращает строку в зависимости чётная ли страница"""
            return string_chet if not number % 2 else str_nechet

        # colontitul = 'Народная Русь' if not scan_pn % 2 else subpagename  # чередующийся на чётных/нечётных страницах
        # colontitul = (colontitul + '.').upper()  # в верхнем регистре с точкой
        # colontitul = str(page_pn)  # колонтитул — номер страницы
        # чередующийся на чётных/нечётных страницах

        # colontitul = ''
        first_pages_without_colontitul = True  # на первых страницах без колонтитула

        subpagename = ''
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
        colontitul_params = [
            label_interpages(book_pn_int, str(book_pn), ''), colontitul_center,
            label_interpages(book_pn_int, '', str(book_pn))
            # римские цифры
            # label_interpages(book_pn, roman.toRoman(book_pn+32), ''),	colontitul_center, label_interpages(book_pn, '', roman.toRoman(book_pn+32))
            # '',	'— ' + str(book_pn) + ' —',	''
        ]
        colontitul = '{{колонтитул|' + '|'.join(colontitul_params) + '}}'

        # на первых страницах без колонтитула
        # if first_pages_without_colontitul and page_pn == page[1]:
        # 	colontitul = ''

        return colontitul
