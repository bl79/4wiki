#!/usr/bin/env python3
# coding: utf8
#
# author: https://github.com/vladiscripts
#
import re
import pywikibot
import vladi_commons
from unidecode import unidecode

class zalivka_from_wikipage():
	# LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки
	SITE = pywikibot.Site('ru', 'wikisource')
	FI = '/home/vladislav/workspace/temp/bse1-5.txt'
	FI = '/home/vladislav/workspace/temp/lubker/all_wikiarticles.txt'
	FO = FI + ' new'
	TEXTOVKA_FROM_FILE = 0
	REWRITE_EXIST_PAGES = None
	REWRITE_REDIRECTS = True
	CLEAN_TEXT_FROM_POSTED = None  # Не ясен смысл и алгоритм очистки текстовки от залитых
	MAKE_REDIRECTS = None
	PAGENAME_PREFIX = 'РСКД'
	# PAGENAME_PREFIX = 'БСЭ1'
	PAGENAME_POSTFIX = ''
	SUMMARY = 'заливка'
	textovki_texts = []
	all_sections = set()
	log = set()  # already_exists_pages
	re_pagename_from_wikilink = re.compile(r'\[\[%s/(.*?)\s*(?:\||\]\])' % PAGENAME_PREFIX)
	sections_re = re.compile(r'''
					((?:\n|^)={2,}\s*(.*?)\s*={2,}\n[\n\s]*	# заголовок
					(.*?))		# текст секции
					(?=\n==|$)	# конец секции или страницы
					''', flags=re.DOTALL | re.VERBOSE)

	# re_pagename_from_wikilink = re.compile(r'\[\[БСЭ1/(.*?)\s*(?:\||\]\])')

	def __init__(self, wordlist_titles):
		self.get_wordlists(wordlist_titles)
		self.get_all_sections()

	def get_wordlists(self, wordlist_titles):
		if self.TEXTOVKA_FROM_FILE == 1:
			self.textovki_texts = [vladi_commons.file_readtext(self.FI)]
		else:
			for textovka_title in wordlist_titles:
				self.textovka = pywikibot.Page(self.SITE, textovka_title)
				self.textovki_texts.append(self.textovka.get())

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

	def find_doubles_titles(self, title_ru, title2, text, header_and_text):
		if title_ru in self.titles_ru:
			p = '%s/%s' % (self.PAGENAME_PREFIX, title_ru)
			# print(p)

			# создание двух разделов статей для заголовков-омонимов
			a1 = header_and_text.replace('# ' + title2, '# [[%s/%s|%s]]' % (self.PAGENAME_PREFIX, title2, title2))
			for i in self.all_sections:
				header2 = i[1]
				h2 = re.search(r'# (.+)\s*', header2)
				title_second2 = h2.group(1)
				title_ru2 = self.clean_header(header2)
				if title_ru2 == title_ru:
					a2 = i[0].replace('# ' + title_second2, '# [[%s/%s|%s]]' % (self.PAGENAME_PREFIX, title_second2, title_second2))
					break
			self.doubles.append('%s\n%s' % (a1, a2))
			self.titles_ru_doubles.append(p)

			title_no_diakritik = unidecode(title2)
			# self.post_wikipage(title2_no_diakritik, self.make_tpl_postpage(title_ru, title2, text))

			# if self.CLEAN_TEXT_FROM_POSTED:  self.clean_text_from_posted(header_and_text)

			if self.MAKE_REDIRECTS:
				redirect_new = pywikibot.Page(self.SITE, title2)
				redirect_new.set_redirect_target(self.PAGENAME_PREFIX + title_ru, create=True)
				# try:
				# 	posttext = r'#перенаправление [[%s/%s]]' % (self.PAGENAME_PREFIX, title_ru)
				# 	self.post_wikipage(header_and_text, title_second, posttext)
				# except:
				# 	print('No a redirect header in: ' + header)
				pass
			pass

		self.titles_ru.append(title_ru)

	def make_tpl_postpage(self, title_ru, title2, text):
		return "{{%s\n|НАЗВАНИЕ = %s\n|НАЗВАНИЕОРИГИНАЛА = %s\n|КАЧЕСТВО = 2\n|ВИКИПЕДИЯ = \n}}\n\n%s" % (
			self.PAGENAME_PREFIX, title_ru, title2, text)


	def post_wikipage(self, header, posttext):
		header_full = self.PAGENAME_PREFIX + '/' + header + self.PAGENAME_POSTFIX
		page_new = pywikibot.Page(self.SITE, header_full)

		if not page_new.exists():
			self.save_wikipage(page_new, posttext)
		elif page_new.exists():
			if self.REWRITE_EXIST_PAGES:
				self.log.add(header_full + ' : Is page')
				self.save_wikipage(page_new, posttext)
			if page_new.isRedirectPage():
				self.log.add(header_full + ' : IsRedirectPage')
				if self.REWRITE_REDIRECTS:
					self.save_wikipage(page_new, posttext)
		pass

	def clean_text_from_posted(self, header_and_text):
		# очистка текстовки от залитых статей
		self.textovka_text = self.textovka_text.replace(header_and_text, '')
		zalivka.log2file()
		pass

	def save_wikipage(self, page_obj, posttext):
		page_obj.text = posttext
		page_obj.save(self.SUMMARY)

	def log2wiki(self):
		# отметки и отчёты залитого
		self.textovka.text = self.textovki_texts
		self.textovka.save('залито')

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
Участник:Vladis13/lubker doubles
""".splitlines()
zalivka = zalivka_from_wikipage(TEXTOVKI_TITLES)
# zalivka.save_textovki_in_one_file(FI)
zalivka.get_section_titles()
# vladi_commons.file_savelines('/home/vladislav/workspace/temp/lubker/doubles_in_textoka', zalivka.titles_ru_doubles)
# vladi_commons.file_savelines('/home/vladislav/workspace/temp/lubker/doubles', zalivka.doubles)

if zalivka.CLEAN_TEXT_FROM_POSTED:
	zalivka.log2file()
# zalivka.log2wiki()
