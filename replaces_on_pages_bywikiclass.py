# -*- coding: utf-8 -*-
import re
import vladi_commons
from lib_for_mwparserfromhell import listtpls, tpl_add_param, replaceParamValue
import pywikibot
import mwparserfromhell as mwp
import sqlite3
from collections import namedtuple
from wikiclass import WikiMethods


class wiki(WikiMethods):
	# LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки
	EDITION = ''
	SITE = pywikibot.Site('ru', 'wikisource')
	# FI_listpages = '/home/vladislav/var/tsd%s-4_listpages.txt' % EDITION
	FI_listpages = '/home/vladislav/var/tsd_so_listpages.txt'
	FI_wordlists_list = '/home/vladislav/var/tsd%s_worlists.txt' % EDITION
	FO = FI_wordlists_list + '_pages_to_rename'
	FI_wl_text = '/home/vladislav/var/tsd%s_worlists.txt' % EDITION
	FO_wl_text = FI_wl_text + '_pages_to_rename'
	PATH_DB = '/home/vladislav/var/tsd.sqlite'
	db_tablename = 'tsd%s' % EDITION
	TEXTOVKA_FROM_FILE = 0  # or from wikipage
	LIST_OF_WORDLISTS_FROM_FILE = 1  # or from wikipage
	REWRITE_EXIST_PAGES = None
	CLEAN_TEXT_FROM_POSTED = None  # Не ясен смысл и алгоритм очистки текстовки от залитых
	MAKE_REDIRECTS = None
	PAGENAME_PREFIX = 'ТСД%s' % EDITION
	PAGENAME_POSTFIX = ''
	SUMMARY = 'заливка'
	pageslist = []
	wordlists_text = []
	lat_redirects = []
	list2rename = []
	# wordlist_title = ''
	# wordlist_text = ''
	wordlists = []
	wordlist = {}
	page_data = {}
	stock_redirects = []
	log = set()  # already_exists_pages
	re_pagename_from_wikilink = re.compile(r'\[\[%s/(.*?)\s*(?:\||\]\])' % PAGENAME_PREFIX)

	def __init__(self):
		super().__init__()
		# список страниц
		self.pageslist = vladi_commons.file_readlines(self.FI_listpages)
		# self.pageslist = ['ТСД2/А']

		# изменение и постинг статей
		for pagename in self.pageslist:
			self.process_article(pagename)

	def process_article(self, pagename):
		"""изменение и постинг статьи"""
		self.cur_article_name = self.get_cur_article_name(pagename)
		self.page_data = self.open_page(pagename,
										mark_RedirectPages_category='ТСД:Перенаправление в словнике - проверить')
		if self.page_data:
			# заполнение self.page_data
			self.parse_page(self.page_data['obj'])

			self.replaces_on_page()

			new_text = str(self.page_data['wikicode'])
			new_text = new_text.replace('[[Категория:ТСД:Статьи не указанные в словниках]]', '')

			new_text = re.sub(r'(\| *-?ТСД3 *=.*?)(\| *-?ТСД1 *=.*?\n?)(?!\|\})', r'\2\1', new_text, flags=re.DOTALL)
			new_text = re.sub(r'(\| *-?ТСД3 *=.*?)(\| *-?ТСД2 *=.*?\n?)(?!\|\})', r'\2\1', new_text, flags=re.DOTALL)
			new_text = re.sub(r'(\| *-?ТСД2 *=.*?)(\| *-?ТСД1 *=.*?\n?)(?!\|\})', r'\2\1', new_text, flags=re.DOTALL)

			new_text = re.sub(r'(= *)\}\}', r'\1\n}}', new_text)
			self.wiki_posting_page(self.page_data['obj'], new_text, '+params ТСД[1-3], СЕКЦИЯ; -значение ВИКИПЕДИЯ если == pagename')


	def replaces_on_page(self):
		tsd_tpl = listtpls(self.page_data['wikicode'], 'ТСД')[0]
		for i in [1, 2, 3]:
			prefix = 'ТСД' + str(i)  # ТСД1
			if not prefix in tsd_tpl and not '-'+prefix in tsd_tpl:
				tsd_tpl.add(prefix, '')

		parameter = 'СЕКЦИЯ'
		tpl_add_param(tsd_tpl, parameter, '')
		section = str(tsd_tpl.get(parameter).value.strip())
		section = section.rstrip('+')
		if section == self.cur_article_name:
			section	= '\n'
		tsd_tpl.get(parameter).value = section

		parameter = 'ВИКИПЕДИЯ'
		if tsd_tpl.has(parameter):
			v = str(tsd_tpl.get(parameter).value.strip())
			if v == self.cur_article_name:
				tsd_tpl.get(parameter).value = '\n'


	# def redirects_do_check_and_renamepages(self, cur_pagename, articlename_in_wordlist):
	# 	print('проверка на редиркт и переименование')
	# 	page_article_data = self.open_page(cur_pagename,
	# 									   switch_to_RedirectTarget=True,
	# 									   mark_RedirectPages_category='ТСД:Перенаправление в словнике - проверить')
	# 	page_article_obj = page_article_data['obj']
	# 	if page_article_obj.isRedirectPage():
	# 		n = cur_pagename.split('/')
	# 		n[1] = self.cur_article_name_tpl
	# 		article_new_from_wl = '/'.join(n)
	# 		page_article_obj.title = article_new_from_wl
	# 		self.wiki_posting_page(page_article_obj, str(page_article_data['wikicode']),
	# 							   'переименование по словнику')
	# 		pass
	# 	return


	# def process_tagPages(self):
	# 	# Новое имя секции, с '+'
	# 	sectionname_new = self.tsd_section_name_new(self.cur_article_name, self.page_data['pagename'])
	# 	# sectionname_new = self.cur_article_name
	# 	# Обновить секцию в теге <pages>
	# 	if 'tag_pages' in self.page_data:
	# 		tag_pages = self.page_data['tag_pages']
	# 		tag_pages.get('onlysection').value = sectionname_new
	#
	# 		# Убрать <pages> со страницы
	# 		self.page_data['wikicode'].remove(tag_pages)
	#
	# 	# Добавить СЕКЦИЯ= шаблон-шапку, если отличается от названия статьи
	# 	self.add_param_SECTION_in_headertpl(sectionname_new)
	#
	# def tsd_section_name_new(self, articlename, pagename):
	# 	articlename = self.string_strip(articlename)
	# 	sectionname_new = ''
	# 	if 'ДО' in pagename.split('/'):
	# 		sectionname_new = articlename
	# 	else:
	# 		sectionname_new = articlename + '+'
	# 	return sectionname_new


wordlist_links = wiki()
wordlist_links.savelist2rename('pages2rename2.txt')
