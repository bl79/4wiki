# -*- coding: utf-8  -*-
import sys
# import pywikibot
import mwparserfromhell
from my import *



filename = r'd:/home/scripts.my/AWBfile.txt'
f = open(filename, 'r', encoding='utf-8')
text = f.read()
f.close()

# text = r'''* {{Из|БСЭ|http://slovari.yandex.ru/Дербент/БСЭ/Дербент/|заглавие=Дербент}}
# '''

ParametersToRemove = (	'место', 'издательство', 'язык', 'тип', 'год', 'ответственные',	'publisher', 	'archiveurl', 'archivedate','accessdate'	)

link2remove = r'https?://(?:www\.)?slovari\.yandex\.ru/[^|\s]*(БСЭ|%D0%91%D0%A1%D0%AD|dict/bse)/'
renameTemplateTo = 'БСЭ3'

code = mwparserfromhell.parse(text)
# print(code)
for template in code.filter_templates():
	print(template)
	if template.name.matches(('статья', 'книга', 'публикация', 'cite web', 'cite news', 'из', 'Из БСЭ')):		

		# if template.name.matches('Из') and template.get(1).value == 'БСЭ':
			# # if template.has('заглавие'):
			# if template.has(3):
				# if not re.match('^\s*$', str(template.get(3).value)):
					# template.add('заглавие', str(template.get(3).value))
					# template.remove(3)
				# else:
					# template.remove(3)
			# if not template.has(3) and not template.has('заглавие'):
				# if template.has('title'):
					# renameParam(template, 'title', 'заглавие')
				# else: template.add('заглавие', sys.argv[1])

			# if template.has(2):
				# template.add('ссылка', str(template.get(2).value))
				# template.remove(2)

			# template.remove(1)
			# removeTplParameters(template, 'издание')
			# # renameParam(template, 'заглавие', 'статья')
			# template.name = renameTemplateTo
			# removeTplParametersExceptThis(template, ('автор', 'заглавие', 'статья', 'том', 'страницы', 'ref', 'ссылка', 'archiveurl', 'archivedate'))
			# findAndDeleteLink(template, link2remove)
			# deleteEmptyParam(template, ('автор', 'том', 'страницы', 'ссылка'))
			# removeSpacesBreaks(template)


		if template.name.matches('Из БСЭ'):
			# переделка 'Из БСЭ' → в БСЭ3			
			# if template.has(1):
				# template.add('ссылка', str(template.get(1).value))
				# template.remove(1)
				# findAndDeleteLink(template, link2remove)
				# deleteEmptyParam(template, ('ссылка',))
			# if template.has('title') or template.has('заглавие'):
				# renameParam(template, 'title', 'заглавие')
			# else:
				# if template.has(2):
					# if not re.match('^\s*$', str(template.get(2).value)):   # не пустой параметр
						# template.add('заглавие', str(template.get(2).value))
						# template.remove(2)
					# else: # пустой параметр, назвать по названию страницы
						# template.add('заглавие', sys.argv[1])
						# template.remove(2)
				# else:
					# template.add('заглавие', sys.argv[1])
			# # print(template)	

			# просто чистка и парсинг url в 'Из БСЭ'
			pagenameFromLink = r'/(?:БСЭ|%D0%91%D0%A1%D0%AD|dict/bse)(?:/[^]/}]*)?/(?:\d+/\d+\.htm\?text=)?([^]/}]+)'
			deleteEmptyParam(template, (1, 2, 'title', 'заглавие'))
			if template.has('title') or template.has('заглавие') or template.has(2):				
				renamedTitle = False
				if template.has('title'):
					renamedTitle = True
					renameParam(template, 'title', 'заглавие')						
				if template.has(2) and not template.has('заглавие'):	# переименовать
					template.get(2).name = 'заглавие'
				if renamedTitle == True: # переименовать title как было, чтобы небыло вопросов, и не надо было отвечать
					renameParam(template, 'заглавие', 'title')
					renamedTitle = False								
			else:
				paramValueFromLinkOrPagename(template, 'заглавие', 1, pagenameFromLink, True)	
										
			if template.has(1) or template.has('ссылка') or template.has('url'):
				findAndDeleteLink(template, link2remove, (1,))
				deleteEmptyParam(template, (1, 'ссылка', 'url'))
				

		# elif template.name.matches('статья') or \
				# (template.name.matches('публикация') and template.get(1).value == 'статья'):
			# if not findAndDeleteLink(template, link2remove): continue
			# renameParam(template, 'заглавие', 'статья')

		# elif template.name.matches(['книга', 'публикация']):
			# if not findAndDeleteLink(template, link2remove): continue
			# renameParam(template, 'часть', 'статья')

		# elif not template.name.matches(['cite web', 'cite news']):
			# if findAndDeleteLink(template, link2remove): continue
			# renameParam(template, 'author', 'автор')
			# renameParam(template, 'title', 'статья')

		

			# template.name = renameTemplateTo
			# removeTplParameters(template, ParametersToRemove)
			replaceParamValue(template, 'автор', '\s{2,}', ' ')
			replaceParamValue(template, 'статья', '\s*— БСЭ — Яндекс.Словари', '')
			replaceParamValue(template, 'статья', '\s*// Большая советская энциклопедия', '')
			replaceParamValue(template, 'статья', '\s*в Большой Советской Энциклопедии', '')
			replaceParamValue(template, 'том', '\s*(\d+).*', r'\1')
			# removeTplParametersExceptThis(template, ('автор', 'статья', 'заглавие', 'том', 'страницы', 'ref', \
				# 'ссылка', \
				# 'archiveurl', 'archivedate', \
				# 'add quotes', 'кавычки', 'издание', 'title')) # {{Из БСЭ}}
			deleteEmptyParam(template, ('автор', 'том', 'страницы', 'ссылка'))
			deleteParamArhiveurlDateIfWebarchive(template)
			removeSpacesBreaks(template)
		
		
		# else: continue
			
	# r'<ref[^>]>[https?://(?:www\.)?slovari\.yandex\.ru/[^|\s]*(БСЭ|%D0%91%D0%A1%D0%AD|dict/bse)/ [^]]*]</ref>'		r'<ref[^>]>https?://(?:www\.)?slovari\.yandex\.ru/[^|\s]*(БСЭ|%D0%91%D0%A1%D0%AD|dict/bse)/</ref>'
	# {{БСЭ3|статья=  }}


# for param in sys.argv:
        # code = param
# print(str(code))
# print(9)

f = open(filename, 'w', encoding='utf-8')
f.write(str(code))
f.close()
