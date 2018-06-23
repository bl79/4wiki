#!/usr/bin/env python3
# coding: utf8
#
# author: https://github.com/vladiscripts
#
import re
import pywikibot
import vladi_commons.lib_for_mwparserfromhell
import vladi_commons.vladi_commons
from vladi_commons.vladi_commons import file_readlines
# import lib_for_mwparserfromhell
from unidecode import unidecode
from unicodedata import normalize
import mwparserfromhell as mwp

import copy

t = """
{{ТСД
|ВИКИПЕДИЯ=Багалярина
|ВИКИТЕКА=
|ВИКИСКЛАД=
|ВИКИСЛОВАРЬ=багалярина
|ВИКИЦИТАТНИК=
|ВИКИВИДЫ=
|ЭСБЕ=
|МЭСБЕ=
|НЕОДНОЗНАЧНОСТЬ=
}}
{{tom|2}}

<!--
{{tom|4|1}}
<pages index="Толковый словарь Даля (2-е издание). Том 1 (1880).pdf" from=125 to=125 onlysection="Багалярина1" />

-->

{{tom|3|1}}
<pages index="Толковый словарь. Том 1 (Даль 1903).djvu" from=62 to=62 onlysection="Багалярина1" />

<!--

{{tom|1|1}}
<pages index="Толковый словарь. Том 1 (Даль 1903).djvu" from=62 to=62 onlysection="Багалярина1" />

[[Категория:ТСД:uuu]]
-->

{{tom|1|1}}
<pages index="Толковый словарь. Том 1 (Даль 1864).djvu" from=62 to=62 onlysection="Багалярина1" />

[[Категория:ТСД:eee|*]]
[[Категория:ТСД:ttt]]
"""

t = """\
{{ТСД
|ВИКИПЕДИЯ=Агрофены
|ВИКИТЕКА=
|ВИКИСКЛАД=
|ВИКИСЛОВАРЬ=Агрофены
|ВИКИЦИТАТНИК=
|ВИКИВИДЫ=
|ЭСБЕ=
|МЭСБЕ=
|НЕОДНОЗНАЧНОСТЬ=
}}
{{tom|1|1|Аграфены-купальницы}}
{{tom|2|1|Аграфены-купальницы}}
{{tom|3|1}}
<pages index="Толковый словарь. Том 1 (Даль 1903).djvu" from=23 to=23 onlysection="Агрофены" />
[[Категория:ТСД:Существительные]]
[[Категория:ТСД:Календарные праздники]]

"""

t = """\
{{ТСД
|ВИКИПЕДИЯ=Федора
|ВИКИТЕКА=
|ВИКИСКЛАД=
|ВИКИСЛОВАРЬ=Федора
|ВИКИЦИТАТНИК=
|ВИКИВИДЫ=
|ЭСБЕ=
|МЭСБЕ=
|НЕОДНОЗНАЧНОСТЬ=
}}
{{tom|1}}
{{tom|2|}}
{{tom|3|4|}}
<pages index="Толковый словарь. Том 4 (Даль 1909).djvu" from=799 to=799 onlysection="Федора" />
{{примечания ВТ}}

[[Категория:ТСД:Праздники и даты]]

"""


def remove_parameters(wikicode, tpl_name, param_name):
	for tpl in wikicode.filter_templates():
		if tpl.name.matches(tpl_name):
			param = tpl.get(param_name).value if tpl.has(param_name) else ''
			wikicode.replace(tpl, str(param))
			pass
	return wikicode


def delete_tpl(wikicode, tplname):
	for tpl in wikicode.filter_templates():
		if tpl.name.matches(tplname):
			wikicode.remove(tpl)


def pop_tpl_categories():
	# categories = [c for c in mwp.parse(t).filter_wikilinks()]
	categories = []
	for wl in wikicode.filter_wikilinks():
		if str(wl.title).startswith('Категория:'):
			categories.append(str(wl))
			wikicode.remove(wl)
	return categories


def pop_tpl_header():
	tsd_tpl = ''
	for tpl in wikicode.filter_templates():
		if tpl.name.matches('ТСД'):
			tsd_tpl = tpl
			wikicode.remove(tpl)
	return tsd_tpl


# def makePage(num_izd, tsd_tpl, content, categories):
# 	if not tpl.has(2) or tpl.has(3):
# 		pass
# 	else:
# 		pass
# 	page_new = [num_izd, "%s\n%s\n\n%s" % (tsd_tpl, content, '\n'.join(categories))]
# 	return page_new


