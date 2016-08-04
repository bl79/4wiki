# -*- coding: utf-8  -*-
import mwparserfromhell
# import pywikibot
# from pywikibot import pagegenerators
from my import *

category_bad_sfn = '[[Категория:Имеются нерабочие якоря в сносках]]'

# def parse(title):
# 	site = pywikibot.Site()
# 	page = pywikibot.Page(site, title)
# 	text = page.get()
# 	return mwparserfromhell.parse(text)

path2script = r"d:\home\scripts.my\4wiki\\"
filename = path2script + r'sfn1.txt'

# f = open(filename, 'r', encoding='utf-8')
# text = f.read()
# f.close()


# f = open(filename, 'r', encoding='utf-8')
# t = f.readlines()
# t = [line.rstrip() for line in t]
arr_listpages = [line.rstrip() for line in open(filename, encoding='utf-8')]
# print (t)
# print(t, end='')
# for line in f.readlines():
    # print (line)


list_tpls = ('sfn', 'sfn0')
	
for pagecontent in arr_listpages:

	# pagecontent = "hhhh{{sfn|refname1|2016|loc=comment}}" \
	# 			  "" \
	# 			  "" \
	# 			  "hhjgh {{книга|заглавие=ннн| ref = refname }}" \
	# 			  "hhhh{{sfn|refname2|2015|loc=comment}}" \
	# 			  "" \
	# 			  "" \
	# 			  "hhjgh {{книга|заглавие=ннн|год=2015| ref = refnamefalse}}"
	pagecontent = "hhjg{{sfn|refname1|2016|loc=comment}}" \
				  "" \
				  "" \
				  "hhjgh {{книга|заглавие=ннн|год=2016| ref = refname1 }}" \
				  "hhhh{{sfn|refname2|2015|loc=comment}}" \
				  "" \
				  "" \
				  "hhjgh {{книга|год=2015|заглавие=ннн| ref = refname2}}"



	# print(p)
	# print(parse(p))	
	# code = parse(pagecontent)
	code = mwparserfromhell.parse(pagecontent)
	list_refs = []
	list_sfns = []
	for template in code.filter_templates():
		if template.has('ref'):
			refs = []
			refs.append(template.get('ref').value.strip())
			for year in ['год', 'year']:
				if template.has(year):
					refs.append(template.get(year).value.strip())
			list_refs.append(refs)

			# refcount = 1
			# tpl_year =

		if template.name.matches('sfn'):
			if template.has('1'):
				sfns = []
				sfns.append(template.get('1').value.strip())
				if template.has('2'):
					sfns.append(template.get('2').value.strip())
			# else:
			# 	print ('sfn has not parameters')
				list_sfns.append(sfns)

	if list_refs != list_sfns:
		print('sfn has not parameters')
	# print('list_refs:')
	# print(list_refs)
	# print('list_sfns:')
	# print(list_sfns)
		# for sfn in list_sfns:
		# 	for ref in list_refs:
		# 		if sfn[0] != ref[0]:  continue
		# 		else
		# 		if sfn[1] == ref[1]:
		# 				continue
		# 		else

				# for template in code.filter_templates():
					# arr = []  # list of refs
					# if template.has('ref'):
						# arr.append(str(template.get('ref').value))

						# setarr = set(arr)
						# if len(arr) != len(setarr):
							# print("Есть одинаковые")
						# # else:	print("Все элементы уникальны")

			# text = str(code)


		# print(text)



# tpl = 'Sfn'
tpl = 'Вершины Каменного Пояса'
# list = pywikibot.pagegenerators.GeneratorFactory(u'-transcludes:' + tpl)
# list = str(pagegenerators.GeneratorFactory(u'-transcludes:' + tpl))
args = (u'-transcludes:' + tpl,)
# local_args = pywikibot.handle_args(u'-transcludes:Sfn',)
# list = pagegenerators.GeneratorFactory.handleArg(local_args)
# gen = pagegenerators.GeneratorFactory()
# list = gen(u'-transcludes:Sfn').getCombinedGenerator()

