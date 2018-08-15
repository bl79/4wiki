# -*- coding: utf-8 -*-
t = """
<section begin="Байка 1" />{{выступ|'''Ба{{акут}}йка,''' отъ гл. ''байкать,'' см. ''{{tsdl|Баить|баю{{акут}}кать}}'' отъ гл. ''{{tsdl|баить}}'', см. это сл. }}<section end="Байка 1" />

<section begin="Байка 2" />{{выступ|'''Ба{{акут}}йка''' <small>ж. англ.</small> мягкая, толстая, очень ворсистая шерстяная ткань. {{gb|Ба{{акут}}йковый}} <small>или</small> {{gb|ба{{акут}}йчатый}} ''сюртукъ. Байковая фабрика.'' {{gb|Ба{{акут}}йковый язы{{акут}}къ}} <small>(отъ ''байки,'' суконный, картавый? или отъ гл. ''баить?)'' или</small> му{{акут}}зыка, вымышленный, малословный языкъ столичныхъ мазуриковъ, воровъ и карманниковъ, нѣчто въ родѣ {{tsdl|Афеня|афенскаго}}; есть дажѣ нѣсколько словъ общихъ, <small>напр. ''ле{{акут}}пень,'' платокъ; но б. ч. придуманы свои: ''бутырь,'' городовой; ''фарао{{акут}}нъ,'' буточникъ; ''стуканцы, веснухи,'' часы; ''сламейка,'' лошадь; ''ходить по музыкѣ,'' говорить байковымъ языкомъ; ''подна{{акут}}чить, захороводить,'' подкупить прислугу; ''переты{{акут}}рить вещь,'' передать наскоро; ''стре{{акут}}ма,'' опасность; ''камышевка,'' ломъ; ''голуби,'' бѣлье на чердакѣ; ''мѣшокъ,'' скупщикъ краденаго и пр.</small>}}{{tsdbr}}<section end="Байка 2" />

<section begin="Байкалит" />{{выступ|'''Байкали{{акут}}тъ ''' <small>м.</small> каменная порода, ископаемое, открытое на Байкалѣ.}} {{tsdbr}}<section end="Байкалит" />

<section begin="Байна" />{{выступ|'''Ба{{акут}}йна,''' {{gb|ба{{акут}}йня}} см. ''{{tsdl|Баня|ба{{акут}}ня}}''.}}{{tsdbr}}<section end="Байна" />
 
<section begin="Байрак" />{{выступ|'''Байра{{акут}}къ''' см. ''{{tsdl|Буерак|буеракъ}}''.}}{{tsdbr}}<section end="Байрак" />

{{свр}}

<section begin="Байка 1-1" />{{выступ|'''Ба{{акут}}йка,''' от гл. ''байкать,'' см. ''{{tsdl|Баить|баю{{акут}}кать|so}}'' от гл. ''{{tsdl|баить}}'', см. это сл. }}<section end="Байка 1-1" />

<section begin="Байка 2-1" />{{выступ|'''Ба{{акут}}йка''' <small>ж. англ.</small> мягкая, толстая, очень ворсистая шерстяная ткань. {{gb|Ба{{акут}}йковый}} <small>или</small> {{gb|ба{{акут}}йчатый}} ''сюртук. Байковая фабрика.'' {{gb|Ба{{акут}}йковый язы{{акут}}к}} <small>(от ''байки,'' суконный, картавый? или от гл. ''баить?)'' или</small> му{{акут}}зыка, вымышленный, малословный язык столичных мазуриков, воров и карманников, нечто в роде {{tsdl|Афеня|афенского|so}}; есть даже несколько слов общих, <small>напр. ''ле{{акут}}пень,'' платок; но б. ч. придуманы свои: ''бутырь,'' городовой; ''фарао{{акут}}н,'' буточник; ''стуканцы, веснухи,'' часы; ''сламейка,'' лошадь; ''ходить по музыке,'' говорить байковым языком; ''подна{{акут}}чить, захороводить,'' подкупить прислугу; ''переты{{акут}}рить вещь,'' передать наскоро; ''стре{{акут}}ма,'' опасность; ''камышевка,'' лом; ''голуби,'' белье на чердаке; ''мешок,'' скупщик краденого и пр.</small>}}{{tsdbr}}<section end="Байка 2-1" />

<section begin="Байкалит1" />{{выступ|'''Байкали{{акут}}т ''' <small>м.</small> каменная порода, ископаемое, открытое на Байкале.}} {{tsdbr}}<section end="Байкалит1" />

<section begin="Байна1" />{{выступ|'''Ба{{акут}}йна,''' {{gb|ба{{акут}}йня}} см. ''{{tsdl|Баня|ба{{акут}}ня|so}}''.}}{{tsdbr}}<section end="Байна1" />
 
<section begin="Байрак1" />{{выступ|'''Байра{{акут}}к''' см. ''{{tsdl|Буерак|буерак|so}}''.}}{{tsdbr}}<section end="Байрак1" />
"""

