#!/usr/bin/env python3
# coding: utf-8
import requests
from urllib.parse import quote
from lxml import etree
import re
# import mwparserfromhell
import pywikibot
import vladi_commons

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
		header = '''<noinclude><pagequality level="1" user="TextworkerBot" /><div class="pagetext">			__NOEDITSECTION__<div class="oldspell"><div style="text-align:justify">{{колонтитул||%s|}}<div class="indent"></noinclude><section begin="%s" />''' % (colontitul, sectionname)
	if footer == '':
		footer = '<section end="%s" /><noinclude><references /></div></div></div></div></noinclude>'
	# {{свр}}
	scanpagetext = header + text + footer
	return scanpagetext


def label_interpages(number, string_chet, str_nechet):
	# возвращает строку в зависимости чётная ли страница
	return string_chet if not number % 2 else str_nechet 
	

site = pywikibot.Site('ru', 'wikisource')
book = 'Пословицы русского народа (Даль)'
index = 'Нечистики. Свод простонародных в Витебской Белоруссии сказаний о нечистой силе (1907).pdf:ВП'  # без префикса "Индекс:"

wordlist = [
	['Нечистики', 1],
	# ['Общее о нечистиках', 10],
	# ['Люцыпыр', 10],
	# ['Пекельники', 36],
	# ['Шешники', 37],
	# ['Касны', 38],
	# ['Шатаны', 39],
	# ['Цмоки', 40],
	# ['Паралики', 41],
	# ['Поветрики', 42],
	# ['Прахи', 43],
	# ['Кадуки', 44],
	# ['Домовые', 48],
	# ['Хлевники', 53],
	# ['Гуменники, пунники и банники', 57],
	# ['Полуночники и еретники', 61],
	# ['Маты', 63],
	# ['Кикиморы', 64],
	# ['Полевики', 66],
	# ['Лешии', 68],
	# ['Кладники', 73],
	# ['Водяники', 75],
	# ['Болотники', 80],
	# ['Русалки', 85],
	# ['Ведьмаки и ведьмы', 90],
	# ['Колдуны и колдуньи', 96],
	# ['Оборотни', 100],
]
page_scan_offset = 2

for article in wordlist:
	subpagename = article[0]
	page_pn = article[1]

	scan_pn = page_pn + page_scan_offset

	# text = ''' '''
	text = vladi_commons.file_readtext(r'e:\temp\СО- Нечистики._Свод_простонародных_в_Витебской_Белоруссии_сказаний_о_нечистой_силе_(1907).txt')
	# text = pywikibot.Page(site, book + '/' + subpagename).get()

	pages_delimeter = r'<!--[ \d]+-->'
	pd = '@@'
	text = re.sub(pages_delimeter, pd, text)
	pages_delimeter = pd

	text = re.sub(r'(\w+|\{\{акут\}\})' + pages_delimeter + r'(\w+)',
				  r'{{перенос|\1|\2}}' + pages_delimeter + r'{{перенос2|\1|\2}}', text)
	text = re.sub(r'\{\{Нечистая[^}]+\}\}', '', text)
	text = re.sub(r'\[\[:?Категория:[^]]+\]\]', '', text)
	section_re = re.compile(pages_delimeter + r'(.*?)' + r'(?=' + pages_delimeter + r'|<!--\s*end\s*-->|$)', re.DOTALL)
	# text = re.sub(r'(\n*== *[LXIV.]+ *)(.*?)( *==\n)', r'\1<br><br>\2\3', text)  # <br> в заголовки с рим. цифрами
	# text = re.sub(r'\n*== *([LXIV.]+) *([^=]+) *==\n', r'<center><big><big>\1<br><br>\2</big></big></center>\n\n\n', text)  # <br> в заголовки с рим. цифрами
	# text = re.sub(r'(<section begin="[^"]+" */>)\n*(== *[LXIV.]+ *)(.*?)( *==\n)', r'\1\n\2<br><br>\3\4', text)  # <br> в заголовки с рим. цифрами
	text = re.sub(r'(?<!==)\n(?!==)', '##BR##', text)  # \n → ##BR## под формат AWB

	text = re.sub(r'\b([Ее])е\b',  r'\1ё', text)  # ёфикация
	text = re.sub(r'\b([Дд])ает',  r'\1аёт', text)  # ёфикация
	text = re.sub(r'\b([Нн])ем\b', r'\1ём', text)  # ёфикация
	text = re.sub(r'\b([Ее])ще\b', r'\1щё', text)  # ёфикация

	p = section_re.findall(text)

	for section_text in p:
		scan_page_name = 'Страница:' + index + '/' + str(scan_pn)
		# scan_page = pywikibot.Page(site, scan_page_name)

		# colontitul = 'Народная Русь' if not scan_pn % 2 else subpagename  # чередующийся на чётных/нечётных страницах
		# colontitul = (colontitul + '.').upper()  # в верхнем регистре с точкой
		# colontitul = str(page_pn)  # колонтитул — номер страницы
				# чередующийся на чётных/нечётных страницах				
		colontitul = [
			# label_interpages(page_pn, str(page_pn), ''),			
			# (subpagename + '.').upper(),
			# label_interpages(page_pn, '', str(page_pn))
			'',
			'— ' + str(page_pn) + ' —',
			''
		]
		colontitul = '{{колонтитул|' + '|'.join(colontitul) + '}}'
		
		scanpagetext = make_pagetext(section_text, subpagename, colontitul, header='', footer='')

		# scan_page.text = scanpagetext
		csvrows.append([scan_page_name, str(page_pn), subpagename, colontitul, section_text])
		scan_pn += 1
		page_pn += 1
		pass

import csv
b = open('test.csv', 'w', encoding='utf-8', newline='')
csvfile = csv.writer(b)
csvfile.writerows(csvrows)
b.close()
pass
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
