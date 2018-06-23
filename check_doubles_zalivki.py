#!/usr/bin/env python3
# coding: utf8
#
# author: https://github.com/vladiscripts
#
import re
import pywikibot
import vladi_commons
from unidecode import unidecode
from unicodedata import normalize

class replaces_on_wikipages():
	# LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки
	SITE = pywikibot.Site('ru', 'wikisource')
	# FI = '/home/vladislav/workspace/temp/bse1-5.txt'
	FI = '/home/vladislav/workspace/temp/lubker/list_diakritiks.txt'
	FO = FI + ' new'
	JSON_FILE = '/home/vladislav/workspace/temp/lubker/from_ancienhome2.json2'
	TEXTOVKA_FROM_FILE = 0
	PAGETITLES_FROM_FILE = 0
	REWRITE_EXIST_PAGES = None
	REWRITE_REDIRECTS = None
	CLEAN_TEXT_FROM_POSTED = None  # Не ясен смысл и алгоритм очистки текстовки от залитых
	MAKE_REDIRECTS = None
	PAGENAME_PREFIX = 'РСКД'
	# PAGENAME_PREFIX = 'БСЭ1'
	PAGENAME_POSTFIX = ''
	# SUMMARY = 'заливка'
	SUMMARY = '+др. редакция'
	textovki_texts = []
	titles = []
	all_sections = []
	log = set()  # already_exists_pages
	re_pagename_from_wikilink = re.compile(r'\[\[%s/(.*?)\s*(?:\||\]\])' % PAGENAME_PREFIX)
	sections_re = re.compile(r'''
					((?:\n|^)={2,}\s*(.*?)\s*={2,}\n[\n\s]*	# заголовок
					(.*?))		# текст секции
					(?=\n==|$)	# конец секции или страницы
					''', flags=re.DOTALL | re.VERBOSE)
	re_s = re.compile(r'\s*', flags=re.DOTALL)
	re_norazr = re.compile(r'\{\{razr2\|(.*?)\}\}', flags=re.DOTALL)

	# re_pagename_from_wikilink = re.compile(r'\[\[БСЭ1/(.*?)\s*(?:\||\]\])')

	def __init__(self, pages_titles):
		self.get_titles(pages_titles)
		# self.get_all_sections()

	def get_titles(self, pages_titles):
		if self.PAGETITLES_FROM_FILE == 1:
			self.titles = vladi_commons.file_readlines(self.FI)
		else:
			self.titles = [title for title in pages_titles]

	def check_pages_for_doubles(self):
		for i in self.all_sections:
			self.check_page_for_double(i['title'], i['text'])

	def check_page_for_double(self, title, text):
		title = 'РСКД/' + title
		page = pywikibot.Page(self.SITE, title)
		if not page.exists():
			print('not page: ' + title)
			posttext = '{{РСКД\n|КАЧЕСТВО = 2\n|ВИКИПЕДИЯ = \n}}\n\n%s' % text
			self.save_wikipage(page, posttext)

		elif page.isRedirectPage():
			print('redirect: ' + title)
			# title = page.getRedirectTarget()
			# page = pywikibot.Page(self.SITE, title)
			# page = page.getRedirectTarget()

		else:
			try:
				text_page = page.get()
				text1 = re.sub(r'\{\{РСКД.*?\}\}\s*', '', text_page, flags=re.DOTALL)
				text1 = text1.strip()
				text2 = text.strip()
				# print(title)
				if text1 == text2:
					# print(title)
					pass
				elif '{{неоднозначность}}' in text1:
					print('неоднозначность: ' + title)
				elif self.t_tosimple(text1) == self.t_tosimple(text2):
					posttext = re.sub(r'(\{\{РСКД.*?\}\}).+', r'\1\n\n%s' % text2, text_page, flags=re.DOTALL)
					self.save_wikipage(page, posttext)
				elif '{{РСКД/Викиредакция}}' not in text_page:
					posttext = re.sub(r'(\{\{РСКД.*?\}\})\s*(.*?)\s*', r'\1\n\n%s\n\n{{РСКД/Викиредакция}}\n\2' % text2, text_page, flags=re.DOTALL)
					self.save_wikipage(page, posttext)
				elif '{{РСКД/Викиредакция}}' in text_page:
					t1 = re.search(r'\{\{РСКД.*?\}\}\s*(.*?)\s*{{РСКД/Викиредакция}}', text_page, flags=re.DOTALL).group(1)
					t2 = re.search(r'{{РСКД/Викиредакция}}\s*(.+)\s*', text_page, flags=re.DOTALL).group(1)
					if self.t_tosimple(t1) == self.t_tosimple(t2):
						posttext = re.sub(r'(\{\{РСКД.*?\}\}).+', r'\1\n\n%s' % text2, text_page, flags=re.DOTALL)
						print('saved pages is eq, saved: ' + title)
						self.save_wikipage(page, posttext)
					else:
						pass
						# print('saved pages is not eq: ' + title)
				else:
					print('skipped: ' + title)

			except:
				print('regexp not found: ' + title)
				pass

	def t_tosimple(self, t):
		return self.re_s.sub(' ', self.re_norazr.sub(r'\1', t))

	def pages_replace(self):
		for title in self.titles:
			page = pywikibot.Page(self.SITE, title)

			if not page.exists():
				print('no page: ', title)
				continue
			elif page.exists():
				if page.isRedirectPage():
					# self.log.add('isRedirectPage: ', title)
					print('isRedirectPage: ', title)
					if self.REWRITE_REDIRECTS:
						posttext = self.page_replaces(page.get())
						self.save_wikipage(page, posttext)
				# elif self.REWRITE_EXIST_PAGES:
				else:
					print('is page: ', title)
					# self.log.add(title + ' : is page')
					posttext = self.page_replaces(page.get())
					self.save_wikipage(page, posttext)
			pass

	def page_replaces(self, text):
		t = normalize('NFD', text)
		t = t.replace('\uf008', '\u0301').replace('\uf014', '\u0313').replace('\uf00f', '\u0300')
		t = normalize('NFC', t)
		return t

	def save_textovki_in_one_file(self, filename):
		tt = '\n'.join(self.textovki_texts)
		vladi_commons.file_savetext(filename, tt)


	def get_wordlists(self):
		if self.TEXTOVKA_FROM_FILE == 1:
			self.textovki_texts = [vladi_commons.file_readtext(self.FI)]
		else:
			for textovka_title in self.titles:
				self.textovka = pywikibot.Page(self.SITE, textovka_title)
				self.textovki_texts.append(self.textovka.get())

	def get_all_sections(self):
		self.get_wordlists()
		sections_re = re.compile(r'''
			((?:\n|^)={2,}\s*(.*?)\s*={2,}\n[\n\s]*	# заголовок
			(.*?))		# текст секции
			(?=\n==|$)	# конец секции или страницы
			''', flags=re.DOTALL | re.VERBOSE)
		# for t in self.textovki_texts:
		# 	for p in sections_re.findall(t):
		# 		self.all_sections.append({'header_and_text': p[0], 'header': p[1], 'text': p[2]})
		self.all_sections = [{'header_and_text': p[0], 'header': p[1], 'text': p[2]} for t in self.textovki_texts for p in sections_re.findall(t)]
		# self.all_sections += [sections_re.findall(t) for t in self.textovki_texts]
		self.get_section_titles()

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
			header_and_text = section['header_and_text']
			text = section['text']
			header = section['header']
			h = re.search(r'# (.+)\s*', header)
			title1 = self.clean_header(h.group(1))
			title2 = self.clean_header(header)

			if re.search(r"^[A-Z]", title1, flags=re.I):
				title1 = unidecode(title1)  # remove diakritik
			section['title_second'] = title1
			section['title'] = title2

			# self.post_wikipage(title2, self.make_tpl_postpage(title1, title2, text))
			pass

			# self.find_doubles_titles(title_ru, title_second, text, header_and_text)


	def save_wikipage(self, page_obj, posttext):
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
Участник:Vladis13/lubker ancrome2
Участник:Vladis13/lubker ancrome3
Участник:Vladis13/lubker ancrome4
Участник:Vladis13/lubker ancrome5
""".splitlines()
pages = replaces_on_wikipages(TEXTOVKI_TITLES)
# dic = vladi_commons.json_data_from_file(self.JSON_FILE)
pages.get_all_sections()
pages.check_pages_for_doubles()
# pages.pages_replace()
# pages.save_textovki_in_one_file(FI)
# pages.get_section_titles()
# vladi_commons.file_savelines('/home/vladislav/workspace/temp/lubker/doubles_in_textoka', zalivka.titles_ru_doubles)
# vladi_commons.file_savelines('/home/vladislav/workspace/temp/lubker/doubles', zalivka.doubles)

if pages.CLEAN_TEXT_FROM_POSTED:
	pages.log2file()
# pages.log2wiki()
