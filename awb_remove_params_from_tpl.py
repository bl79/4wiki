#!/usr/bin/env python3
# coding: utf-8
#
# author: https://github.com/vladiscripts
#
import os
import re
import pywikibot
import mwparserfromhell
from vladi_commons import vladi_commons, lib_for_mwparserfromhell

page_title = False
# if len(sys.argv) > 1:
	# page_title = sys.argv[1]

wikipages_filename = r'/tmp/AWBwikipage.txt'
listpages_filename = '/home/vladislav/workspace/listpages.txt'
listpages = vladi_commons.file_readlines_in_set(listpages_filename)
print('listpages loaded')
site = pywikibot.Site('ru', 'wikisource')
for title in listpages:
	if title == '': continue
	page = pywikibot.Page(site, title)
	text_original = page.get()
	text = text_original

	template = 'ТСД'
	parameters = (
		'НАЗВАНИЕ',
		'НАЗВАНИЕ2',
		'1-ИЗД.ТОМ',
		'1-ИЗД.СТРАНИЦА СКАНА',
		'1-ИЗД.СТРАНИЦЫ КНИГИ',
		'2-ИЗД.ТОМ',
		'2-ИЗД.СТРАНИЦА СКАНА',
		'2-ИЗД.СТРАНИЦЫ КНИГИ',
		'3-ИЗД.ТОМ',
		'3-ИЗД.СТРАНИЦА СКАНА',
		'3-ИЗД.СТРАНИЦЫ КНИГИ',
		'НАВИГАЦИЯ',
		'КАЧЕСТВО',
		'ПРЕДЫДУЩИЙ',
		'СЛЕДУЮЩИЙ',
		'СПИСОК',
		'ДРУГОЕ',
		)


	text = text.replace('__NOTOC__', '')
	wikicode = mwparserfromhell.parse(text)
	# wikicode = str(remove_parameters(wikicode, template, parameters))
	# wikicode = str(lib_for_mwparserfromhell.delete_tpl(wikicode, 'sub-nav'))

	lib_for_mwparserfromhell.remove_parameters(wikicode, template, parameters)
	lib_for_mwparserfromhell.delete_tpl(wikicode, 'sub-nav')

	pass
	text = str(wikicode)
	# print(str(wikicode))
	# print(text)


	if text_original != text:
		# Запись
		page.text = text
		page.save("чистка параметров шаблона")

		#python_and_path = r'python3 /home/vladislav/pwb/scripts/'
		## python_and_path = r'python3 scripts/'
		#pwb_cfg = r' -dir:~/.pywikibot/'
		#marker_page_start = '€@@@@@@@@€'
		#marker_page_end   = '@€€€€€€€€@'

		#text = marker_page_start+'\n' + "'''"+title+"'''\n" + text + '\n'+marker_page_end+'\n'
		## vladi_commons.file_savetext(wikipages_filename, text)

		#params = [
			#'-family:wikisource',
			#'-file:' + wikipages_filename,
			#'-begin:"' + marker_page_start + '"', '-end:"' + marker_page_end + '"', '-notitle',
			#'-summary:"чистка параметров шаблона"',
			#'-pt:0', pwb_cfg,
			#'-force',
			## '-simulate',
		#]

		## os.system(python_and_path + 'pagefromfile.py' + ' ' + ' '.join(params))

