#!/usr/bin/env python3
# coding: utf8
#
# author: https://github.com/vladiscripts
#
import re
import mwparserfromhell
import pywikibot
import vladi_commons

listpages_filename = 'rskd2.txt'  # список страниц для обработки
templates = ('РСКД',)
parameters = """\
НАЗВАНИЕ
НАЗВАНИЕОРИГИНАЛА
СТРАНИЦА
""".splitlines()


def remove_parameters(wikicode, tpl_name, keys_list):
	for tpl in wikicode.filter_templates():
		if tpl.name.matches(tpl_name):
			for k in keys_list:
				if tpl.has(k): tpl.remove(k)
	return wikicode

with open(listpages_filename, 'r', encoding='utf-8') as f: 
	listpages = f.read().splitlines()
#listpages = ['РСКД/Aeolis',]

site = pywikibot.Site('ru', 'wikisource')

for title in listpages:
	if title == '': continue	
	page = pywikibot.Page(site, title)
	if page.isRedirectPage(): continue
	text = page.get()
	text = text.replace('__NOTOC__', '')
	wikicode = mwparserfromhell.parse(text)
	page.text = str(remove_parameters(wikicode, templates, parameters))
	# from pywikibot import editor as editarticle
	page.save('чистка параметров шаблона')