# list = pywikibot.pagegenerators.MySQLPageGenerator('SELECT page_namespace, page_title FROM page JOIN templatelinks ON tl_from = page_id WHERE tl_namespace = 10 AND tl_title = "Sfn" AND page_namespace = 0')
# list = pywikibot.pagegenerators.MySQLPageGenerator('SELECT page_namespace, page_title FROM page LIMIT 10')

query = 'SELECT * FROM page LIMIT 10'

# genFactory = GeneratorFactory()
# gen = genFactory.getCombinedGenerator()

# list = pywikibot.pagegenerators.MySQLPageGenerator(query)
# for i in list:
	# print(i)

	
# import os, sys
# sys.stdout = open("t.txt", 'w')
# os.system('python c:\pwb\pwb.py listpages.py -ns:0 -transcludes:"{}" -format:3 -lang:ru -family:wikipedia'.format(tpl)) 


# from wmflabs import db
# conn = db.connect('enwiki')  # You can also use "enwiki_p"
# # conn is a oursql.connection object.
# with conn.cursor() as cur:
    # cur.execute(query)  # Or something....
	
	
	


# commands = [
	# r'python c:\pwb\pwb.py listpages.py -transcludes:"{tpl}"', tpl,
# ]
# for command in commands:
	# os.system(command)
	# for cats in CategoriesToRename:
		# from_ = ' -from:"' + cats[0] + '"'
		# to_ = ' -to:"' + cats[1] + '"'
		# summary_ = ' -summary:"' + summary + '"'
		# run = command + from_ + to_ + summary_  # + ' -simulate'
		# print('echo ' + run)
		# os.system(run)
	

# from wmflabs import db
# conn = db.connect('enwiki')  # You can also use "enwiki_p"
# # conn is a oursql.connection object.
# with conn.cursor() as cur:
    # cur.execute(query)  # Or something....

    # return oursql.connect(db=dbname + '_p',
                          # host=host,
                          # read_default_file=os.path.expanduser("~/replica.my.cnf"),
                          # charset=None,
                          # use_unicode=False,
                          # )
# host = 'enwiki' + ".labsdb"  # 'localhost'   'ruwiki.labsdb'
# host = 'tools-login.wmflabs.org'   # 'localhost'   'ruwiki.labsdb'
# user='vladi2016'  # 'textworkerBot'
# password = 'goreibeda'
# # password = 'vladidengi'
# db = 'ruwiki_p'	
# user='u14134'  # 'textworkerBot'
# charset='utf8'
	
# import pymysql
# import pymysql.cursors
# conn= pymysql.connect(host,user,password,db,charset,cursorclass=pymysql.cursors.DictCursor)
# a=conn.cursor()
# a.execute(query)	
	
	
# print (text)

# import sys
# import mwparserfromhell
# from my import *

# filename = r'../temp/AWBfile.txt'
# f = open(filename, 'r', encoding='utf-8')
# text = f.read()
# f.close()

# # text = r'''* {{Из|БСЭ|http://slovari.yandex.ru/Дербент/БСЭ/Дербент/|заглавие=Дербент}}
# # '''

# ParametersToRemove = (
	# 'место', 'издательство', 'язык', 'тип', 'год', 'ответственные', 'publisher', 'archiveurl', 'archivedate',
	# 'accessdate')

