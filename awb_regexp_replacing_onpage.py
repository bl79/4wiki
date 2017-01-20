# coding: utf-8
import re
import sys
import vladi_commons
import mwparserfromhell

if len (sys.argv) > 1:
	page_title = sys.argv[1]
	
# re_any_title = r'\n={2,}\s*([^=\n]+)\s*={2,} *\n'
# r = re.search(re_any_title + r'\n\n*(.*?)' + '((?:' + re_any_title + ')|$)', text, re.S)
wikipages_filename = r'..\temp\AWBwikipage.txt'
text = vladi_commons.file_readtext(wikipages_filename)
# text = '''  '''
# wikicode = mwparserfromhell.parse(text)

# # регистр букв заголовков в строчные ------
# for header in wikicode.filter_headings():
	# t = str(header.title).strip().capitalize()
	# t = t.replace('i', 'I')
	# t = t.replace('v', 'V')
	# t = t.replace('x', 'X')
	# header.title = ' ' + t + ' '
# # ----------


if page_title:
	# text = 'k'
	pagenames = re.search(r'(^.+)/(.*?)$', page_title)
	if pagenames:	
		basepagename = pagenames.group(1)
		subpagename = pagenames.group(2)
		page_offset = 1
		to_page_number = str(int(subpagename) + page_offset)
		# text = re.sub(r'{{перенос сноски\|ref\s*}}', '{{перенос сноски|' + basepagename + '/'+ to_page_number+'}}', text)
		text = text.replace('{{перенос сноски|ref}}', '{{перенос сноски|' + basepagename + '/'+ to_page_number+'}}')

		# c2 = re.search(r"{{[Кк]олонтитул\s*\|[^|]*\|(?:''')?([^|]*?)\.?(?:''')?\|[^|]*}}", text).group(1)
		# if re.match('^\s*$', c2):
			# c2 = "''' — .'''"
		# colontitul = vladi_commons.wikicolontitul(
			# vladi_commons.label_interpages(page_pn, str(page_pn), ''),
			# c2,
			# vladi_commons.label_interpages('', str(page_pn), page_pn))
		

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
# print(str(wikicode))

# vladi_commons.file_savetext(wikipages_filename, str(wikicode))
vladi_commons.file_savetext(wikipages_filename, text)

