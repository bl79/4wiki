#!/usr/bin/env python3
# coding: utf-8
#
# author: https://github.com/vladiscripts
#
import requests
from urllib.parse import quote
from lxml import etree
import re
import pywikibot
import vladi_commons


def normalization_pagename(t):
	""" Первая буква в верхний регистр, ' ' > '_' """
	t = t.strip()
	return t[0:1].upper() + t[1:].replace(' ', '_')

# wikipages_filename = r'..\temp\AWBfile.txt'
# text = vladi_commons.file_readtext(wikipages_filename)
exclude_namespaces = r'(Special|Служебная|Участник|User|У|Обсуждение[ _]участника|ОУ|Википедия|ВП|Обсуждение[ _]Википедии|Обсуждение):'
close_tpls = re.compile(r'\{\{([Оо]тпатрулировано|[Сс]делано|[Dd]one|[Оо]тклонено)\s*(?:\|.*?)?\}\}')
sections_re = re.compile(r"<section begin=[\"']([^\"']*(?:\D|\D \d))[\"'] */>[\n\s]*\{\{выступ\s*\|\s*\[?\s*''+([^']+)", re.DOTALL)
link_re = re.compile(r'\s*(?<!<s>)\s*(\[\[(?!%s).*?\]\])' % exclude_namespaces)
link_title_re = re.compile(r'\[\[([^]|]+).*?\]\]')
link_just_re = re.compile(r'\s*(\[\[(?!%s).*?\]\])' % exclude_namespaces)
tag_li_re = re.compile(r'^[*#](.*)$', re.MULTILINE)
header_re = re.compile(r'^==+([^=]+)==+$', re.MULTILINE)
textend = re.compile(r'\n*$')

re_akut = re.compile(r'\{\{[Аа]кут3?\}\}')
re_notw = re.compile(r'[^\w -]')

page_tsds_list = []

site = pywikibot.Site('ru', 'wikisource')
offset_of_volumes = [17, 2, 2, 4]
volume = 4
scanpageN = 5
while scanpageN <= 800:
	# for workpage in workpages:
	workpage = 'Страница:Толковый словарь. Том 4 (Даль 1909).djvu/' + str(scanpageN)
	page = pywikibot.Page(site, workpage)
	text = page.get()

	first_tsds = True

	# нечётный номер страницы
	# if number % 2:
	# 	pb = pb + 1
	# return pb / 2 + offset[2]

	bookpageN = str((scanpageN - offset_of_volumes[volume - 1]) * 2 - 1) \
				+ '-' + \
				str((scanpageN - offset_of_volumes[volume - 1]) * 2)

	sections = sections_re.findall(text)
	for section in sections:
		word_DO = section[1]
		word_DO = re_akut.sub('', word_DO)
		word_DO = re_notw.sub('', word_DO)

		if first_tsds:
			marker_showpageN = '\t|3'
			first_tsds = None
		else:
			marker_showpageN = ''

		tsds = '# {{tsds|%s\t|%s\t|%s%s}}' % (section[0], word_DO, str(bookpageN), marker_showpageN)

		page_tsds_list.append(tsds)

	scanpageN += 1


text = '\n'.join(page_tsds_list)

pass

vladi_commons.file_savetext('tsds3-' + str(volume) + '.txt', text)
pass
