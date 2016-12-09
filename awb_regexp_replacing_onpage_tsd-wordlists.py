# coding: utf-8
import re
import vladi_commons
import lib_for_mwparserfromhell
import mwparserfromhell

wikipages_filename = r'..\temp\AWBfile.txt'
text = vladi_commons.file_readtext(wikipages_filename)
wikicode = mwparserfromhell.parse(text)

for template in wikicode.filter_templates():
	if template.name.matches(('tsds', 'тсдс')):

		if template.has(3):
			template.remove(3)

			if template.has(4):
				p4 = template.get(4).value
				template.remove(4)
				template.add(3, p4)

			if template.has(5):
				p5 = template.get(5).value
				template.remove(5)
				template.add(4, p5)


pass

vladi_commons.file_savetext(wikipages_filename, str(wikicode))