import re
import vladi_commons
import pywikibot
import mwparserfromhell as mwp
from my_wikisource_class.wikiclass import WikiMethods


class wiki(WikiMethods):
	# LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки
	EDITION = 3
	SITE = pywikibot.Site('ru', 'wikisource')
	FI = '/home/vladislav/var/tsd%s_worlists.txt' % EDITION
	FO = FI + '_pages_to_rename'
	FI_pagelist = '/home/vladislav/var/tsd%s_doubles_tagpages.txt' % EDITION
	FO_pagelist = FI_pagelist + '_pages_to_rename'
	TEXTOVKA_FROM_FILE = 0  # or from wikipage
	PAGELIST_FROM_FILE = 1  # or from wikipage
	REWRITE_EXIST_PAGES = None
	CLEAN_TEXT_FROM_POSTED = None  # Не ясен смысл и алгоритм очистки текстовки от залитых
	MAKE_REDIRECTS = None
	PAGENAME_PREFIX = 'ТСД%s' % EDITION
	PAGENAME_POSTFIX = ''
	SUMMARY = 'заливка'
	wordlists_text = []
	lat_redirects = []
	list2rename = []
	wordlist_title = ''
	wordlist_text = ''
	page = ''  # pywikibot object
	page_wikicode = ''  # mwp object
	pagename = ''
	cur_article_name = ''
	pagelists_titles = ''
	pagelist = ''
	log = set()  # already_exists_pages
	re_pagename_from_wikilink = re.compile(r'\[\[%s/(.*?)\s*(?:\||\]\])' % PAGENAME_PREFIX)

	def __init__(self, *args):
		super().__init__()
		self.PAGELIST_TITLES = vladi_commons.str2list(args[0])
		self.get_pagelists()
		# self.parse_wordlist()
		# self.operate_wordlist_pagelinks()

		# for TEXTOVKA_TITLE in vladi_commons.lines2list(self.WORDLIST_TITLES):
		# if self.TEXTOVKA_FROM_FILE == 1:
		# 	self.get_text_of_wordlists()
		# self.get_text_of_wordlist()
		for pagename in self.pagelists_titles:
			self.page_data = self.open_page(pagename)
			if self.page_data:
				self.parse_page(self.page_data['obj'])
				self.page_find_doubles_tag_pages()

	def page_find_doubles_tag_pages(self):
		wikicode = self.page_data['wikicode']
		page_obj = self.page_data['obj']
		pagename = self.page_data['pagename']
		pagestags = self.get_pagestags(wikicode)
		if len(pagestags) > 1:
			# обрабатывать только трансклюзии с одной страницы скана, для простоты
			if len(pagestags) == 2:
				# if pagestags[0].get('from').value == pagestags[1].get('from').value \
				# 		and pagestags[0].get('to').value == pagestags[1].get('to').value:
				if True:
					# sectionname_new = self.tsd_section_name(self.cur_article_name, pagename)
					self.sectionname_new = self.tsd_section_name(pagename)
					if self.scanpage_add_section_for_double_terms(pagestags) is True:
						# замена двух тегов pages на один
						pagestags[0].get('onlysection').value = self.sectionname_new
						pagestags[0].get('to').value = pagestags[1].get('to').value
						wikicode.remove(pagestags[1])
						# удаление категории
						for link in wikicode.filter_external_links():
							catname = link.name
						text = re.sub(r'\n?\[\[Категория:ТСД:двойные pages.*?\]\]', '', str(wikicode))
						text = text + '\n[[Категория:ТСД:Проверить секции в трансклюзии]]'
						page_obj.text = text
						page_obj.save('tags <pages>: combined to one section')
				else:
					pass
			elif len(pagestags) == 3:
				# if pagestags[0].get('from').value == pagestags[1].get('from').value \
				# 		and pagestags[0].get('from').value == pagestags[2].get('from').value \
				# 		and pagestags[0].get('to').value == pagestags[1].get('to').value \
				# 		and pagestags[0].get('to').value == pagestags[2].get('to').value:
				if True:
					# sectionname_new = self.tsd_section_name(self.cur_article_name, pagename)
					self.sectionname_new = self.tsd_section_name(pagename)
					if self.scanpage_add_section_for_double_terms(pagestags) is True:
						# замена двух тегов pages на один
						pagestags[0].get('onlysection').value = self.sectionname_new
						wikicode.remove(pagestags[1])
						wikicode.remove(pagestags[2])
						# удаление категории
						# for link in wikicode.filter_external_links():
						# 	catname = link.name
						text = re.sub(r'\n?\[\[Категория:ТСД:двойные pages.*?\]\]', '', str(wikicode))
						page_obj.text = text
						page_obj.save('tags <pages>: combined to one section')
				else:
					pass
			elif len(pagestags) == 4:
				# if pagestags[0].get('from').value == pagestags[1].get('from').value \
				# 		and pagestags[0].get('from').value == pagestags[2].get('from').value \
				# 		and pagestags[0].get('from').value == pagestags[3].get('from').value \
				# 		and pagestags[0].get('to').value == pagestags[1].get('to').value \
				# 		and pagestags[0].get('to').value == pagestags[2].get('to').value \
				# 		and pagestags[0].get('to').value == pagestags[3].get('to').value:
				if True:
					# sectionname_new = self.tsd_section_name(self.cur_article_name, pagename)
					self.sectionname_new = self.tsd_section_name(pagename)
					if self.scanpage_add_section_for_double_terms(pagestags) is True:
						# замена двух тегов pages на один
						pagestags[0].get('onlysection').value = self.sectionname_new
						wikicode.remove(pagestags[1])
						wikicode.remove(pagestags[2])
						wikicode.remove(pagestags[3])
						# удаление категории
						# for link in wikicode.filter_external_links():
						# 	catname = link.name
						text = re.sub(r'\n?\[\[Категория:ТСД:двойные pages.*?\]\]', '', str(wikicode))
						text = text + '\n[[Категория:ТСД:Проверить секции в трансклюзии]]'
						page_obj.text = text
						page_obj.save('tags <pages>: combined to one section')
				else:
					pass
			else:
				print('%s: too much tags <pages>' % self.page_data['pagename'])

	def scanpage_add_section_for_double_terms(self, tagpages):
		"""обработка секций только с одной страницы индекса
		(чистка простых случаев для первич.обработки)
		"""
		written = False
		ipages = {int(str(tagpages[0].get('from').value))}
		ipages.update(int(str(tagpages[i].get('to').value)) for i, tag in enumerate(tagpages))
		pagesnum = [i for i in range(min(ipages), max(ipages)+1)]
		for i, pn in enumerate(ipages):
			scanpage_name = 'Страница:%s/%s' % (tagpages[0].get('index').value, str(pagesnum[i]))
			scanpage = pywikibot.Page(self.SITE, scanpage_name)
			scanpage_wikicode = mwp.parse(scanpage.text)

			# проверка, что нового названия секции уже нет на странице
			for tag in scanpage_wikicode.filter_tags():
				if tag.tag.matches('section') and tag.has('begin'):
					if tag.get('begin').value == self.sectionname_new:
						print('%s: секция одноимённая названию страницы уже есть на странице скана' % self.page_data[
							'pagename'])
						# return False
						self.sectionname_new = '(омонимы) ' + self.sectionname_new
						break

			# добавление секции
			t = scanpage.text
			t = re.sub(r'(<section\s+begin\s*=\s*[\'"]%s[\'"][ /]*>)' % str(tagpages[0].get('onlysection').value),
					   r'<section begin="%s" />\1' % self.sectionname_new, t)
			t = re.sub(r"(<section\s+end\s*=\s*[\'\"]%s[\'\"][ /]*>)" % tagpages[len(tagpages) - 1].get('onlysection').value,
				r'\1<section end="%s" />' % self.sectionname_new, t)
			scanpage.text = t
			scanpage.save(summary='+section for the double terms')
			written = True
		if written:
			return True


TEXTOVKI_TITLES = """
ТСД-словник/2/А
"""
wordlist_links = wiki(TEXTOVKI_TITLES)
wordlist_links.savelist2rename('pages2rename2.txt')