# dics = [
	# {
		# 'renameTemplateTo': 'Книга:Городские имена сегодня и вчера|1997|заглавие=',
		# 'urlPartWithPagename': r'Петербургская%20топонимика|%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D1%81%D0%BA%D0%B0%D1%8F%20%D1%82%D0%BE%D0%BF%D0%BE%D0%BD%D0%B8%D0%BC%D0%B8%D0%BA%D0%B0',
		# 'addSignature': r'|dict/petertoponim',
		# 'paramTitle': 'заглавие',
		# 'paramAuthor': '',
	# },
	# {
		# 'renameTemplateTo': 'Книга:Энциклопедия «Москва» 1997',
		# 'urlPartWithPagename': r'Энциклопедия%20«Москва»|%D0%AD%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F%20%C2%AB%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%C2%BB|Энциклопедия%20%C2%ABМосква%C2%BB',
		# 'addSignature': r'|dict/mos',
		# 'paramTitle': '1',
		# 'paramAuthor': 'автор',
	# },
	# {
		# 'renameTemplateTo': 'Имена московских улиц',
		# 'urlPartWithPagename': r'Московские%20улицы|%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B5%20%D1%83%D0%BB%D0%B8%D1%86%D1%8B',
		# 'addSignature': r'|dict/mostoponim',
		# 'paramTitle': '1',
		# 'paramAuthor': 'автор',
	# },
	# {
		# 'renameTemplateTo': 'Из БОЭ',
		# 'urlPartWithPagename': r'Олимпийская%20энциклопедия|%D0%9E%D0%BB%D0%B8%D0%BC%D0%BF%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F%20%D1%8D%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F',
		# 'addSignature': r'|dict/olympic',
		# 'paramTitle': 'title',
		# 'paramAuthor': 'автор',
	# },
	# {
		# 'renameTemplateTo': 'Революционеры',
		# 'urlPartWithPagename': r'Революционеры|%D0%A0%D0%B5%D0%B2%D0%BE%D0%BB%D1%8E%D1%86%D0%B8%D0%BE%D0%BD%D0%B5%D1%80%D1%8B',
		# 'addSignature': r'|dict/revoluc',
		# 'paramTitle': '1',
		# 'paramAuthor': 'автор',
	# },
	# {
		# 'renameTemplateTo': r'Отечественные певцы 1750-1917',
		# 'urlPartWithPagename': r'Отечественные%20певцы|%D0%9E%D1%82%D0%B5%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%B5%D0%B2%D1%86%D1%8B',
		# 'addSignature': '',
		# 'paramTitle': '1',
		# 'paramAuthor': 'автор',
	# },
	# # {
		# # renameTemplateTo : 'Кто есть кто в современной культуре‎‎',
		# # 'addSignature': 'dict/who-is-who',
		# # pagenameFromLink : r'/(?:Кто%20есть%20кто%20в%20культуре/|%D0%9A%D1%82%D0%BE%20%D0%B5%D1%81%D1%82%D1%8C%20%D0%BA%D1%82%D0%BE%20%D0%B2%20%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%B5/)([^]|/?&}\n]+)/?',
		# # link2removebase : r'Кто%20есть%20кто%20в%20культуре|%D0%9A%D1%82%D0%BE%20%D0%B5%D1%81%D1%82%D1%8C%20%D0%BA%D1%82%D0%BE%20%D0%B2%20%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%B5|dict/who-is-who',
	# # },
	# {
		# 'renameTemplateTo': r'Вокально-энциклопедический словарь',
		# 'urlPartWithPagename': r'Вокально-энциклопедический%20словарь|%D0%92%D0%BE%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE-%D1%8D%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C',
		# 'addSignature': r'|dict/agin',
		# 'paramTitle': '1',
		# 'paramAuthor': 'автор',
	# },
	# # {
		# # renameTemplateToIzBSE : 'Из БСЭ'
		# # pagenameFromLink : r'/(?:БСЭ/|%D0%91%D0%A1%D0%AD/|article.xml\?book=bse&title=|dict/bse)(?:/[^]/}]*)?/([^]|/?&}\s\n]+)'
		# # pagenameFromLink : r'/(?:БСЭ|%D0%91%D0%A1%D0%AD|dict/bse)(?:/[^]/}]*)?/(?:\d+/\d+\.htm\?text=)?([^]/}\s\n]+)'
		# # pagenameFromLink : r'/(?:БСЭ|%D0%91%D0%A1%D0%AD|dict/bse)(?:/[^]/}]*)?/([^]|/?&}\s\n]+)'  (?:/[^]/}]*)?
	# # },
	# ]
