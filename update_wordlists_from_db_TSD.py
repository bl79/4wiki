# -*- coding: utf-8 -*-
import re
import vladi_commons
from lib_for_mwparserfromhell import listtpls
import pywikibot
import mwparserfromhell as mwp
import sqlite3
from collections import namedtuple
from wikiclass import WikiMethods


class wiki(WikiMethods):
	# LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки
	EDITION = 2
	SITE = pywikibot.Site('ru', 'wikisource')
	FI_listpages = '/home/vladislav/var/tsd%s_listpages.txt' % EDITION
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
		# self.FI_wordlists_list = """
		# ТСД-словник/2/А
		# """.splitlines()
		# self.WORDLIST_TITLES = vladi_commons.file_readlines(self.FI_wordlists_list)
		self.get_wordlists()

		# Обновление пагинации в словниках
		self.update_wordlists()

	def update_wordlists(self):
		# Обновить словники и пагинацию из БД
		self.con = sqlite3.connect(self.PATH_DB)
		for self.wordlist in self.wordlists:
			self.parse_wordlist_wmp()

		# постинг словника
		for self.wordlist in self.wordlists:
			# self.wordlist = namedtuple('wordlist', wl.keys())(**wl)
			# постинг словника
			self.wiki_posting_page(self.wordlist['obj'], str(self.wordlist['wikicode']), 'пагинация')

	def parse_wordlist_wmp(self):
		list_tpls = listtpls(self.wordlist['wikicode'], tplname='tsds')
		for tpl in list_tpls:
			self.cur_article_name_tpl = tpl.get(1).value.strip()
			cur_page_name = '%s/%s' % (self.PAGENAME_PREFIX, self.cur_article_name_tpl)
			cur_article_name_DO = '%s/%s/ДО' % (self.PAGENAME_PREFIX, self.cur_article_name_tpl) if tpl.has(
				1) else False
			# pagination_in_tpl = re.findall('\d+', params_pagination)

			# self.check_page(cur_page_name)
			# self.check_page(cur_article_name_DO)

			# if self.cur_article_name == self.page_data['article_name']:
			# 	self.update_wordlist_item()
			# 	break

			# Обновить tsds и пагинацию из БД
			self.db_get_article_data(self.cur_article_name_tpl, tablename=self.db_tablename)
			if len(self.page_data):
				self.update_wordlist_item(tpl, self.page_data, use_pagenum_instead_scannum=True)
			# else:
			# 	print('нет данных по статье в БД: %s' % self.cur_article_name_tpl)
			pass

		# сохранение найденных редиректов в файл в формате списка переименования для pwb
		if len(self.redirects):
			vladi_commons.file_savelines(self.FO + self.wordlist['title'], self.redirects)

		# постинг словника
		# self.wiki_posting_page(self.wordlist.page_obj, str(self.wordlist.wikicode), 'пагинация')

	def redirects_do_check_and_renamepages(self, cur_pagename, articlename_in_wordlist):
		print('проверка на редиркт и переименование')
		page_article_data = self.open_page(cur_pagename,
										   switch_to_RedirectTarget=True,
										   mark_RedirectPages_category='ТСД:Перенаправление в словнике - проверить')
		page_article_obj = page_article_data['obj']
		if page_article_obj.isRedirectPage():
			n = cur_pagename.split('/')
			n[1] = self.cur_article_name_tpl
			article_new_from_wl = '/'.join(n)
			page_article_obj.title = article_new_from_wl
			self.wiki_posting_page(page_article_obj, str(page_article_data['wikicode']),
								   'переименование по словнику')


wordlist_links = wiki()
wordlist_links.savelist2rename('pages2rename2.txt')
