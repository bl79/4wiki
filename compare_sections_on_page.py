import re
import pywikibot
import vladi_commons

LISTPAGES_FILENAME = 'listpages.txt'  # список страниц для обработки

SITE = pywikibot.Site('ru', 'wikisource')
listpages = set(vladi_commons.file_readlines(LISTPAGES_FILENAME))
pages1 = []
pages2 = []

for page_title in listpages:
	page_title = re.search('\[\[:(.*?)\]\]', page_title).group(1)
	page = pywikibot.Page(SITE, page_title)
	wikipage = page.get()

	section1_re = re.compile(r'''\{\{БСЭ1.*?\}\}[\n\s]*(.*?)[\n\s]*\n==''', flags=re.DOTALL)
	section2_re = re.compile(r'\n==\s*В другой.*?==\n[\n\s]*(.*?)[\n\s]*$', flags=re.DOTALL)

	pages1.append(section1_re.search(wikipage).group(1))
	pages2.append(section2_re.search(wikipage).group(1))
	pass

wikipages_section1 = 'wikipages_section1.txt'
wikipages_section2 = 'wikipages_section2.txt'
vladi_commons.file_savelines(wikipages_section1, pages1)
vladi_commons.file_savelines(wikipages_section2, pages2)
