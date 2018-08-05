#!/usr/bin/env python3
# coding: utf-8
import requests
from urllib.parse import quote
from lxml import etree
from lxml.html import fromstring, tostring
from lxml import cssselect
import re
# import mwparserfromhell
import pywikibot
import roman
from vladi_commons.file_helpers import file_savetext, file_readtext
from my_wikiclass.format_text_to_wiki_indexpage import FormatText_to_WikiIndexPage

text2upload = 'pages_to_bot_upload.csv'
csvrows = []



def normalization_pagename(t):
    """ Первая буква в верхний регистр, ' ' → '_' """
    t = t.strip()
    return t[0:1].upper() + t[1:].replace(' ', '_')


class openwikipage:
    def __init__(self, project, book, subpagename, prefix='', postfix=''):
        self.subpagename = subpagename
        self.site = pywikibot.Site('ru', project)
        self.page = pywikibot.Page(self.site, prefix + book + postfix + '/' + str(subpagename))
        self.text = self.page.get()

    # wikicode = mwparserfromhell.parse(self.text)

    def save(self, edit_comment=''):
        self.page.save(edit_comment)

    def save2file(self):
        file_savetext(wikipages_filename, text)


# article_page = openwikipage(project, book, subpagename)


# site = pywikibot.Site('ru', 'wikisource')
# book = 'Пословицы русского народа (Даль)' + '/'
book = ''
# index = 'Сочинения Платона (Платон, Карпов). Том 5, 1879.pdf:ВТ'  # без префикса "Индекс:"
# wordlist : имя викистраницы, стр. книги, имена секций