# link2removeSY = r'https?://(?:www\.|m\.)?slovari\.yandex\.ru'

# code = mwparserfromhell.parse(text)

# reSymbols = r'[.,;:›"/\s—−-]*'
# reEnd = reSymbols + '$'
# reBegin = '^' + reSymbols
# reTire = r'[\s—−-]+'
# reV = r'(?:\b(?:в|из|на)\s+)?'
# reBSE = reSymbols + r'\(?["«]*(?:\[\[)?(?:БСЭ|[Бб]ольш(ая|ой) [Сс]оветск(ая|ой) [Ээ]нциклопеди[яи])(?:\]\])?["»]*\)?[.,:;\s›—−-]*'
# reYS = r'["\'«]?(Яндекс[е]?[.\s]*(?:Словар(?:[еьи]|ях))?|(?:slovari.)?yandex.ru)["\'»]?'
# reRemoveFromTitles = [
	# # r'.*',  # внимание: это удаление всего заголовка ссылки, для взятия его из url. только для словарей с именем в url
	# r'(в )?[Сс]ловар(?:[еьи]|ях)?.*?(?:на )?(?:сайте )?' + reYS,
	# r'(?:Биография|Данные)? (?:на )?(?:сайте )?' + reYS,
	# # r'["\'«]?(?:[Яя]ндекс|[Yy]andex)[.\s:-]*(?:[Сс]ловари|[Ss]lovari)["\'»]?',
	# r'[Сс]ловари',
	# 'Биография',
	# r'{{мёртвая ссылка\|число=14\|месяц=06\|год=2016}}',
	# r'(?:\[\[Пружанский, Аркадий Михайлович\|)?Пружанский\s*А.\s*М.(?:&#93;&#93;)?\s*Отечественные певцы. 1750[\s—−-]+1917: Словарь.[\s—−-]+Изд. 2-е испр. и доп., электронное.[\s—−-]+М., 2008',
	# # r'(?:В 30 т.)?[—−/ -]*М.: "?Советская энциклопедия"?[,.] 1969[—−/ -]*1978',
	# # r'(?:в (?:словаре|энциклопедиии|книге|справочнике) )?["«]*Кто есть кто в(?: современной)? культуре["»]*',
	# r'(?:в\s+(?:словаре|энциклопедии|книге|справочнике)\s*)?["«]*Отечественные певцы["»]*',
	# r'[\s.]*Эксклюзивные биографии.[\s—−-]+Выпуск 1[\s—−-]+2.[\s—−-]+М.: МК[\s—−-]+Периодика, 2006[\s—−-]+2007\.?',
	# r'[[\s]*(Агин, Михаил Суренович\|)?Агин М\.\s*С\.[]\s]*(?:&#93;{{мёртвая ссылка\|число=14\|месяц=06\|год=2016}}&#93;)?\s*Вокально-энциклопедический словарь. \(?Биобиблиография\)?. В 5 т.[\s—−-]+М.,\s*1991[\s—−-]+1994\]*',
	# r'Вокально-энциклопедический словарь(?:, 1991-1994)?',
	# r'Отечественные певцы(?:[.\s—−-]+2008)?',
	# r'(?:Энциклопедия|в [Ээ]нциклопедии) ["«]*Москва["»]*',
	# r'М.: БРЭ, 1997',
	# r'Петербургская топонимика',
	# # r'На Яндекс[.:\s]*[Тт]опонимика',
	# '<!-- Заголовок добавлен ботом -->',
	# r'^Биография' + reV + reBSE,
	# r'^Биография$',
	# r'Электронная версия',
	# reSymbols + reV + reYS,
	# r'1969[\s—−-]*1978',
	# r'\d-е изд(?:\.|ание)?',
	# reSymbols + reV + reBSE,
	# r'[Сс]татья' + reV,
	# reBegin,
	# reEnd,
	# ]

