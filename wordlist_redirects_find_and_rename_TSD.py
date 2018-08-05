# -*- coding: utf-8 -*-
import re
import vladi_commons
from lib_for_mwparserfromhell import listtpls
import pywikibot
from my_wikiclass.wikiclass import WikiMethods


class wiki(WikiMethods):
	# LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки
	EDITION = 2
	SITE = pywikibot.Site('ru', 'wikisource')
	FI_listpages = '/home/vladislav/var/tsd%s_listpages.txt' % EDITION
	FI_wordlists_list = '/home/vladislav/var/tsd%s_worlists.txt' % EDITION
	FO = FI_wordlists_list + '_pages_to_rename'
	FI_wl_text = '/home/vladislav/var/tsd%s_worlists.txt' % EDITION
	FO_wl_text = FI_wl_text + '_pages_to_rename'
	FO_REDIRECTS = '/home/vladislav/var/tsd%s_redirects.txt' % EDITION
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
	stock_redirects = True
	re_pagename_from_wikilink = re.compile(r'\[\[%s/(.*?)\s*(?:\||\]\])' % PAGENAME_PREFIX)

	def __init__(self):
		super().__init__()
		# self.FI_wordlists_list = """
		# ТСД-словник/2/А
		# """.splitlines()
		# self.WORDLIST_TITLES = vladi_commons.file_readlines(self.FI_wordlists_list)
		use_pywikibot = False
		use_mwparser = False
		get_html = True
		self.get_wordlists(use_pywikibot=use_pywikibot, use_mwparser=use_mwparser, get_html=get_html)
		for self.wordlist in self.wordlists:
			if use_mwparser:
				self.process_wordlist_wmp()
			elif get_html:
				self.process_wordlist_html()
		vladi_commons.file_savelines(self.FO_REDIRECTS, self.redirects)
		# self.posting_wordlists()
		pass

	def process_wordlist_html(self):
		hxs = self.wordlist['html_parsed']
		if hxs is None:
			print('No html_parsed in %s' % self.wordlist['title'])
			return
		# articles_e = hxs.cssselect('ol li')
		# for article_e in articles_e:
		# 	for a in article_e:
		# 		title = a.get('title')
		# 		if not title or not str(title.startswith(self.PAGENAME_PREFIX)):
		# 			continue
		# 		# href = a.get('href')
		# 		if a.cssselect('[class~=mw-redirect]'):
		# 			title = a.get('title')
		# 			if self.stock_redirects:
		# 				self.redirects.append(title)
		# 				print(title)
		# 			pass
		# 		pass
		redirects_e = hxs.cssselect('li a[class~=mw-redirect]')
		for a in redirects_e:
			title = a.get('title')
			if self.stock_redirects:
				self.redirects.append(title)
				print(title)
		pass

	def process_wordlist_wmp(self):
		list_tpls = listtpls(self.wordlist['wikicode'], tplname='tsds')
		for tpl in list_tpls:
			self.cur_article_name_tpl = tpl.get(1).value.strip()
			cur_wl_page_name = '%s/%s' % (self.PAGENAME_PREFIX, self.cur_article_name_tpl)
			cur_wl_article_name_DO = '%s/%s/ДО' % (self.PAGENAME_PREFIX, self.cur_article_name_tpl) if tpl.has(
				1) else False

			# проверка статьи СО
			self.redirects_do_check_and_renamepages(cur_wl_page_name)
			# проверка статьи ДО
			self.redirects_do_check_and_renamepages(cur_wl_article_name_DO)

		# сохранение найденных редиректов в файл в формате списка переименования для pwb
		# if len(self.redirects):
		# 	vladi_commons.file_savelines(self.FO + self.wordlist['title'], self.redirects)

		# постинг словника
		# self.wiki_posting_page(self.wordlist.page_obj, str(self.wordlist.wikicode), 'пагинация')

	def redirects_do_check_and_renamepages(self, articlename_in_wordlist, old_orphography=False):
		print('проверка на редиркт и переименование')
		PAGENAME_POSTFIX = '/ДО' if old_orphography else ''
		pagename_article_in_wordlist = '%s/%s' % (self.PAGENAME_PREFIX, articlename_in_wordlist) + PAGENAME_POSTFIX
		page_article_data = self.open_page(pagename_article_in_wordlist,
										   switch_to_RedirectTarget=True,
										   mark_RedirectPages_category='ТСД:Перенаправление в словнике - проверить')
		page_obj = page_article_data['obj']
		if page_obj.exists():
			if page_obj.isRedirectPage():
				RedirectTarget = page_obj.getRedirectTarget()
				page_redirect_obj = RedirectTarget
				# pagename_redirect = page_redirect_obj.title
				page_redirect_obj.title = pagename_article_in_wordlist
				mark_RedirectPages_category = True
				if mark_RedirectPages_category:
					page_redirect_obj.text = page_redirect_obj.text + '\n[[Категория:%s]]' % mark_RedirectPages_category

				# n = cur_pagename.split('/')
				# n[1] = self.cur_article_name_tpl
				# article_new_from_wl = '/'.join(n)
				self.wiki_posting_page(page_redirect_obj, str(page_article_data['wikicode']),
									   'переименование по словнику')
				pass
		return

	def posting_wordlists(self):
		# постинг словников
		for self.wordlist in self.wordlists:
			self.wiki_posting_page(self.wordlist['obj'], str(self.wordlist['wikicode']), 'пагинация')


wordlist_links = wiki()
# wordlist_links.savelist2rename('pages2rename2.txt')