path = '/home/vladislav/var/tolstoy/html/parsed/'
volumes_from_file = [
    # {
    # 	'filename': 1,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[3, 26, 19],
    # 		[27, 95, 20],
    # 		[97, 101, 19],
    # 		[103, 166, 18],
    # 		[167, 212, 19],
    # 		[213, 302, 20],
    # 		[305, 358, 19],
    # 	],
    # 	'roman_offset': [3, 23, -1],
    # },
    # {
    # 	'filename': 2,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 75, 12],
    # 		[79, 237, 10],
    # 		[241, 252, 8],
    # 		[253, 296, 9],
    # 		[297, 302, 10],
    # 		[303, 342, 11],
    # 		[343, 346, 12],
    # 		[349, 401, 11],
    # 		[403, 417, 10],
    # 	],
    # 	'roman_offset': [1, 11, 1],
    # },
    # {
    # 	'filename': 3,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 11, 0],
    # 		[13, 80, -1],
    # 		[81, 112, 1],
    # 		[113, 212, 2],
    # 		[215, 268, 1],
    # 		[269, 283, 2],
    # 		[286, 348, 0],
    # 	],
    # 	'roman_offset': [1, 11, 1],
    # },
    # {
    # 	'filename': 4,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 116, 11],
    # 		[117, 119, 12],
    # 		[122, 171, 10],
    # 		[173, 278, 9],
    # 		[281, 308, 8],
    # 		[309, 364, 9],
    # 		[365, 380, 10],
    # 		[383, 450, 9],
    # 	],
    # 	'roman_offset': [1, 11, 0],
    # },
    # {
    # 	'filename': 5,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 48, 11],
    # 		[49, 65, 12],
    # 		[67, 143, 11],
    # 		[145, 256, 10],
    # 		[257, 273, 11],
    # 		[277, 376, 9],
    # 	],
    # 	'roman_offset': [1, 10, 0],
    # },
    # {
    # 	'filename': 6,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 152, 12],
    # 		[153, 162, 11],
    # 		[163, 176, 12],
    # 		[177, 190, 13],
    # 		[191, 269, 14],
    # 		[271, 316, 13],
    # 	],
    # },
    # {
    # 	'filename': 7,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 54, 12],
    # 		[55, 106, 11],
    # 		[107, 314, 12],
    # 		[315, 341, 13],
    # 		[344, 432, 11],
    # 	],
    # 	'roman_offset': [5, 11, 2],
    # },
    # {
    # 	'filename': 8,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 16, 14],
    # 		[17, 32, 15],
    # 		[33, 373, 16],
    # 		[377, 464, 14],
    # 		[465, 480, 15],
    # 		[481, 665, 16],
    # 	],
    # 	'roman_offset': [1, 12, 0],
    # },
    # {
    # 	'filename': 9,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 158, 16],
    # 		[159, 352, 18],
    # 		[353, 519, 19],
    # 	],
    # 	'roman_offset': [1, 15, 1],
    # },
    # {
    # 	'filename': 10,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 64, 6],
    # 		[65, 112, 7],
    # 		[113, 160, 8],
    # 		[161, 433, 9],
    # 	],
    # },
    # {
    # 	'filename': 11,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 318, 7],
    # 		[319, 470, 9],
    # 	],
    # },
    # {
    # 	'filename': 12,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 186, 6],
    # 		[187, 232, 7],
    # 		[235, 341, 6],
    # 		[343, 428, 5],
    # 	],
    # },
    # {
    # 	'filename': 13,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 9, 2],
    # 		[12, 40, 0],
    # 		[41, 78, 1],
    # 		[79, 150, 2],
    # 		[151, 883, 3],
    # 	],
    # },
    # {
    # 	'filename': 14,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 9, 2],
    # 		[11, 448, 1],
    # 	],
    # },
    # {
    # 	'filename': 15,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 181, 1],
    # 		[185, 338, -1],
    # 	],
    # },
    # {
    # 	'filename': 16,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 16, 1],
    # 		[19, 259, 0],
    # 	],
    # },
    # {
    # 	'filename': 17,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 55, 11],
    # 		[59, 132, 9],
    # 		[135, 156, 8],
    # 		[157, 280, 9],
    # 		[281, 312, 10],
    # 		[313, 465, 11],
    # 		[468, 814, 10],
    # 	],
    # 	'roman_offset': [1, 11, 1],
    # },
    # {
    # 	'filename': 18,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 90, 11],
    # 		[91, 224, 12],
    # 		[225, 364, 13],
    # 		[365, 557, 14],
    # 	],
    # 	'roman_offset': [1, 10, 1],
    # },
    # {
    # 	'filename': 19,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 14, 6],
    # 		[15, 348, 7],
    # 		[349, 396, 8],
    # 		[397, 399, 9],
    # 		[401, 520, 8],
    # 	],
    # },
    # {
    # 	'filename': 20,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 50, 10],
    # 		[51, 92, 11],
    # 		[93, 573, 12],
    # 		[576, 688, 10],
    # 	],
    # 	'roman_offset': [1, 10, 1],
    # },
    # {
    # 	'filename': 21,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 5, 42],
    # 		[7, 12, 41],
    # 		[13, 100, 42],
    # 		[102, 141, 41],
    # 		[145, 200, 39],
    # 		[203, 261, 38],
    # 		[265, 338, 36],
    # 		[340, 412, 35],
    # 		[413, 434, 36],
    # 		[435, 476, 37],
    # 		[477, 543, 38],
    # 		[547, 695, 36],
    # 	],
    # 	'roman_offset': [1, 39, 4],
    # },
    # {
    # 	'filename': 22,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 13, 2],
    # 		[15, 174, 1],
    # 		[175, 196, 2],
    # 		[199, 361, 1],
    # 		[365, 367, -1],
    # 		[369, 553, -2],
    # 		[557, 559, -4],
    # 		[561, 791, -5],
    # 	],
    # },
    # {
    # 	'filename': 23,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 465, 38],
    # 		[468, 483, 36],
    # 		[486, 512, 34],
    # 		[514, 584, 33],
    # 	],
    # 	'roman_offset': [1, 35, 3],
    # },
    # {
    # 	'filename': 24,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 798, 2],
    # 		[801, 938, 1],
    # 		[941, 969, 0],
    # 		[973, 1012, -2],
    # 	],
    # },
    # {
    # 	'filename': 25,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[4, 169, 11],
    # 		[173, 246, 9],
    # 		[247, 410, 10],
    # 		[411, 507, 11],
    # 		[511, 916, 9],
    # 	],
    # 	'roman_offset': [1, 12, 2],
    # },
    # {
    # 	'filename': 26,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 119, 11],
    # 		[123, 243, 9],
    # 		[245, 304, 8],
    # 		[307, 309, 7],
    # 		[313, 520, 5],
    # 		[521, 951, 6],
    # 	],
    # 	'roman_offset': [1, 11, 1],
    # },
    # {
    # 	'filename': 27,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[3, 92, 11],
    # 		[95, 238, 10],
    # 		[239, 262, 11],
    # 		[265, 349, 10],
    # 		[353, 408, 8],
    # 		[409, 534, 9],
    # 		[535, 558, 10],
    # 		[562, 766, 8],
    # 	],
    # 	'roman_offset': [1, 11, 2],
    # },
    # {
    # 	'filename': 28,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 220, 42],
    # 		[221, 306, 44],
    # 		[309, 330, 43],
    # 		[333, 398, 42],
    # 	],
    # 	'roman_offset': [1, 39, 3],
    # },
    # {
    # 	'filename': 29,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 53, 31],
    # 		[57, 230, 29],
    # 		[233, 248, 28],
    # 		[251, 291, 27],
    # 		[295, 336, 25],
    # 		[337, 371, 26],
    # 		[375, 452, 24],
    # 	],
    # 	'roman_offset': [1, 28, 4],
    # },
    # {
    # 	'filename': 30,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 24, 31],
    # 		[27, 206, 30],
    # 		[209, 270, 29],
    # 		[273, 483, 28],
    # 		[485, 608, 27],
    # 	],
    # 	'roman_offset': [1, 28, 4],
    # },
    # {
    # 	'filename': 31,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[3, 46, 25],
    # 		[47, 65, 26],
    # 		[69, 101, 24],
    # 		[105, 112, 22],
    # 		[115, 200, 21],
    # 		[203, 216, 20],
    # 		[217, 254, 21],
    # 		[257, 326, 20],
    # 	],
    # 	'roman_offset': [1, 23, 4],
    # },
    # {
    # 	'filename': 32,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 50, 12],
    # 		[51, 104, 13],
    # 		[105, 238, 14],
    # 		[239, 445, 15],
    # 		[447, 505, 14],
    # 		[507, 543, 13],
    # 	],
    # 	'roman_offset': [1, 11, 1],
    # },
    # {
    # 	'filename': 33,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 72, 11],
    # 		[73, 240, 12],
    # 		[241, 260, 13],
    # 		[261, 326, 14],
    # 		[329, 498, 13],
    # 	],
    # 	'roman_offset': [1, 11, 1],
    # },
    # {
    # 	'filename': 34,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[4, 34, 36],
    # 		[35, 80, 38],
    # 		[81, 140, 40],
    # 		[143, 318, 39],
    # 		[321, 403, 38],
    # 		[407, 408, 36],
    # 		[409, 504, 37],
    # 		[505, 530, 38],
    # 		[533, 629, 37],
    # 	],
    # 	'roman_offset': [1, 35, 4],
    # },
    # {
    # 	'filename': 35,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 118, 23],
    # 		[121, 272, 22],
    # 		[275, 300, 21],
    # 		[301, 532, 22],
    # 		[533, 556, 23],
    # 		[557, 579, 24],
    # 		[583, 711, 22],
    # 	],
    # 	'roman_offset': [1, 20, 4],
    # },
    # {
    # 	'filename': 36,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 16, 12],
    # 		[17, 54, 13],
    # 		[55, 74, 14],
    # 		[75, 91, 15],
    # 		[95, 390, 13],
    # 		[392, 532, 12],
    # 		[533, 772, 13],
    # 	],
    # 	'roman_offset': [1, 10, 3],
    # },
    # {
    # 	'filename': 37,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[3, 19, 17],
    # 		[23, 82, 15],
    # 		[83, 277, 16],
    # 		[281, 309, 14],
    # 		[313, 371, 12],
    # 		[375, 399, 10],
    # 		[403, 470, 8],
    # 		[473, 496, 7],
    # 	],
    # 	'roman_offset': [1, 15, 4],
    # },
    # {
    # 	'filename': 38,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 36, 11],
    # 		[39, 177, 10],
    # 		[181, 214, 8],
    # 		[215, 310, 9],
    # 		[311, 326, 10],
    # 		[327, 437, 11],
    # 		[441, 619, 9],
    # 	],
    # 	'roman_offset': [1, 11, 1],
    # },
    # {
    # 	'filename': 39,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 205, 43],
    # 		[209, 222, 41],
    # 		[225, 259, 40],
    # 	],
    # 	'roman_offset': [1, 40, 4],
    # },
    # {
    # 	'filename': 40,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 6, 3],
    # 		[8, 66, 2],
    # 		[69, 435, 1],
    # 		[438, 468, -1],
    # 		[471, 542, -2],
    # 	],
    # },
    # {
    # 	'filename': 41,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 9, 3],
    # 		[11, 610, 2],
    # 	],
    # },
    # {
    # 	'filename': 42,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[6, 393, 2],
    # 		[396, 553, 0],
    # 		[557, 717, -2],
    # 	],
    # 	'roman_offset': [1, 11, 1],
    # },
    # {
    # 	'filename': 43,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[2, 32, 13],
    # 		[33, 240, 14],
    # 		[241, 361, 15],
    # 		[363, 374, 14],
    # 	],
    # 	'roman_offset': [1, 11, 3],
    # },
    # {
    # 	'filename': 44,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 78, 10],
    # 		[79, 256, 11],
    # 		[257, 390, 12],
    # 		[392, 460, 11],
    # 		[462, 485, 10],
    # 		[487, 499, 9],
    # 	],
    # 	'roman_offset': [1, 9, 1],
    # },
    # {
    # 	'filename': 45,
    # 	'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
    # 	# 'page_scan_offset': 33,
    # 	# [from, to, offset]
    # 	'page_scan_offset': [
    # 		[1, 10, 4],
    # 		[12, 496, 3],
    # 		[499, 517, 2],
    # 		[521, 603, 0],
    # 	],
    # },
    {
        'filename': 46,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 34, 22],
            [35, 88, 23],
            [89, 242, 24],
            [245, 294, 23],
            [296, 513, 22],
            [515, 590, 21],
        ],
        'roman_offset': [3, 21, 1],
    },
    {
        'filename': 47,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 60, 12],
            [61, 176, 13],
            [177, 222, 17],
            [225, 621, 16],
        ],
        'roman_offset': [1, 11, 11],
    },
    {
        'filename': 48,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 369, 30],
            [372, 539, 28],
        ],
        'roman_offset': [1, 27, 3],
    },
    {
        'filename': 49,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 21, 3],
            [25, 124, 1],
            [125, 131, 2],
            [135, 157, 0],
            [161, 310, -2],
        ],
    },
    {
        'filename': 50,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 196, 23],
            [199, 227, 22],
            [230, 517, 20],
            [521, 352, 0],
        ],
        'roman_offset': [1, 20, 3],
    },
    {
        'filename': 51,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 116, 2],
            [119, 160, 1],
            [161, 249, 0],
            [250, 292, 1],
        ],
    },
    {
        'filename': 52,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 44, 27],
            [45, 159, 28],
            [163, 277, 26],
            [281, 428, 24],
        ],
        'roman_offset': [1, 24, 3],
    },
    {
        'filename': 53,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [2, 235, 38],
            [239, 388, 36],
            [391, 563, 35],
        ],
        'roman_offset': [1, 36, 3],
    },
    {
        'filename': 54,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 56, 16],
            [57, 204, 17],
            [205, 208, 18],
            [210, 320, 17],
            [321, 343, 18],
            [346, 392, 16],
            [393, 476, 18],
            [477, 753, 19],
        ],
        'roman_offset': [1, 15, 1],
    },
    {
        'filename': 55,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 178, 13],
            [179, 216, 14],
            [217, 396, 15],
            [399, 636, 14],
        ],
        'roman_offset': [1, 12, 1],
    },
    {
        'filename': 56,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 88, 15],
            [89, 174, 16],
            [177, 276, 15],
            [277, 383, 16],
            [387, 663, 14],
        ],
        'roman_offset': [1, 13, 2],
    },
    {
        'filename': 57,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 16, 27],
            [17, 196, 28],
            [199, 267, 27],
            [271, 430, 25],
        ],
        'roman_offset': [1, 24, 3],
    },
    {
        'filename': 58,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 126, 15],
            [128, 176, 14],
            [177, 224, 18],
            [225, 235, 19],
            [238, 272, 17],
            [273, 416, 18],
            [417, 625, 19],
            [626, 674, 18],
        ],
        'roman_offset': [1, 15, 1],
    },
    {
        'filename': 59,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [2, 10, 15],
            [5, 389, 16],
        ],
        'roman_offset': [1, 15, 2],
    },
    {
        'filename': 60,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 47, 4],
            [49, 84, 3],
            [85, 560, 5],
        ],
    },
    {
        'filename': 61,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [2, 136, 10],
            [137, 152, 11],
            [153, 162, 12],
            [163, 423, 13],
        ],
        'roman_offset': [1, 8, 3],
    },
    {
        'filename': 62,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [2, 16, 10],
            [17, 575, 12],
        ],
        'roman_offset': [1, 8, 3],
    },
    {
        'filename': 63,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 54, 14],
            [55, 240, 15],
            [241, 525, 16],
        ],
        'roman_offset': [1, 13, 1],
    },
    {
        'filename': 64,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 80, 23],
            [81, 116, 24],
            [117, 240, 25],
            [241, 398, 27],
        ],
        'roman_offset': [1, 20, 3],
    },
    {
        'filename': 65,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [2, 200, 30],
            [201, 365, 32],
            [367, 376, 31],
        ],
        'roman_offset': [1, 27, 4],
    },
    {
        'filename': 66,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 9, 3],
            [11, 204, 2],
            [205, 256, 4],
            [257, 530, 5],
        ],
    },
    {
        'filename': 67,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 340, 47],
        ],
        'roman_offset': [1, 47, 4],
    },
    {
        'filename': 68,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 9, 3],
            [11, 305, 2],
        ],
    },
    {
        'filename': 69,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 8, 0],
            [11, 270, -2],
        ],
    },
    {
        'filename': 70,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 8, 4],
            [11, 122, 2],
            [123, 240, 5],
        ],
    },
    {
        'filename': 71,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [241, 248, -236],
            [251, 334, -238],
            [335, 571, -237],
        ],
    },
    {
        'filename': 72,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 144, 13],
            [145, 340, 14],
            [341, 633, 17],
        ],
        'roman_offset': [1, 12, 1],
    },
    {
        'filename': 73,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [2, 70, 43],
            [71, 192, 44],
            [193, 206, 45],
            [207, 377, 46],
            [379, 387, 45],
        ],
        'roman_offset': [1, 40, 4],
    },
    {
        'filename': 74,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 3, 7],
            [5, 330, 6],
        ],
    },
    {
        'filename': 75,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [2, 287, 35],
        ],
        'roman_offset': [1, 32, 4],
    },
    {
        'filename': 76,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 361, 10],
        ],
        'roman_offset': [1, 7, 3],
    },
    {
        'filename': 77,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 3, 36],
            [5, 232, 35],
            [233, 248, 36],
            [249, 339, 37],
        ],
        'roman_offset': [1, 32, 4],
    },
    {
        'filename': 78,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 7, 4],
            [9, 458, 3],
        ],
    },
    {
        'filename': 79,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 303, 3],
        ],
    },
    {
        'filename': 80,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 365, 11],
            [367, 376, 10],
        ],
        'roman_offset': [1, 7, 4],
    },
    {
        'filename': 81,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 9, 3],
            [11, 186, 2],
            [187, 309, 6],
            [311, 317, 5],
        ],
    },
    {
        'filename': 82,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 7, 4],
            [9, 220, 3],
            [221, 329, 5],
            [331, 338, 4],
        ],
    },
    {
        'filename': 83,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 638, 13],
        ],
        'roman_offset': [1, 12, 1],
    },
    {
        'filename': 84,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 13, 3],
            [15, 447, 2],
        ],
    },
    {
        'filename': 85,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 16, 13],
            [17, 120, 14],
            [121, 465, 15],
        ],
        'roman_offset': [1, 12, 1],
    },
    {
        'filename': 86,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [2, 62, 14],
            [63, 216, 15],
            [217, 318, 16],
        ],
        'roman_offset': [1, 13, 2],
    },
    {
        'filename': 87,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 54, 15],
            [55, 422, 16],
        ],
        'roman_offset': [1, 14, 1],
    },
    {
        'filename': 88,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 353, 38],
        ],
        'roman_offset': [1, 35, 3],
    },
    {
        'filename': 89,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 235, 3],
            [236, 246, 4],
            [248, 269, 3],
            [271, 276, 2],
        ],
    },
    {
        'filename': 90,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 8, 3],
            [11, 14, 2],
            [17, 89, 1],
            [93, 150, -1],
            [152, 173, -2],
            [179, 184, -5],
            [185, 218, -4],
            [223, 348, -6],
            [349, 352, -5],
            [354, 478, -6],
        ],
    },
    {
        'filename': 91,
        'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
        'page_scan_offset': [
            [1, 34, 2],
            [37, 111, 1],
            [115, 648, -1],
            [651, 669, -2],
        ],
    },
]