# for dic in dics:
	# pagenameFromLink = r'/(?:' + dic['urlPartWithPagename'] + r')/([^]|/?&}\n]+)/?'
	# link2remove_DicSignature = dic['urlPartWithPagename'] + dic['addSignature']
	# link2remove = link2removeSY + r'/[^|\s]*(' + str(link2remove_DicSignature) + ')'

	# for template in code.filter_templates():
		# if template.name.matches(('cite web', 'cite news')) and findLink(template, link2remove):
			# newtpl = mwparserfromhell.nodes.template.Template(dic['renameTemplateTo'])
			# if template.has('title'):
				# title = str(template.get('title').value.strip())
				# newtpl.add(dic['paramTitle'], title)
			# if template.has('author') and template.get('author').value != '':
				# title = str(template.get('author').value.strip())
				# newtpl.add(dic['paramAuthor'], title)
			# code.replace(template, str(newtpl))

	# for template in code.filter_templates():
		# if template.name.matches(('книга')) and findLink(template, link2remove):
			# newtpl = mwparserfromhell.nodes.template.Template(dic['renameTemplateTo'])
			# if template.has('заглавие'):
				# title = str(template.get('заглавие').value.strip())
				# newtpl.add(dic['paramTitle'], title)
			# if template.has('автор') and template.get('автор').value != '':
				# title = str(template.get('автор').value.strip())
				# newtpl.add(dic['paramAuthor'], title)
			# code.replace(template, str(newtpl))

	# link2template(code, link2remove, dic['renameTemplateTo'], 'ссылка', dic['paramTitle'], reRemoveFromTitles, pagenameFromLink)