def section_processing(section, tpl_header, categories, articleTitle):
	# tpl_header = copy.deepcopy(tpl_header)
	tom_tpl = section[0]
	content = section[1]
	section_tpl_wikicode = mwp.parse(tom_tpl)
	for tpl in section_tpl_wikicode.filter_templates():
		if tpl.name.matches('tom'):
			num_izd = str(tpl.get(1).value).strip()
			# {{tom}} - без аналога в изданиях, без 2-го параметра или с 3-м
			tpls_noTerm = []
			# for tpl in wikicode.filter_templates():
			# 	if tpl.name.matches('tom'):
			if not tpl.has(2) or tpl.get(2).value == '' \
					or (tpl.has(3) and tpl.get(3).value != ''):
				# tpls_noTerm.append(tpl)
				# tpl_header.add(tpls_noTerm)
				tpl_header.add('-ТСД%s' % num_izd, '%s<!-- временный шаблон для бота -->' % str(tpl))
				return None

			title_ed = '%s%s/%s' % (PAGENAME_PREFIX, num_izd, articleTitle)
			# articleName = articleTitle.partition('/')[0]
			tpl_header.add('ТСД%s' % num_izd, articleTitle.partition('/')[0])
			# page_new = makePage(num_izd, title_ed, tpl_header, content, categories)
			page_new = [num_izd, title_ed, tpl_header, content]
			return page_new


def rename_to_num_edition(pageEditions, articleTitle):
	# приоритеты для переименования
	numEd = ''
	if '2' in pageEditions:
		numEd = '2'
	elif '3' in pageEditions:
		numEd = '3'
	elif '1' in pageEditions:
		numEd = '1'
	else:
		numEd = '0'
	title_new = '%s%s/%s' % (PAGENAME_PREFIX, numEd, articleTitle)
	return title_new


# def comments():
# 	for template in wikicode.filter_comments():
# 		if template.name.matches("Cleanup") and not template.has("date"):
# 			template.add("date", "July 2012")


def remove_comments():
	for comment in wikicode.filter_comments():
		wikicode.remove(comment)


commented_pages = re.compile(r"<!--\s*{{[Tt]om.+?}}\s*<pages.*?>\s*-->", flags=re.DOTALL)
"({{tom.+?}}.+?)(?!<!--)(?={{tom)"

"(?<!<!--\s*)({{tom.+?}}.+?)(?=<!--|{{tom|$)"

sections_re = re.compile(r'''
		(\{\{[Tt]om.+?\}\})	# заголовок
		\s*(.*?)\s*(?:<br[\s/]*>)*\s*	# текст секции
		(?=\{\{[Tt]om|$)			# конец секции или страницы
		''', flags=re.DOTALL | re.VERBOSE)
# self.all_sections += [sections_re.findall(t) for t in self.textovki_texts]
# sections_re = re.compile(r"(\{\{[Tt]om.+?\}\})\s*(.*?)\s*(?=\{\{[Tt]om|$)", flags=re.DOTALL)


if __name__ == '__main__':
	PAGENAME_PREFIX = 'ТСД'
	SITE = pywikibot.Site('ru', 'wikisource')
	# pages = [
	# 	'ТСД/Фабрика',
	# 	'ТСД/Фабрика/ДО'
	# ]
	pages = file_readlines('/home/vladislav/var/tsd_to_split.txt')

	for title in pages:
		page = pywikibot.Page(SITE, title)
		if not page.isRedirectPage():
			wikicode = mwp.parse(page.text)   # wikicode = mwp.parse(t)
			articleTitle = title.partition('/')[2]

			tpl_header = pop_tpl_header()
			remove_comments()
			# categories = pop_tpl_categories()

			pageEditions = [str(tpl.get(1).value).strip() for tpl in wikicode.filter_templates()
							if tpl.name.matches('tom') and tpl.has(1) and tpl.has(2)]  # номера имеющихся изданий
			title_new = rename_to_num_edition(pageEditions, articleTitle)
			page.move(title_new, 'сортировка по изданиям; см. СО проекта ТСД')


		# Разделение переименованой страницы на страницы по изданиям
		page = page.moved_target()   # page = pywikibot.Page(SITE, title_new)
		wikicode = mwp.parse(page.text)		# wikicode = mwp.parse(t)
		articleTitle = title.partition('/')[2]
		tpl_header = pop_tpl_header()
		remove_comments()
		categories = pop_tpl_categories()

		split_by_sectionsEds = sections_re.findall(str(wikicode))
		pages_new = [section_processing(section, tpl_header, categories, articleTitle)
					 for section in split_by_sectionsEds]

		for page_new in pages_new:
			if page_new is None:
				continue

			new_content = page_new[3]
			tpl_header = page_new[2]
			title_ed = page_new[1]
			page_new_text = "%s\n\n%s\n\n%s\n" % (tpl_header, new_content, '\n'.join(categories))

			# title_ed = '%s%s/%s' % (PAGENAME_PREFIX, page_new[0], articleTitle)
			if title_ed == page.title():
				page_ed = page
			else:
				page_ed = pywikibot.Page(SITE, title_ed)
			page_ed.text = page_new_text
			page_ed.save('из [[%s]], разделение по изданиям' % title)
			print(title_ed + '\n' + new_content)
	pass