volumes = [
    # {
    # 	'index': 'Deutsches Reichsgesetzblatt 1918 077 0',
    # 	'page_scan_offset': 0,
    # 	'wordlist': [
    # 		['Reichsgesetzblatt (1918)/черновик таблиц', 537, 'таблица'],
    #
    # 	],
    # },

    # {
    # 'index': 'Сочинения Платона (Платон, Карпов). Том 1, 1863.pdf:ВТ',
    # 'page_scan_offset': 33,
    # 'wordlist': [
    # # ['Предисловие (к первому изданию) (Карпов)', -27, 'Предисловие-1'],
    # # ['Предисловие (ко второму изданию) (Карпов)', -9, 'Предисловие-2'],
    # # # ['Жизнь Платона (Карпов)', 1, 'Жизнь Платона'],
    # # # ['О сочинениях Платона (Карпов)', 15, 'О сочинениях Платона'],
    # # # ['Протагор. Введение (Карпов)', 43, 'Протагор. Введение'],
    # # # ['Протагор (Платон/Карпов)', 51, 'Протагор'],
    # # # ['Эвтидем. Введение (Карпов)', 133, 'Эвтидем. Введение'],
    # # # ['Эвтидем (Платон/Карпов)', 163, 'Эвтидем'],
    # # # ['Лахес. Введение (Карпов)', 219, 'Лахес. Введение'],
    # # # ['Лахес (Платон/Карпов)', 227, 'Лахес'],
    # # # ['Хармид. Введение (Карпов)', 263, 'Хармид. Введение'],
    # # # ['Хармид (Платон/Карпов)', 277, 'Хармид'],
    # # # ['Иппиас меньший. Введение (Карпов)', 313, 'Иппиас меньший. Введение'],
    # # # ['Иппиас Меньший (Платон/Карпов)', 321, 'Иппиас Меньший'],
    # # # ['Эвтифрон. Введение (Карпов)', 345, 'Эвтифрон. Введение'],
    # # # ['Эвтифрон (Платон/Карпов)', 355, 'Эвтифрон'],
    # # # ['Апология Сократа. Введение (Карпов)', 385, 'Апология Сократа. Введение'],
    # # # ['Апология Сократа (Платон/Карпов)', 404, 'Апология Сократа'],
    # # # ['Историко-филологический указатель к 1-й части соч. Платона.', 444, 'указатель-1'],
    # # ['', 449, 'Опечатки-1'],
    # ],
    # },
    # {
    # 'index': 'Сочинения Платона (Платон, Карпов). Том 2, 1863.pdf:ВТ',
    # 'page_scan_offset': 1,
    # 'wordlist': [
    # # # ['Критон. Введение (Карпов)', 7, 'Критон. Введение'],
    # # # ['Критон (Платон/Карпов)', 14, 'Критон'],
    # # # ['Федон. Введение (Карпов)', 37, 'Федон. Введение'],
    # # # ['Федон (Платон/Карпов)', 59, 'Федон'],
    # # # ['Менон. Введение (Карпов)', 147, 'Менон. Введение'],
    # # # ['Менон (Платон/Карпов)', 156, 'Менон'],
    # # # ['Горгиас. Введение (Карпов)', 211, 'Горгиас. Введение'],
    # # # ['Горгиас (Платон/Карпов)', 236, 'Горгиас'],
    # # # ['Алкивиад Первый. Введение (Карпов)', 369, 'Алкивиад Первый. Введение'],
    # # # ['Алкивиад Первый (Платон/Карпов)', 385, 'Алкивиад Первый'],
    # # # ['Алкивиад Второй. Введение (Карпов)', 453, 'Алкивиад Второй. Введение'],
    # # # ['Алкивиад Второй (Платон/Карпов)', 459, 'Алкивиад Второй'],
    # # # ['Историко-филологический указатель ко 2-й части соч. Платона.', 482, 'указатель-2'],
    # ],

    # },
    # {
    # 'index': 'Сочинения Платона (Платон, Карпов). Том 3, 1863.pdf:ВТ',
    # 'page_scan_offset': 5,
    # 'wordlist': [
    # # # # ['Политика или государство. Введение (Карпов)', 3, 'Политика или государство. Введение'],
    # # # ['Карпов В. Н., Содержание первой книги', 49, 'Содержание первой книги'],
    # # # ['Политика или государство. Книга первая (Платон/Карпов)', 51, 'Книга первая'],
    # # # ['Карпов В. Н., Содержание второй книги', 93, 'Содержание второй книги'],
    # # # ['Политика или государство. Книга вторая (Платон/Карпов)', 96, 'Книга вторая'],
    # # # ['Карпов В. Н., Содержание третьей книги', 139, 'Содержание третьей книги'],
    # # # ['Политика или государство. Книга третья (Платон/Карпов)', 145, 'Книга третья'],
    # # # ['Карпов В. Н., Содержание четвертой книги', 197, 'Содержание четвертой книги'],
    # # # ['Политика или государство. Книга четвертая (Платон/Карпов)', 204, 'Книга четвертая'],
    # # # ['Карпов В. Н., Содержание пятой книги', 244, 'Содержание пятой книги'],
    # # # ['Политика или государство. Книга пятая (Платон/Карпов)', 249, 'Книга пятая'],
    # # # ['Карпов В. Н., Содержание шестой книги', 295, 'Содержание шестой книги'],
    # # # ['Политика или государство. Книга шестая (Платон/Карпов)', 305, 'Книга шестая'],
    # # # ['Карпов В. Н., Содержание седьмой книги', 346, 'Содержание седьмой книги'],
    # # # ['Политика или государство. Книга седьмая (Платон/Карпов)', 354, 'Книга седьмая'],
    # # # ['Карпов В. Н., Содержание восьмой книги', 395, 'Содержание восьмой книги'],
    # # # ['Политика или государство. Книга восьмая (Платон/Карпов)', 398, 'Книга восьмая'],
    # # # ['Карпов В. Н., Содержание девятой книги', 439, 'Содержание девятой книги'],
    # # # ['Политика или государство. Книга девятая (Платон/Карпов)', 447, 'Книга девятая'],
    # # # ['Карпов В. Н., Содержание десятой книги', 479, 'Содержание десятой книги'],
    # # # ['Политика или государство. Книга десятая (Платон/Карпов)', 486, 'Книга десятая'],
    # # # ['Историко-филологический указатель к 3-й части соч. Платона', 526, 'указатель-3'],
    # ],
    # },
    # {
    # 'index': 'Сочинения Платона (Платон, Карпов). Том 4, 1863.pdf:ВТ',
    # 'page_scan_offset': 5,
    # 'wordlist': [
    # # # # ['Федр. Введение (Карпов)', 3, 'Федр. Введение'],
    # # # ['Федр (Платон/Карпов)', 17, 'Федр'],
    # # # # ['Пир. Введение (Карпов)', 119, 'Пир. Введение'],
    # # # ['Пир (Платон/Карпов)', 144, 'Пир'],
    # # # # ['Лизис. Введение (Карпов)', 227, 'Лизис. Введение'],
    # # # ['Лизис (Платон/Карпов)', 237, 'Лизис'],
    # # # # ['Иппиас Больший. Введение (Карпов)', 267, 'Иппиас Больший. Введение'],
    # # # ['Иппиас Больший (Платон/Карпов)', 278, 'Иппиас Больший'],
    # # # # ['Менексен. Введение (Карпов)', 319, 'Менексен. Введение'],
    # # # ['Менексен (Платон/Карпов)', 328, 'Менексен'],
    # # # # ['Ион. Введение (Карпов)', 359, 'Ион. Введение'],
    # # # ['Ион (Платон/Карпов)', 366, 'Ион'],
    # # # # ['Феаг. Введение (Карпов)', 389, 'Феаг. Введение'],
    # # # ['Феаг (Платон/Карпов)', 398, 'Феаг'],
    # # # # ['Соперники. Введение (Карпов)', 419, 'Соперники. Введение'],
    # # # ['Соперники (Платон/Карпов)', 422, 'Соперники'],
    # # # # ['Иппарх. Введение (Карпов)', 437, 'Иппарх. Введение'],
    # # # ['Иппарх (Платон/Карпов)', 439, 'Иппарх'],
    # # # # ['Клитофон. Введение (Карпов)', 455, 'Клитофон. Введение'],
    # # # ['Клитофон (Платон/Карпов)', 457, 'Клитофон'],
    # # # ['Историко-филологический указатель к 4-й части соч. Платона', 464, 'указатель-4'],
    # ],
    # },
    # {
    # 'index': 'Сочинения Платона (Платон, Карпов). Том 5, 1879.pdf:ВТ',
    # 'page_scan_offset': 7,
    # 'wordlist': [
    # # # ['Филеб. Введение (Карпов)', 3, 'Филеб. Введение'],
    # # # ['Филеб (Платон/Карпов)', 49, 'Филеб'],
    # # # ['Кратил. Введение (Карпов)', 169, 'Кратил. Введение'],
    # # # ['Кратил (Платон/Карпов)', 198, 'Кратил'],
    # # # ['Теэтет. Введение (Карпов)', 289, 'Теэтет. Введение'],
    # # # ['Теэтет (Платон/Карпов)', 320, 'Теэтет'],
    # # # ['Софист. Введение (Карпов)', 441, 'Софист. Введение'],
    # # # ['Софист (Платон/Карпов)', 479, 'Софист'],
    # ],
    # },
    # {
    # 'index': 'Сочинения Платона (Платон, Карпов). Том 6, 1879.pdf:ВТ',
    # 'page_scan_offset': 5,
    # 'wordlist': [
    # # # ['Политик. Введение (Карпов)', 3, 'Политик. Введение'],
    # # # ['Политик (Платон/Карпов)', 66, 'Политик'],
    # # # ['Парменид. Введение (Карпов)', 161, 'Парменид. Введение'],
    # # # ['Парменид (Платон/Карпов)', 244, 'Парменид'],
    # # ['Тимей. Введение (Карпов)', 329, 'Тимей. Введение'],
    # # # ['Тимей (Платон/Карпов)', 371, 'Тимей'],
    # # # ['Критиас. Введение (Карпов)', 491, 'Критиас. Введение'],
    # # # ['Критиас (Платон/Карпов)', 497, 'Критиас'],
    # # # ['Минос. Введение (Карпов)', 523, 'Минос. Введение'],
    # # # ['Минос (Платон/Карпов)', 537, 'Минос'],
    # # # ['Несколько слов об Эриксиасе (Карпов)', 557, 'Эриксиас. Введение'],
    # # # ['Эриксиас (Псевдо-Платон/Карпов)', 559, 'Эриксиас'],
    # ],
    # },
]

