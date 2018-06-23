# coding: utf-8
import re
import sys
# import roman
import vladi_commons

# from vladi_commons import *

page_title = False
if len(sys.argv) > 1:
	page_title = sys.argv[1]

# re_any_title = r'\n={2,}\s*([^=\n]+)\s*={2,} *\n'
# r = re.search(re_any_title + r'\n\n*(.*?)' + '((?:' + re_any_title + ')|$)', text, re.S)

# wikipages_filename = r'..\temp\AWBwikipage.txt'
# wikipages_filename = r'%TEMP%\AWBwikipage.txt'
# wikipages_filename = r'AWBwikipage.txt'
wikipages_filename = r'/tmp/AWBwikipage.txt'
text = vladi_commons.file_readtext(wikipages_filename)


# text = '''
# * {{tsds|РазДва|1. ДваТри (1-2)|1}}
# * {{tsds|ОдинДва||}}
# '''

# import mwparserfromhell  # не работает настраницах OCR ТСД, ибо там часто незакрытые тэги
# wikicode = mwparserfromhell.parse(text)

def capitalize_headers():
	# регистр букв заголовков в строчные
	import mwparserfromhell
	for header in wikicode.filter_headings():
		t = str(header.title).strip().capitalize()
		t = t.replace('i', 'I')
		t = t.replace('v', 'V')
		t = t.replace('x', 'X')
		header.title = ' ' + t + ' '


def tsd_pagenumber(izdanie, volume, pagenumber_scan):
	offset_of_volumes = [[2, -626, 1, 1], [90, 9, 8, 8], [17, 2, 2, 4]]
	i = izdanie - 1
	v = volume - 1
	if izdanie == 1 or izdanie == 2:
		page_number = str(int(pagenumber_scan) - offset_of_volumes[i][v])
	elif izdanie == 3:
		page_number = str((int(pagenumber_scan) - offset_of_volumes[i][v] - 1) * 2 + 1)
	return str(page_number)


def capitalize_parameters_tpl(wikicode):
	import mwparserfromhell  # не работает настраницах OCR ТСД, ибо там часто незакрытые тэги
	wikicode = mwparserfromhell.parse(text)
	par_parsing = re.compile(r'([\d\s.()]*)(.*)')
	for tpl in wikicode.filter_templates():
		if tpl.name.matches('tsds'):
			for i in range(1, 3):
				v = par_parsing.findall(str(tpl.get(i).value))
				tpl.get(i).value = v[0][0] + v[0][1].capitalize()


def convert(text):
	import requests
	r = requests.post("http://scripts.my/toDO/toDOraw.php", data={'text': text})
	conv_txt = r.text
	# коррекция слов, которые не надо конвертировать
	conv_txt = re.sub(r"(\n''\w+)ъ(\.'')", r"\1\2", conv_txt)  # ''Критъ.'', ''Сокръ.''
	# conv_txt = re.sub(r"\b([Сс]равн)ъ\.", r"\1.", conv_txt)   # сравнъ.
	return conv_txt


class TSD_OCR():
	def __init__(self, text_page):
		import re
		self.text_page = text_page
		self.sections_do = re.findall(r'<section begin="([^"]+(?:[^\d]| \d))"[ /]+>(.*?)<section end="\1"', text_page, re.DOTALL)
		self.sections_so = re.findall(r'<section begin="([^"]+[^ ]\d)"[ /]+>(.*?)<section end="\1"', text_page, re.DOTALL)
		self.converted_orf = ''

	def convert_so2do(self):
		# конвертация текста внутри секций
		for section in self.sections_so:
			conv_txt = convert(section[1])
			self.converted_orf = self.text_page.replace(section[1], conv_txt)

	def replace_words_in_DO(self, list_replace):
		for r in list_replace:
			self.converted_orf = self.text_page.sub(r[0], r[1])


#~ osr = TSD_OCR(text)
list_replace = [
['прилагъ.', 'прилаг.'],
['растеніе', 'растенье'],
['берѣзк', 'березк'],
['состояніе', 'состоянье'],
['положеніе', 'положенье'],
["[^']—мость[^']", "'''''—мость'''''"],
['ябѣд', 'ябед'],
['пегій', 'пѣгій'],
]
# title = ''
# for texta in wikicode.nodes:

# if hasattr(texta, 'title'):
# 	title_ = re.search(r'^\s*(\d+)\.?\s*$', str(texta.title))
# 	if title_:
# 		# if texta.value == '\n={2,}\s*([^=\n]+)\s*={2,} *\n'
# 		# 	title = texta.value
# 		title = str(title_.group(1))
# 	# print(texta.title)
# 	# print(type(texta))
# 	# print(str(texta))


# r = re.search(re_any_title + r'\n\n*(.*?)' + '((?:' + re_any_title + ')|$)', text, re.S)
# for p in r.groups():
# print(p)

# print(part)
# title = r.group(2)

# if re.search(r'^\d+\.?$', title):
# print(title)
# title = p.group(1).strip()

# section = mwparserfromhell.parse(p)
# title = str(section.heading()).strip()
# for part in section.filter_headings():
# 	title = str(part.title).strip()
# for texta in section.filter_text():
# 	print(texta)

#
# if hasattr(texta, 'value'):
# 	# print(texta.value)
# 	texta.value = re.sub(r'^(\d+)\. ', '{{стих|глава= %s|стих= %s|цвет=gray}} '    % (title, r'\1'), texta.value)
# 	texta.value = re.sub(r'\n(\d+)\. ', '\n{{стих|глава= %s|стих= %s|цвет=gray}} ' % (title, r'\1'), texta.value)
# 	texta.value = re.sub(r' (\d+)\. ', ' {{стих|глава= %s|стих= %s|цвет=gray}} '   % (title, r'\1'), texta.value)
# 	pass
#





pass
text = str(wikicode)
# print(str(wikicode))
# print(text)

vladi_commons.file_savetext(wikipages_filename, text)

# vladi_commons.file_savetext(wikipages_filename, 'll')
