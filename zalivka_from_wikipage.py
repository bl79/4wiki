#!/usr/bin/env python3
# coding: utf8
#
# author: https://github.com/vladiscripts
#
import re
import pywikibot
import vladi_commons


class zalivka_from_wikipage():
	# LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки
	SITE = pywikibot.Site('ru', 'wikisource')
	FI = '/home/vladislav/workspace/temp/bse1-5.txt'
	FO = FI + ' new'
	TEXTOVKA_FROM_FILE = 0
	REWRITE_EXIST_PAGES = None
	CLEAN_TEXT_FROM_POSTED = None  # Не ясен смысл и алгоритм очистки текстовки от залитых
	MAKE_REDIRECTS = None
	# PAGENAME_PREFIX = 'РСКД'
	PAGENAME_PREFIX = 'БСЭ1'
	PAGENAME_POSTFIX = ''
	SUMMARY = 'заливка'
	textovka_text = []
	log = set()  # already_exists_pages
	re_pagename_from_wikilink = re.compile(r'\[\[%s/(.*?)\s*(?:\||\]\])' % PAGENAME_PREFIX)

	# re_pagename_from_wikilink = re.compile(r'\[\[БСЭ1/(.*?)\s*(?:\||\]\])')

	def __init__(self, TEXTOVKA_TITLE):
		self.TEXTOVKA_TITLE = TEXTOVKA_TITLE

		if self.TEXTOVKA_FROM_FILE == 1:
			self.textovka_text = vladi_commons.file_readtext(self.FI)
		else:
			self.textovka = pywikibot.Page(self.SITE, self.TEXTOVKA_TITLE)
			self.textovka_text = self.textovka.get()
		self.all_sections = self.get_all_sections()

	def get_all_sections(self):
		sections_re = re.compile(r'''
			((?:\n|^)={2,}\s*(.*?)\s*={2,}\n[\n\s]*	# заголовок
			(.*?))		# текст секции
			(?=\n==|$)	# конец секции или страницы
			''', flags=re.DOTALL | re.VERBOSE)
		return sections_re.findall(self.textovka_text)

	def clean_header(self, header):
		h = self.re_pagename_from_wikilink.search(header)
		if h:
			header = h.group(1)
		else:
			header = re.sub('\s*#[\s\d]*$', '', header)
		return header

	def post_wikipages(self):
		for section in self.all_sections:
			header_and_text = section[0]
			text = section[2]
			header = section[1]
			# is_header_mark = None  # if header.find('#') == -1 else True
			# if not is_header_mark:
			title_article = self.clean_header(header)
			if self.MAKE_REDIRECTS:
				title_second = re.search(r'# (.+)\s*', header).group(1)

			# posttext = "{{%s\n|НАЗВАНИЕ = %s\n|НАЗВАНИЕОРИГИНАЛА = %s\n|КАЧЕСТВО = 2\n|ВИКИПЕДИЯ = \n}}\n\n%s" % (			self.PAGENAME_PREFIX, title_article, title_second, text)
			posttext = "{{%s |КАЧЕСТВО = 2 |ВИКИПЕДИЯ = }}\n\n%s" % (self.PAGENAME_PREFIX, text)
			self.post_wikipage(header_and_text, title_article, posttext)

			if self.MAKE_REDIRECTS:
				try:
					posttext = r'#перенаправление [[%s/%s]]' % (self.PAGENAME_PREFIX, title_article)
					self.post_wikipage(header_and_text, title_second, posttext)
				except:
					print('No a redirect header in: ' + header)
				pass
			pass

	def post_wikipage(self, header_and_text, header, posttext):
		header_full = self.PAGENAME_PREFIX + '/' + header + self.PAGENAME_POSTFIX
		page_new = pywikibot.Page(self.SITE, header_full)

		if not page_new.exists():
			self.save_wikipage(page_new, posttext)
		elif page_new.isRedirectPage():
			self.log.add(header_full + ' : IsRedirectPage')
			# if self.REWRITE_EXIST_PAGES:
			# 	self.save_wikipage(page_new, posttext)
			# self.save_wikipage(page_new, posttext)
			pass
		else:
			self.log.add(header_full + ' : Is page')
			if self.REWRITE_EXIST_PAGES:
				self.save_wikipage(page_new, posttext)

		if self.CLEAN_TEXT_FROM_POSTED:
			# очистка текстовки от залитых статей
			self.textovka_text = self.textovka_text.replace(header_and_text, '')
			zalivka.log2file()
		pass

	def save_wikipage(self, page_obj, posttext):
		page_obj.text = posttext
		page_obj.save(self.SUMMARY)

	def log2wiki(self):
		# отметки и отчёты залитого
		self.textovka.text = self.textovka_text
		self.textovka.save('залито')

	def log2file(self):
		vladi_commons.file_savetext(self.FO, self.textovka_text)

		# vladi_commons.file_savelines('already_exists_pages.log', self.log)

TEXTOVKI_TITLES = """\
Обсуждение:Большая советская энциклопедия/для заливки/том 7
Обсуждение:Большая советская энциклопедия/для заливки/том 8
""".splitlines()
for TEXTOVKA_TITLE in TEXTOVKI_TITLES:
	zalivka = zalivka_from_wikipage(TEXTOVKA_TITLE)
	zalivka.post_wikipages()

if zalivka.CLEAN_TEXT_FROM_POSTED:
	zalivka.log2file()
# zalivka.log2wiki()