# macros_pwb_post = """\
# {{-stop-}}
# {{-start-}}
# '''%s/%s'''
# """

macros_pwb_post = """\
{{-start-}}
'''%s/%s'''
%s
{{-stop-}}
"""


def pagenum_to_scanpagenum(pagenum, offset):
    scanpagenum = str(int(pagenum) + offset)
    return scanpagenum


if __name__ == '__main__':

    bookpagenum_re_text = r'^id="(.+?)".*?/pagenumber>\s*'
    bookpagenum_re = re.compile(bookpagenum_re_text)

    for v in volumes_from_file:
        # if len(v['wordlist']) == 0: continue
        page_scan_offset = v['page_scan_offset']
        index = v['index']
        volume_num = v['filename']

        volume_text_pages = []

        volume_text_to_post_pwb = []

        # subpagename = page[0]
        # page_pn = page[1]
        # section_name = page[2] if page[2] else subpagename

        file_path = path + str(v['filename']) + '.parsed' + '.html'
        text_source = file_readtext(file_path)
        text = text_source

        # text = re.sub('<span class="opdelimiter">([^<>]*)</span>', r'\1', text)

        # for page in v['wordlist']:

        text = re.sub('pagenumber[^>]+id=', 'pagenumber id=', text)

        for i, textpage in enumerate(text.split('<pagenumber ')):
            if i == 0:
                # book_pn = 'I'
                p = {'numbookpage': 0, 'numindexpage': 1, 'colontitul': ''}
            else:
                try:
                    book_pn = bookpagenum_re.match(textpage).group(1)
                except:
                    pass

                subpagename = ''
                if re.match('^\d+$', book_pn):
                    # offset_pn_from, offset_pn_to, page_scan_offset, scan_pn = offset[0], offset[1], offset[2], 0
                    # if book_pn >= offset_pn_from and book_pn <= offset_pn_to:
                    # 	scan_pn = pagenum_to_scanpagenum(book_pn, page_scan_offset)
                    book_pn = int(book_pn)
                    if book_pn in [i.get('numindexpage') for i in volume_text_pages]:
                        """ дубль страниц, ошибочный номер грозит перезаписью"""
                        pass
                    elif book_pn == 0:
                        pass
                    page_scan_offset, scan_pn = 0, 0
                    for offset in v['page_scan_offset']:
                        offset_pn_from, offset_pn_to, page_scan_offset = offset[0], offset[1], offset[2]
                        if book_pn >= offset_pn_from and book_pn <= offset_pn_to:
                            scan_pn = pagenum_to_scanpagenum(book_pn, page_scan_offset)
                            break
                    p = {'numbookpage': book_pn, 'numindexpage': scan_pn,
                         'colontitul': FormatText_to_WikiIndexPage.make_colontitul(book_pn, subpagename)}

                elif re.match('^[IVXCL]+$', book_pn, flags=re.IGNORECASE):
                    book_pn = int(roman.fromRoman(book_pn))
                    page_scan_offset, scan_pn = 0, 0
                    ro = v['roman_offset']
                    offset_pn_from, offset_pn_to, page_scan_offset = ro[0], ro[1], ro[2]
                    if book_pn >= offset_pn_from and book_pn <= offset_pn_to:
                        scan_pn = pagenum_to_scanpagenum(book_pn, page_scan_offset)
                    p = {'numbookpage': book_pn, 'numindexpage': scan_pn,
                         'colontitul': FormatText_to_WikiIndexPage.make_colontitul(roman.toRoman(book_pn), subpagename)}

            # try:
            # 	book_pn = int(bookpagenum_re.match(textpage).group(1))
            # except:
            # 	pass
            # else:

            textpage = re.sub(bookpagenum_re_text + r'\n+', r'\n\n', textpage)
            textpage = bookpagenum_re.sub('', textpage)
            p['text'] = textpage.strip(' ')
            volume_text_pages.append(p)
            pass

        # text = re.sub('<a href="#(.+?)".*? type="note">\[\d*\]</a>(.*?)',
        # 			  # <div class="section" id="\1">(.+?)</div>',
        # 			  r'<ref name="\1"></ref>\2',
        # 			  text)

        # page_pn = re.search(r'<a name="(\d+)"></a>', text).groups()
        # page_pn = re.sub('(<span class="opnumber">[\dVIXC]+</span>)', r'\1@@@', text)

        # page_pn = re.sub(r'<a name="(\d+)"></a>', """\
        # {{-stop-}}
        # {{-start-}}
        # '''%s/%s'''
        # """ % (index, r'\1' - 20), text)

        # scan_pn = page_pn + page_scan_offset

        # text = ''' '''
        # text = vladi_commons.file_readtext(r'e:\temp\СО- Нечистики._Свод_простонародных_в_Витебской_Белоруссии_сказаний_о_нечистой_силе_(1907).txt')
        # text = pywikibot.Page(site, book + subpagename).get()

        # pd = r'<!--[ \d]+-->'
        # pages_delimeter = '@@'
        # text = re.sub(pd, pages_delimeter, text)

        # text = re.sub(r'(\w+|\{\{акут\}\})' + pages_delimeter + r'(\w+)',
        # 			  r'{{перенос|\1|\2}}' + pages_delimeter + r'{{перенос2|\1|\2}}', text)
        # section_re = re.compile(pages_delimeter + r'(.*?)' + r'(?=' + pages_delimeter + r'|<!--\s*end\s*-->|$)',
        # 						re.DOTALL)

        # text = re.sub(r'\{\{Нечистая[^}]+\}\}', '', text)
        # text = re.sub(r'\[\[:?Категория:[^]]+\]\]', '', text)
        # text = re.sub(r'(\n*== *[LXIV.]+ *)(.*?)( *==\n)', r'\1<br><br>\2\3', text)  # <br> в заголовки с рим. цифрами
        # text = re.sub(r'\n*== *([LXIV.]+) *([^=]+) *==\n', r'<center><big><big>\1<br><br>\2</big></big></center>\n\n\n', text)  # <br> в заголовки с рим. цифрами
        # text = re.sub(r'(<section begin="[^"]+" */>)\n*(== *[LXIV.]+ *)(.*?)( *==\n)', r'\1\n\2<br><br>\3\4', text)  # <br> в заголовки с рим. цифрами

        # text = re.sub(r'(?<!==)\n(?!==)', '##BR##', text)  # \n → ##BR## под формат AWB

        # text = re.sub(r'\b([Ее])е\b',  r'\1ё', text)  # ёфикация
        # text = re.sub(r'\b([Дд])ает',  r'\1аёт', text)  # ёфикация
        # text = re.sub(r'\b([Нн])ем\b', r'\1ём', text)  # ёфикация
        # text = re.sub(r'\b([Ее])ще\b', r'\1щё', text)  # ёфикация

        # p = section_re.findall(text)

        # p = [t.value() for t in volume_text_pages]

        # for section_text in p:
        for t in volume_text_pages:
            section_text, book_pn, scan_pn, colontitul = t['text'], t['numbookpage'], t['numindexpage'], t['colontitul']

            # scan_page_name = 'Страница:' + index + str(scan_pn) + '.jpg'

            scan_page_name = 'Страница:' + index + '/' + str(scan_pn)
            # scan_page = pywikibot.Page(site, scan_page_name)
            subpagename = ''

            scanpagetext = FormatText_to_WikiIndexPage.make_pagetext(section_text, subpagename, colontitul, header='',
                                                                     footer='', colontitul_up=False)

            # scan_page.text = scanpagetext
            # csvrows.append([scan_page_name, str(page_pn), subpagename, section_name, colontitul, section_text])
            # scan_pn += 2
            # page_pn += 2
            # pass

            textpage_topost = macros_pwb_post % ('Страница:' + index % volume_num, str(scan_pn), scanpagetext)
            volume_text_to_post_pwb.append(textpage_topost)

        file_savetext(path + 'topost/' + str(v['filename']) + '.parsed.txt',
                      '\n'.join(volume_text_to_post_pwb))
        pass
    # import csv
    #
    # b = open(text2upload, 'w', encoding='utf-8', newline='')
    # csvfile = csv.writer(b)
    # csvfile.writerows(csvrows)
    # b.close()
    # pass

    # exclude_namespaces = r'\[\[(?:Special|Служебная|Участник|User|У|Обсуждение[ _]участника|ОУ|Википедия|ВП|Обсуждение[ _]Википедии|Обсуждение):'
    #
    # # тэги li
    # for string in re.findall(r'^[*#](.*)$', text, re.MULTILINE):
    # 	check_links(string)
    #
    # # заголовки
    # for string in re.findall(r'^==+([^=]+)==+$', text, re.MULTILINE):
    # 	check_links(string)
    #
    # # Парсинг
    #
    # wikicode2 = mwparserfromhell.parse(text_original)

    # article_page.text = str(remove_parameters(wikicode1, var_template, 1))
    # scan_page.text = str(remove_parameters(wikicode2, var_template, 2))

    # Запись страниц
    # vladi_commons.file_savetext(wikipages_filename, text)

    # scan_page.text = text
    # edit_comment = ''
    # scan_page.save(edit_comment)
