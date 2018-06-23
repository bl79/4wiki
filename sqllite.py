# -*- coding: utf-8 -*-
import sqlite3


def create_table():
	# Подключение к базе
	# conn = sqlite3.connect('my.sqlite')
	conn = sqlite3.connect(':memory:')
	# Создание курсора
	c = conn.cursor()
	# Создание таблицы
	c.execute('''CREATE TABLE pages (page_id INT PRIMARY KEY,title VARCHAR, timeedit INT)''')
	c.execute(
		'''CREATE TABLE refs (id INT auto_increment PRIMARY KEY,page_id INT, citeref VARCHAR, link_to_sfn VARCHAR, ref_text VARCHAR)''')
	conn.commit()
	# закрываем соединение с базой
	c.close()
	conn.close()


def add_page(page_id, title, timeedit):
	c.execute("INSERT INTO pages (page_id,title,timeedit) VALUES ('%s','%s','%s')" % (page_id, title, timeedit))
	conn.commit()


def add_ref(page_id, citeref, link_to_sfn, ref_text):
	c.execute("INSERT INTO refs (page_id,citeref,link_to_sfn,ref_text) VALUES ('%s','%s','%s','%s')" % (
	page_id, citeref, link_to_sfn, ref_text))
	conn.commit()


# Вводим данные
# name = 'adminuuu'
# passwd = '123uuuu'
# add_user(name, passwd)

# таким образом можно добавить новый элемент
# new_page = Pages(2, "14\"/45_BL_Mark_VII", 20160910000000)
# new_ref = Refs(2, "CITEREF.D0.91.D0.B0.D0.BB.D0.B0.D0.BA.D0.B8.D0.BD.2C_.D0.94.D0.B0.D1.88.D1.8C.D1.8F.D0.BD2006",
# 			   "cite_note-.D0.91.D0.B0.D0.BB.D0.B0.D0.BA.D0.B8.D0.BD.2C_.D0.94.D0.B0.D1.88.D1.8C.D1.8F.D0.BD.E2.80.942006.E2.80.94.E2.80.94238-1",
# 			   "Балакин, Дашьян, 2006")
add_page(2, "14\"/45_BL_Mark_VII", 20160910000000)
add_ref(2, "CITEREF.D0.91.D0.B0.D0.BB.D0.B0.D0.BA.D0.B8.D0.BD.2C_.D0.94.D0.B0.D1.88.D1.8C.D1.8F.D0.BD2006",
		"cite_note-.D0.91.D0.B0.D0.BB.D0.B0.D0.BA.D0.B8.D0.BD.2C_.D0.94.D0.B0.D1.88.D1.8C.D1.8F.D0.BD.E2.80.942006.E2.80.94.E2.80.94238-1",
		"Балакин, Дашьян, 2006")

# Делаем запрос в базу
# print("Список пользователей:\n")
c.execute('SELECT * FROM users')
row = c.fetchone()

# выводим список пользователей в цикле
while row is not None:
	print("id:" + str(row[0]) + " Логин: " + row[1] + " | Пароль: " + row[2])
	row = c.fetchone()

# закрываем соединение с базой
c.close()
conn.close()