# print(code)
# for template in code.filter_templates():
# 	# print(template)
#
# 	if template.name.matches(('статья', 'книга', 'публикация', 'cite web', 'cite news', 'из', 'Из БСЭ')):
# 		# print(template)
# 		if not findLink(template, link2remove):
# 			separateLinkFromPartParameter(template)
# 			findAndDeleteLink(template, link2removeSY)
# 			continue
#
# 		if template.name.matches('Из') and template.get(1).value == 'БСЭ':
# 			# # if template.has('заглавие'):
# 			# if template.has(3):
# 			# if not re.match('^\s*$', str(template.get(3).value)):
# 			# template.add('заглавие', str(template.get(3).value))
# 			# template.remove(3)
# 			# else:
# 			# template.remove(3)
# 			# if not template.has(3) and not template.has('заглавие'):
# 			# if template.has('title'):
# 			# renameParam(template, 'title', 'заглавие')
# 			# else: template.add('заглавие', sys.argv[1])
#
# 			# if template.has(2):
# 			# template.add('ссылка', str(template.get(2).value))
# 			# template.remove(2)
#
# 			# template.remove(1)
# 			# removeTplParameters(template, ('издание',))
# 			# # renameParam(template, 'заглавие', 'статья')
# 			# template.name = renameTemplateTo
# 			# removeTplParametersExceptThis(template, ('автор', 'заглавие', 'статья', 'том', 'страницы', 'ref', 'ссылка', 'archiveurl', 'archivedate'))
# 			# findAndDeleteLink(template, link2remove)
# 			# deleteEmptyParam(template, ('автор', 'том', 'страницы', 'ссылка'))
# 			# removeSpacesBreaks(template)
#
#
#
# 			# r'/(?:БСЭ|%D0%91%D0%A1%D0%AD|dict/bse|article.xml\?book=bse)(?:/[^]/}\s]*)?(?:/\d+/\d+\.htm\?text=|&title=)?([^]/}]*)'
# 			# /[^]/}\s]+/
# 			deleteEmptyParam(template, (2, 3, 'title', 'заглавие'))
# 			if template.has('title') or template.has('заглавие') or template.has(2):
# 				renamedTitle = False
# 				if template.has('title'):
# 					renamedTitle = True
# 					renameParam(template, 'title', 'заглавие')
# 				if template.has(3) and not template.has('заглавие'):  # переименовать
# 					template.get(3).name = 'заглавие'
# 				if renamedTitle == True:  # переименовать title как было, чтобы небыло вопросов, и не надо было отвечать
# 					renameParam(template, 'заглавие', 'title')
# 					renamedTitle = False
# 			else:
# 				paramValueFromLinkOrPagename(template, 'заглавие', 2, pagenameFromLink)
#
# 			if template.has(2) or template.has('ссылка') or template.has('url'):
# 				findAndDeleteLink(template, link2remove, (2,))
# 				deleteEmptyParam(template, (2, 'ссылка', 'url'))
#
# 			template.remove(1)
# 			template.name = renameTemplateToIzBSE
# 			replaceParamValue(template, 'автор', '\s{2,}', ' ')
# 			replaceParamValue(template, 'статья', '\s*— БСЭ — Яндекс.Словари', '')
# 			replaceParamValue(template, 'статья', '\s*// Большая советская энциклопедия', '')
# 			replaceParamValue(template, 'статья', '\s*в Большой Советской Энциклопедии', '')
# 			replaceParamValue(template, 'том', '\s*(\d+).*', r'\1')
# 			# removeTplParametersExceptThis(template, ('автор', 'статья', 'заглавие', 'том', 'страницы', 'ref', \
# 			# 'ссылка', \
# 			# 'archiveurl', 'archivedate', \
# 			# 'add quotes', 'кавычки', 'издание', 'title')) # {{Из БСЭ}}
# 			deleteEmptyParam(template, ('автор', 'том', 'страницы', 'ссылка', 'издание', 'title', 'заглавие'))
# 			deleteParamArhiveurlDateIfWebarchive(template)
# 			removeSpacesBreaks(template)
# 			continue
#
# 		elif template.name.matches('Из БСЭ'):
# 			# # переделка 'Из БСЭ' → в БСЭ3
# 			# # if template.has(1):
# 			# # template.add('ссылка', str(template.get(1).value))
# 			# # template.remove(1)
# 			# # findAndDeleteLink(template, link2remove)
# 			# # deleteEmptyParam(template, ('ссылка',))
# 			# # if template.has('title') or template.has('заглавие'):
# 			# # renameParam(template, 'title', 'заглавие')
# 			# # else:
# 			# # if template.has(2):
# 			# # if not re.match('^\s*$', str(template.get(2).value)):   # не пустой параметр
# 			# # template.add('заглавие', str(template.get(2).value))
# 			# # template.remove(2)
# 			# # else: # пустой параметр, назвать по названию страницы
# 			# # template.add('заглавие', sys.argv[1])
# 			# # template.remove(2)
# 			# # else:
# 			# # template.add('заглавие', sys.argv[1])
# 			# # # print(template)
#
# 			# просто чистка и парсинг url в 'Из БСЭ'
#
# 			# заглавия из ссылок, удаление имеющихся введённых вручную заглавий
# 			for p in ('заглавие', 'title', 2):
# 				if template.has(p):
# 					if isPagenameInLink(template, 1, pagenameFromLink):
# 						template.get(p).value = ''
#
# 			if template.has('заглавие'):
# 				if template.get('заглавие').value == 'None':
# 					template.get('заглавие').value = ''
# 			deleteEmptyParam(template, (1, 2, 'title', 'заглавие'))
# 			if template.has('title') or template.has('заглавие') or template.has(2):
# 				renamedTitle = False
# 				if template.has('title'):
# 					renamedTitle = True
# 					renameParam(template, 'title', 'заглавие')
# 				if template.has(2) and not template.has('заглавие'):  # переименовать
# 					template.get(2).name = 'заглавие'
# 				if renamedTitle == True:  # переименовать title как было, чтобы небыло вопросов, и не надо было отвечать
# 					renameParam(template, 'заглавие', 'title')
# 					renamedTitle = False
#
# 					# # заглавия из ссылок, удаление имеющихся введённых вручную заглавий
# 					# if isPagenameInLink(template, 'заглавие', 1, pagenameFromLink, True):
# 					# paramValueFromLinkOrPagename(template, 'заглавие', 1, pagenameFromLink, True)
# 			else:
# 				paramValueFromLinkOrPagename(template, 'заглавие', 1, pagenameFromLink)
# 			if not template.has('заглавие'):
# 				template.name = r'БСЭ3|заглавие='
#
# 			if template.has(1) or template.has('ссылка') or template.has('url'):
# 				findAndDeleteLink(template, link2remove, (1,))
# 				deleteEmptyParam(template, (1, 'ссылка', 'url'))
# 			continue
#
# 		elif template.name.matches(('статья', 'книга', 'публикация', 'cite web', 'cite news')):
# 			# print(template)
# 			# if not findAndDeleteLink(template, link2remove): continue
# 			if template.name.matches('статья') or \
# 					(template.name.matches('публикация') and template.has(1) and template.get(1).value == 'статья'):
# 				findAndDeleteLink(template, link2remove)
# 			# renameParam(template, 'заглавие', 'статья')
# 			# removeTplParametersExceptThis(template, ('автор', 'статья', 'заглавие', 'том', 'страницы', 'ref', 				'archiveurl', 'archivedate'))
# 			# print(template)
#
# 			elif template.name.matches(('книга', 'публикация')):
# 				separateLinkFromPartParameter(template)
# 				template.remove('заглавие')
# 				if template.has('часть'):
# 					paramValueFromLinkOrPagename(template, 'часть', '', pagenameFromLink)
# 					renameParam(template, 'часть', 'статья')
# 				findAndDeleteLink(template, link2remove)
# 				# removeTplParametersExceptThis(template, ('автор', 'статья', 'заглавие', 'том', 'страницы', 'ref', 				'archiveurl', 'archivedate'))
# 				print(template)
#
# 			elif template.name.matches(('cite web', 'cite news')):
# 				renameParam(template, 'url', 'ссылка')
# 				renameParam(template, 'author', 'автор')
# 				renameParam(template, 'title', 'статья')
# 			# removeTplParametersExceptThis(template, ('автор', 'статья', 'заглавие', 'том', 'страницы', 'ref', 				'archiveurl', 'archivedate'))
#
# 			template.name = renameTemplateToBSE
# 			# removeTplParameters(template, ParametersToRemove)
# 			replaceParamValue(template, 'автор', '\s{2,}', ' ')
# 			replaceParamValue(template, 'статья', '\s*— БСЭ — Яндекс.Словари', '')
# 			replaceParamValue(template, 'статья', '\s*// Большая советская энциклопедия', '')
# 			replaceParamValue(template, 'статья', '\s*в Большой Советской Энциклопедии', '')
# 			replaceParamValue(template, 'том', '\s*(\d+).*', r'\1')
# 			removeTplParametersExceptThis(template, (
# 				'автор', 'статья', 'заглавие', 'том', 'страницы', 'ref', 'archiveurl', 'archivedate'))
# 			# removeTplParametersExceptThis(template, ('автор', 'статья', 'заглавие', 'том', 'страницы', 'ref', \
# 			# 'ссылка', \
# 			# 'archiveurl', 'archivedate', \
# 			# 'add quotes', 'кавычки', 'издание', 'title')) # {{Из БСЭ}}
# 			deleteEmptyParam(template, (
# 				'автор', 'том', 'страницы', 'ссылка', 'ссылка часть', 'часть ссылка', 'издание', 'title', 'заглавие',
# 				'ref',
# 				'archiveurl', 'archivedate'))
# 			deleteParamArhiveurlDateIfWebarchive(template)
# 			removeSpacesBreaks(template)
# 			# print(template)

# print(str(code))
# print(9)


# text = str(code)
# f = open(filename, 'w', encoding='utf-8')
# f.write(text)
# f.close()
