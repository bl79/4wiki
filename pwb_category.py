# from my import *
# from pywikibot import category
import os
import vladi_commons

# summary = r"орфография категории [[ВП:ЗКБВ#Средние века|по запросу]]"
# summary = r"Переименование категории: по [[ВП:Обсуждение категорий/Декабрь 2016#15 декабря 2016|итогу обсуждения]]"
# summary = r"уточнение названия категории, по [[ВП:КАТГОС]]"
# summary = r"уточнение названия категории"
summary = r"Переименование категории, по [[ВП:Обсуждение категорий/Декабрь 2016#10 декабря 2016|итогу обсуждения]]"
# summary = r"Переименование категории: дубликат"
# summary = r"Переименование категории: по основной статье и [[ВП:Обсуждение категорий/Декабрь 2016#2 декабря 2016|итогу обсуждения]]"
# summary = r"Переименование категории: [[ВП:Обсуждение категорий/Декабрь 2016#2 декабря 2016|по основной статье]]"
# summary = r"Переименование категории: по основной статье"
# summary = r"переименование категории: аналогично другим в [[:Категория:Праздники по странам]]"


# регулярка для создания списка (в отдельном файле, незабыть переконвертировать список в оконания строк как в Unix CR для r'\n'):
# ^Категория:Арбитры(.*?)\n
# Категория:Футбольные арбитры$1\nКатегория:Футбольные судьи$1\n

file_listcat = 'cats2rename.txt'
CategoriesToRename = vladi_commons.file_readlines_in_list_interlines(file_listcat)

# логин
run = r'python c:\pwb\pwb.py login.py'
os.system(run)

# print('echo ' + str(CategoriesToRename))	
summary_ = ' -summary:"' + summary + '"'
for cats in CategoriesToRename:	

	# переименование страницы
	command = r'python c:\pwb\pwb.py movepages.py -pt:0 -noredirect'
	from_ = ' -from:"' + cats[0] + '"'
	to_ = ' -to:"' + cats[1] + '"'
	run = command + from_ + to_ + summary_  # + ' -simulate'	
	print('echo ' + run)		
	os.system(run)	

	# переименование категорий
	command = r'python c:\pwb\pwb.py category.py move -pt:0 -inplace'  # -keepsortkey
	from_ = ' -from:"' + cats[0] + '"'
	to_ = ' -to:"' + cats[1] + '"'	
	run = command + from_ + to_ + summary_  # + ' -simulate'	
	# run += ' -batch'
	print('echo ' + run)		
	os.system(run)
	