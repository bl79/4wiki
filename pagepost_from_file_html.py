#!/usr/bin/env python3
# coding: utf-8
import requests
from urllib.parse import quote
from lxml import etree
from lxml.html import fromstring, tostring
from lxml import cssselect
import re
# import mwparserfromhell
# import pywikibot
import vladi_commons

text2upload = 'pages_to_bot_upload.csv'
csvrows = []


#
# <noinclude><pagequality level="1" user="TextworkerBot" /><div class="pagetext"><div class="oldspell"><div style="text-align:justify">{{колонтитул||##colontitul##|}}<div class="indent">__NOEDITSECTION__</noinclude>
# <section begin="##subpagename##" />##section_text##<section end="##subpagename##" /><noinclude><references /></div></div></div></div></noinclude>


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
		vladi_commons.file_savetext(wikipages_filename, text)


# article_page = openwikipage(project, book, subpagename)

def make_pagetext(text, sectionname='', colontitul='', header='', footer=''):
	if header == '':
		header = '''<noinclude><pagequality level="1" user="TextworkerBot" /><div class="pagetext">			__NOEDITSECTION__<div class="oldspell"><div style="text-align:justify">{{колонтитул||%s|}}<div class="indent"></noinclude><section begin="%s" />''' % (
			colontitul, sectionname)
	if footer == '':
		footer = '<section end="%s" /><noinclude><references /></div></div></div></div></noinclude>'
	# {{свр}}
	scanpagetext = header + text + footer
	return scanpagetext


def label_interpages(number, string_chet, str_nechet):
	# возвращает строку в зависимости чётная ли страница
	return string_chet if not number % 2 else str_nechet


# site = pywikibot.Site('ru', 'wikisource')
# book = 'Пословицы русского народа (Даль)' + '/'
book = ''
# index = 'Сочинения Платона (Платон, Карпов). Том 5, 1879.pdf:ВТ'  # без префикса "Индекс:"
# wordlist : имя викистраницы, стр. книги, имена секций


path = '/home/vladislav/var/tolstoy/html/parsed/'
volumes_from_file = [
	{
		'filename': 6,
		'index': 'L. N. Tolstoy. All in 90 volumes. Volume %s.pdf',
		# 'page_scan_offset': 33,
		# [from, to, offset]
		'page_scan_offset': [
			[1, 163, 12],
							],
		'wordlist': [
			['Предисловие (к первому изданию) (Карпов)', -27, 'Предисловие-1'],
			# ['Предисловие (к первому изданию) (Карпов)', -27, 'Предисловие-1'],
			# ['Предисловие (ко второму изданию) (Карпов)', -9, 'Предисловие-2'],
			# # ['Жизнь Платона (Карпов)', 1, 'Жизнь Платона'],
			# # ['О сочинениях Платона (Карпов)', 15, 'О сочинениях Платона'],
			# # ['Протагор. Введение (Карпов)', 43, 'Протагор. Введение'],
			# # ['Протагор (Платон/Карпов)', 51, 'Протагор'],
			# # ['Эвтидем. Введение (Карпов)', 133, 'Эвтидем. Введение'],
			# # ['Эвтидем (Платон/Карпов)', 163, 'Эвтидем'],
			# # ['Лахес. Введение (Карпов)', 219, 'Лахес. Введение'],
			# # ['Лахес (Платон/Карпов)', 227, 'Лахес'],
			# # ['Хармид. Введение (Карпов)', 263, 'Хармид. Введение'],
			# # ['Хармид (Платон/Карпов)', 277, 'Хармид'],
			# # ['Иппиас меньший. Введение (Карпов)', 313, 'Иппиас меньший. Введение'],
			# # ['Иппиас Меньший (Платон/Карпов)', 321, 'Иппиас Меньший'],
			# # ['Эвтифрон. Введение (Карпов)', 345, 'Эвтифрон. Введение'],
			# # ['Эвтифрон (Платон/Карпов)', 355, 'Эвтифрон'],
			# # ['Апология Сократа. Введение (Карпов)', 385, 'Апология Сократа. Введение'],
			# # ['Апология Сократа (Платон/Карпов)', 404, 'Апология Сократа'],
			# # ['Историко-филологический указатель к 1-й части соч. Платона.', 444, 'указатель-1'],
			# ['', 449, 'Опечатки-1'],
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

macros_pwb_post = """\
{{-stop-}}
{{-start-}}
'''%s/%s'''
"""


def pagenum_to_scanpagenum(pagenum, offset):
	scanpagenum = str(int(pagenum) - offset)
	return scanpagenum

bookpagenum_re = re.compile(r'^id="(.+?)".*?/pagenumber>\s*')

for v in volumes_from_file:
	if len(v['wordlist']) == 0: continue
	page_scan_offset = v['page_scan_offset']
	index = v['index']

	volume_text_pages = []

	# for page in v['wordlist']:
	for offset in v['page_scan_offset']:
		# subpagename = page[0]
		# page_pn = page[1]
		# section_name = page[2] if page[2] else subpagename

		file_path = path + str(v['filename']) + '.parsed' + '.html'
		text_source = vladi_commons.file_readtext(file_path)
		text = text_source

		# text = re.sub('<span class="opdelimiter">([^<>]*)</span>', r'\1', text)

		for i, textpage in enumerate(text.split('<pagenumber ')):
			if i == 0:
				# book_pn = 'I'
				p = {'numbookpage': 0, 'numindexpage': 1}
			else:
				try:
					book_pn = int(bookpagenum_re.match(textpage).group(1))
				except:
					pass
				else:
					offset_pn_from,offset_pn_to, page_scan_offset, scan_pn  = offset[0],  offset[1], offset[2], 0
					if book_pn>= offset_pn_from and book_pn<= offset_pn_to:
						scan_pn = book_pn + page_scan_offset
					p = {'numbookpage': book_pn, 'numindexpage': scan_pn}
			textpage = bookpagenum_re.sub('', textpage)
			p['text'] = textpage
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


		# for section_text in p:
		for t in volume_text_pages:
			section_text, page_pn, scan_pn = t['text'], t['numbookpage'], t['numindexpage']


			# scan_page_name = 'Страница:' + index + str(scan_pn) + '.jpg'

			scan_page_name = 'Страница:' + index + '/' + str(scan_pn)
			# scan_page = pywikibot.Page(site, scan_page_name)

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
			colontitul_center = colontitul_center + '.'
			# colontitul_center = label_interpages(page_pn, (subpagename + '.').upper().replace(' ВВЕДЕНИЕ (КАРПОВ).', ''), '')
			# if colontitul_center == '':  colontitul_center = 'ВВЕДЕНІЕ.'
			import roman

			colontitul = [
				# label_interpages(page_pn, roman.toRoman(page_pn+32), ''),	 # римские цифры
				# # label_interpages(page_pn, str(page_pn), ''),
				# colontitul_center,
				# label_interpages(page_pn, '', roman.toRoman(page_pn+32))
				# label_interpages(page_pn, '', str(page_pn))
				'',
				'— ' + str(page_pn) + ' —',
				''
			]
			colontitul = '{{колонтитул|' + '|'.join(colontitul) + '}}'

			# на первых страницах без колонтитула
			if first_pages_without_colontitul and page_pn == page[1]:
				colontitul = ''

			scanpagetext = make_pagetext(section_text, subpagename, colontitul, header='', footer='')

			# scan_page.text = scanpagetext
			csvrows.append([scan_page_name, str(page_pn), subpagename, section_name, colontitul, section_text])
			scan_pn += 2
			page_pn += 2
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
