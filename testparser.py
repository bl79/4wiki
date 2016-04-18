# -*- coding: utf-8  -*-
import mwparserfromhell
import pywikibot

# file = r'd:\home\scripts.my\wiki-xml'

text = u''' эстрадного или циркового {{nobr|uu=6|r}}представления, [[фильм]]а<ref name="encycl">{{статья
 |автор         = Рудницкий К. Л. 
 |заглавие      = Режиссёрское искусство
 |ссылка        = http://slovari.yandex.ru/~книги/БСЭ/Режиссёрское%20искусство/
 |язык          = 
 |издание       = БСЭ
 |тип           = 
 |место         = М.
 |издательство  = Советская энциклопедия
 |год           = 
 |том           = 
}}</ref>.'''

print (text)
code = mwparserfromhell.parse(text)
print(code)

templates = code.filter_templates()
print(templates)

template = templates[0]
print(template.name)

for template in code.filter_templates():
	if template.name.matches("статья") and not template.has("date"):
		template.add("date", "July 2012")
		
		# code.replace(template, "{{bar-stub}}")
	
print(code)


def parse(title):
    site = pywikibot.Site()
    page = pywikibot.Page(site, title)
    text = page.get()
    return mwparserfromhell.parse(text)
	
    if textfile and not addText:
        with codecs.open(textfile, 'r', config.textfile_encoding) as f:
            addText = f.read()
