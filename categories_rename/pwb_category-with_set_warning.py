# from my import *
# from pywikibot import category
import os
from vladi_commons.vladi_helpers import file_readlines_in_list_interlines

# summary = r"орфография категории [[ВП:ЗКБВ#Средние века|по запросу]]"
summary = r"категория: [[ВП:Обсуждение категорий/Июль 2016#20 июля 2016]]"
# summary = r"переименование категории: аналогично другим в [[:Категория:Праздники по странам]]"

# CategoriesToRename = [
# ["Категория:Персоналии XVIII века по национальности‎", "Категория:Персоналии XVIII века по странам‎"],
# ["Категория:Персоналии XVI века по национальности‎", "Персоналии XVI века по странам‎"],
# ]
file_listcat = 'cats2rename.txt'
CategoriesToRename = file_readlines_in_list_interlines(file_listcat)

# print('echo ' + str(CategoriesToRename))	
summary_ = f' -summary:"{summary}"'
for cats in CategoriesToRename:
    # переименование страницы
    command = r'python c:\pwb\pwb.py movepages.py -pt:0 -noredirect'
    from_ = f' -from:"{cats[0]}"'
    to_ = f' -to:"{cats[1]}"'
    run = command + from_ + to_ + summary_  # + ' -simulate'
    # print(f'echo {run}')
    # os.system(run)

    # переименование категорий
    command = r'python c:\pwb\pwb.py category.py move -pt:0 -inplace'  # -keepsortkey
    from_ = f' -from:"{cats[0]}"'
    to_ = f' -to:"{cats[1]}"'
    run = command + from_ + to_ + summary_  # + ' -simulate'
    run += ' -batch'
    print(f'echo {run}')
    os.system(run)

    # установка предупреждения "Переименованная категория"
    tpl = f'{{Переименованная категория|{cats[1][10:]}}}'
    run = f'python c:\pwb\pwb.py replace.py -pt:0 -page:"{cats[0]}" -regex "^.*$" "{tpl}" -dotall {summary_}'
    run += ' -always'
    print(f'echo {run}')
    os.system(run)
