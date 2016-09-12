# from my import *
# from pywikibot import category
import os
import vladi_commons

# summary = r"орфография категории [[ВП:ЗКБВ#Средние века|по запросу]]"
summary = r"категория: [[ВП:Обсуждение категорий/Сентябрь 2016#10 сентября 2016]]"
# summary = r"категория: по основной статье"
# summary = r"переименование категории: аналогично другим в [[:Категория:Праздники по странам]]"

# CategoriesToRename = [
	# ["Категория:Персоналии XVIII века по национальности‎", "Категория:Персоналии XVIII века по странам‎"],
	# ["Категория:Персоналии XVI века по национальности‎", "Персоналии XVI века по странам‎"],
# ]
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
	