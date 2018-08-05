#!/usr/bin/env python3
# coding: utf-8

# from my import *
# from pywikibot import category
import os
from vladi_commons.vladi_helpers import file_readlines_in_list_interlines

"""
python $PWBPATH/pwb.py listpages -family:wikipedia -format:3 -ns:14 -subcats:"Категория:Фараоны"  > ~/workspace/4wiki/categories_rename/cats2rename.txt
"""

# summary = r"орфография категории [[ВП:ЗКБВ#Средние века|по запросу]]"
# summary = r"Переименование категории: по [[ВП:Обсуждение категорий/Декабрь 2016#15 декабря 2016|итогу обсуждения]]"
# summary = r"уточнение названия категории, по [[ВП:КАТГОС]]"
# summary = r"уточнение названия категории"
# summary = r"Переименование категории, [[ВП:Обсуждение категорий/Февраль 2017#8 февраля 2017|унифиация]]"
# summary = r"Переименование категории: дубликат"
# summary = r"Переименование категории: по основной статье и [[ВП:Обсуждение категорий/Январь 2017#10 января 2017|итогу обсуждения]]"
# summary = r"категория, по [[ВП:Обсуждение категорий/Март 2017#8 марта 2017|обсуждению]]"
# summary = r"Переименование категории: [[ВП:Обсуждение категорий/Декабрь 2016#2 декабря 2016|по основной статье]]"
summary = r"Переименование категории: по основной статье"
# summary = r"переименование категории: аналогично другим в [[:Категория:Праздники по странам]]"
# summary = r"категория"


# регулярка для создания списка (в отдельном файле, незабыть переконвертировать список в оконания строк как в Unix CR для r'\n'):
# ^Категория:Арбитры(.*?)\n
# Категория:Футбольные арбитры$1\nКатегория:Футбольные судьи$1\n

def clearstr(s):
    """чистка невидимого символа в конце названия"""
    return s.strip().replace(b'\xe2\x80\x8e'.decode('utf-8'), '')


if __name__ == '__main__':

    file_listcat = 'cats2rename.txt'
    CategoriesToRename = file_readlines_in_list_interlines(file_listcat)

    Windows = False
    # Windows = True
    if Windows:
        runcommand, config = f'python c:/pwb/pwb.py', ''
    else:
        runcommand, config = 'python3 $PWBPATH/pwb.py', '-dir:~/.pywikibot'
    args = [
        # '-family:wikisource',
        '-family:wikipedia',
        # '-simulate',
        '-user:TextworkerBot',
    ]
    arguments = ' ' + ' '.join(args)

    # логин
    run = f'{runcommand} login.py {arguments} {config}'
    os.system(run)

    # print('echo ' + str(CategoriesToRename))
    summary_ = f'-summary:"{summary}"'
    for catold, catnew in CategoriesToRename:
        catnew = clearstr(catnew)
        # переименование страницы
        command = r'movepages.py -pt:0' + ' -noredirect'
        run = f'{runcommand} {command} -from:"{clearstr(catold)}" -to:"{catnew}" {summary_} {arguments} {config}'
        print(f'echo {run}')
        os.system(run)
        # run = f'{runcommand} {command} -from:"{catold}" -to:"{catnew}" {summary_} {arguments} {config}'
        # print(f'rename with cleanup a invisible symbol, echo {run}')
        # os.system(run)

        # # переименование категорий
        # command = r'replace.py -regex "(\[\[Категория:[^]|]+)[‎\s]+(\||\]\])" "\1\2"'
        # run = f'{runcommand} {command} -cat:"{catold}" -always -summary:"викификация" {arguments} {config}'
        # print(f'echo {run}')
        # os.system(run)

        # переименование категорий
        command = r'category.py move -pt:0 -inplace'  # -keepsortkey
        run = f'{runcommand} {command} -from:"{clearstr(catold)}" -to:"{catnew}" {summary_} {arguments} {config}'
        print(f'echo {run}')
        os.system(run)
        # run = f'{runcommand} {command} -from:"{catold}" -to:"{catnew}" {summary_} {arguments} {config}'
        # print(f'rename with cleanup a invisible symbol, echo {run}')
        # os.system(run)
