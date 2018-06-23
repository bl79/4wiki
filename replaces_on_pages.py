#!/usr/bin/env python3
# coding: utf8
#
# author: https://github.com/vladiscripts
#
import re
import pywikibot
from vladi_commons import vladi_commons
from unidecode import unidecode
from unicodedata import normalize

class replaces_on_wikipages():
	# LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки
	SITE = pywikibot.Site('ru', 'wikisource')
	# FI = '/home/vladislav/workspace/temp/bse1-5.txt'
	FI = '/home/vladislav/var/rskd_listpages.txt'
	FO = FI + ' new'
	TEXTOVKA_FROM_FILE = 0
	PAGETITLES_FROM_FILE = 1
	REWRITE_EXIST_PAGES = None
	REWRITE_REDIRECTS = None
	CLEAN_TEXT_FROM_POSTED = None  # Не ясен смысл и алгоритм очистки текстовки от залитых
	MAKE_REDIRECTS = None
	PAGENAME_PREFIX = 'РСКД'
	# PAGENAME_PREFIX = 'БСЭ1'
	PAGENAME_POSTFIX = ''
	# SUMMARY = 'заливка'
	SUMMARY = 'unicode normalize'
	textovki_texts = []
	titles = []
	all_sections = set()
	log = set()  # already_exists_pages
	re_pagename_from_wikilink = re.compile(r'\[\[%s/(.*?)\s*(?:\||\]\])' % PAGENAME_PREFIX)
	sections_re = re.compile(r'''
					((?:\n|^)={2,}\s*(.*?)\s*={2,}\n[\n\s]*	# заголовок
					(.*?))		# текст секции
					(?=\n==|$)	# конец секции или страницы
					''', flags=re.DOTALL | re.VERBOSE)

	# re_pagename_from_wikilink = re.compile(r'\[\[БСЭ1/(.*?)\s*(?:\||\]\])')

	def __init__(self, pages_titles):
		self.get_titles(pages_titles)
		# self.get_all_sections()

	def get_titles(self, pages_titles):
		if self.PAGETITLES_FROM_FILE == 1:
			self.titles = vladi_commons.file_readlines(self.FI)
		else:
			self.titles = [title for title in pages_titles]

	def pages_replace(self):
		# self.titles = ['РСКД/Ὑβρις']
		for title in self.titles:
			page = pywikibot.Page(self.SITE, title)

			if not page.exists():
				print('no page: ', title)
				continue
			elif page.exists():
				if page.isRedirectPage():
					# self.log.add('isRedirectPage: ', title)
					print('isRedirectPage: ', title)
					if not self.REWRITE_REDIRECTS:
						continue
				else:
					print('is page: ', title)
					# self.log.add(title + ' : is page')
				page.get()
				posttext = self.page_replaces(page.text)
				self.save_wikipage(page, posttext)

	def page_replaces(self, text):
		t = normalize('NFD', text)		
		t = re.sub(r"([^'])'(\w)\u0301", r'\1\2'+'\u0313\u0301', t)
		t = t.replace('\u0303', '\u0342')  # периспоменти combining из комбинируемая тильда
		t = t.replace('\uf008', '\u0301').replace('\uf014', '\u0313').replace('\uf00f', '\u0300')
		t = t.replace("ε̉", "ἐ").replace("η̉", "ἠ").replace("α̉", "ἀ")
		# t = t.replace('·', '.')
		t = normalize('NFC', t)
		return t
		# insource:/[^\w0-9Ά-ϓἀ-ῼ!-@№\{\}\|\[\]\(\)<>.,;:?!='"#*•\/\\a-zA-Zа-яёА-ЯЁ\s\-—īĭöŭăé]+/  -"РСКД/Словник" prefix:"РСКД"

	def save_textovki_in_one_file(self, filename):
		tt = '\n'.join(self.textovki_texts)
		vladi_commons.file_savetext(filename, tt)

	def get_all_sections(self):
		sections_re = re.compile(r'''
			((?:\n|^)={2,}\s*(.*?)\s*={2,}\n[\n\s]*	# заголовок
			(.*?))		# текст секции
			(?=\n==|$)	# конец секции или страницы
			''', flags=re.DOTALL | re.VERBOSE)
		for t in self.textovki_texts:
			self.all_sections = self.all_sections.union(sections_re.findall(t))
			pass
		# self.all_sections += [sections_re.findall(t) for t in self.textovki_texts]

	def clean_header(self, header):
		h = self.re_pagename_from_wikilink.search(header)
		if h:
			header = h.group(1)
		else:
			header = re.sub('\s*#[\s\d]*$', '', header)
		return header

	def get_section_titles(self):
		self.titles_ru = []
		self.titles_ru_doubles = []
		self.doubles = []
		for section in self.all_sections:
			header_and_text = section[0]
			text = section[2]
			header = section[1]
			title_ru = self.clean_header(header)
			h = re.search(r'# (.+)\s*', header)
			title2 = self.clean_header(h.group(1))

			if re.search(r"^[A-Z]", title2, flags=re.I):
				title2 = unidecode(title2)  # remove diakritik
			self.post_wikipage(title2, self.make_tpl_postpage(title_ru, title2, text))
			pass

			# self.find_doubles_titles(title_ru, title_second, text, header_and_text)

	def save_wikipage(self, page_obj, posttext):
		if page_obj.text != posttext:
			print('saving...')
			page_obj.text = posttext
			page_obj.save(self.SUMMARY)

	def log2wiki(self):
		# отметки и отчёты залитого
		self.page.text = self.textovki_texts
		self.page.save('залито')

	def log2file(self):
		vladi_commons.file_savetext(self.FO, self.textovki_texts)

	# vladi_commons.file_savelines('already_exists_pages.log', self.log)


# TEXTOVKI_TITLES = """\
# Участник:Vladis13/lubker textovka7
# Участник:Vladis13/lubker textovka6
# Участник:Vladis13/lubker textovka5
# Участник:Vladis13/lubker textovka4
# Участник:Vladis13/lubker textovka3
# Участник:Vladis13/lubker textovka2
# Участник:Vladis13/lubker textovka1
# """.splitlines()
TEXTOVKI_TITLES = """\
Участник:Vladis13/lubker ancrome1
""".splitlines()
pages = replaces_on_wikipages(TEXTOVKI_TITLES)
pages.pages_replace()
# pages.save_textovki_in_one_file(FI)
# pages.get_section_titles()
# vladi_commons.file_savelines('/home/vladislav/workspace/temp/lubker/doubles_in_textoka', zalivka.titles_ru_doubles)
# vladi_commons.file_savelines('/home/vladislav/workspace/temp/lubker/doubles', zalivka.doubles)

if pages.CLEAN_TEXT_FROM_POSTED:
	pages.log2file()
# pages.log2wiki()
