#!/usr/bin/env python3
# coding: utf8
#
# author: https://github.com/vladiscripts
#
import re
import mwparserfromhell
import pywikibot
import vladi_commons

listpages_filename = 'listpages.txt'  # список страниц для обработки
var_template = ('ВАР', 'ВАР2')


def pagetitle_target(title):
	""" Форматер названия второй страницы """
	# Строка ниже создаёт:
	# 'Страница:Lobachevsky (Syn otechestva).djvu/3' → 'Страница:Lobachevsky (Syn otechestva).djvu:ВТ/3'
	# 'Страница:Lobachevsky (Syn otechestva).djvu' → 'Страница:Lobachevsky (Syn otechestva).djvu:ВТ'
	addon = ':ВТ'
	npages = r'(/\d+)$'
	if re.search(npages, title):
		title_new = re.sub(npages, addon + r'\1', title)
	else:
		title_new = title + addon
	return title_new


def file_readlines_in_list(filename):
	from sys import version_info
	PYTHON_VERSION = version_info.major
	if PYTHON_VERSION == 3:
		f = open(filename, encoding='utf-8')
	else:
		import codecs
		f = codecs.open(filename, 'r', encoding='utf-8')
	arr_strings = f.read().splitlines()
	f.close()
	# чистка пустых строк
	for v in arr_strings:
		if v.isspace() or v == '':
			arr_strings.remove(v)
	return arr_strings


def file_readlines_in_set(filename):
	arr_strings = set(file_readlines_in_list(filename))
	return arr_strings


def remove_parameters(wikicode, tpl_name, param_name):
	for tpl in wikicode.filter_templates():
		if tpl.name.matches(tpl_name):
			param = tpl.get(param_name).value if tpl.has(param_name) else ''
			wikicode.replace(tpl, str(param))
			pass
	return wikicode


FI = '/home/vladislav/workspace/bse1.txt'

SITE = pywikibot.Site('ru', 'wikisource')
wikipage = vladi_commons.file_readtext(FI)

list_ = [
'Аномит',
'Александры земля',
'Аллеломорфизм ложный',
'Алунд',
'Альдоль',
'Аноплоцефалиды',
'Альпака, посеребренный мельхиор',
'Альбиносы',
'Анормальные дети',
'Александр Север',
'Альбирео',
'Анонимное общество',
'Альбский ярус',
'Аналогия Непера',
'Анортит',
'Амурская железная дорога',
'Андрогинофор',
'Алкоран',
'Американские фильтры',
'Аналитическая функция',
'Александра Вюртембергского, герцога, канал',
'Александрийское семя',
'Анормальный',
'Александр Обренович',
'Амурский край',
'Американская педагогика',
'Анизокория',
'Американская форма бухгалтерии',
'Ангорская коза',
'Альпийская складчатость',
'Английская педагогика',
'Альпака, вид животных',
'Амфибластула',
'Альпийская роза',
'Алкоголаза',
'Александр Карагеоргиевич',
'Альпийские общества',
'Аллен, химическое вещество',
'Альдегидаза',
'Александр I, болгарский князь',
'Александра I канал',
'Алексин, имунное тело',
'Аналитическая механика',
'Анималькулисты',
'Аналитическая химия',
'Альбит',
'Андийские языки',
'Аномалистический месяц',
'Альпийская куропатка',
'Альголь',
'Александра III канал',
'Алеппский прыщ',
'Аллантоин',
'Аннулирование государственных долгов',
'Al pari',
'Альтерновые слои',
'Альпакс',
'Анортоклаз',
'Аллилен',
'Александра II канал',
'Алинда',
'Александровский централ',
'Амфибол',
]


def all_sections(wikipage):
	sections_re = re.compile(r'''
		((?:\n|^)={2,}\s*(.*?)\s*={2,}\n[\n\s]*	# заголовок
		(.*?))		# текст секции
		(?=\n==|$)	# конец секции или страницы; пропускает из выборки след.секции
		# (?<=\n==|$)
		''', flags=re.DOTALL | re.VERBOSE)
	return sections_re.findall(wikipage)


already_exists_pages = set()
textovka_title = 'Обсуждение:Большая советская энциклопедия/для заливки/том 2'
textovka = pywikibot.Page(SITE, textovka_title)
textovka_text = textovka.get()
for section in all_sections(wikipage):
	header = section[1]
	text = section[2]
	header_and_text = section[0]
	if header in list_:
		# очистка текстовки от залитых статей
		wikipage = wikipage.replace(header_and_text, '')
		textovka.text = textovka_text.replace(header_and_text, '')
		pass

# textovka.save('залито')
FO = FI + ' new'
vladi_commons.file_savetext(FO, wikipage)
# vladi_commons.file_savelines('already_exists_pages.log', already_exists_pages)
