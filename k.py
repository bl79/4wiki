# -*- coding: utf-8  -*-
# coding: utf8
import re
import mwparserfromhell

text = """
{{sub template}}
{{tpl_name}}
{{tpl-pnum|jj|555|kk}}
llll
{{tpl_name | {{sub template}} some text| y = iiiii| [[link|text]]   | [[CITEREF1_sfn_.D1.81.D0.BD.D0.BE.D1.81.D0.BA.D0.B0 | uuu]]  [[вторая викиссылка в параметре | ннннннн]]}}
text
"""
# title = 'Участник:Vladis13/статья'	

# print(text)
# print('----------------------------------------  ^^^ original text \n')

refs = [
	{
		'citeref':         "CITEREF1_sfn_.D1.81.D0.BD.D0.BE.D1.81.D0.BA.D0.B0",
		"link_to_sfn": "cite_note-2",
		"text":        "1 sfn сноска"
	},
	{'citeref':         "CITEREF2_sfn_.D1.81.D0.BD.D0.BE.D1.81.D0.BA.D0.B0",
	 "link_to_sfn": "cite_note-2",
	 "text":        "2 sfn сноска"
	 }
]



list_sfn_links = set([ref['link_to_sfn'] for ref in refs])
print(list_sfn_links)

wikicode = mwparserfromhell.parse(text)

tplname = 'tpl_name'
# tplname = 'tpl-pnum'
digits = re.compile(r'\d+')
# wikicode.remove('tpl_name')

for tpl in wikicode.filter_templates():
	if tpl.name.matches(tplname):

		# pvalueslist = set()
		for p in tpl.params:
			if digits.search(str(p.name).strip()):
				# tpl.remove(p.name)
				wikilink = p.value.filter_wikilinks()
				if len(wikilink):
					wikilink = wikilink[0]
					print(wikilink)
				# for wikilink in p.value.filter_wikilinks():
					# print(wikilink)
					wlref = str(wikilink.title).strip()
					print(wlref)
					# for ref in refs:
						# print(ref)
						# print(ref['link_to_sfn'])
						# if wlref == ref['link_to_sfn']:
							# print('строка найдена')


# pvalueslist.add(p.value.strip())
# print(type(value))
# print(value)

# for p in pvalueslist:
# 	for wikilink in p.filter_wikilinks():
# 		print(wikilink)


print('-----------')


# Удаление пустого шаблона (без параметров)
for tpl in wikicode.filter_templates():
	if tpl.name.matches(tplname):
		c = 0
		print(tpl.name)
		print("число всех параметров: " + str(len(tpl.params)))
		for p in tpl.params:
			print("параметр имя: " + str(p.name) + ", параметр значение: " + str(p.value))
			if digits.search(str(p.name).strip()):
				print("параметр с цифрой: " + str(p.name))
				c += 1
				# print("1: " + str(c))
		print("число нумерованных параметров: " + str(c))
		if c == 0:
			wikicode.remove(tpl)
# print('empty')
# print(c)

tpl = mwparserfromhell.nodes.template.Template(tplname)
wikicode.append(tpl)

# tpl.add('TplUrlParameter', 'link.url')

text = str(wikicode)
# print(str(pvalueslist))
print(str(wikicode))
