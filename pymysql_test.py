# -*- coding: utf-8 -*-
import pymysql.cursors
import urllib.parse

# # Connect to the database
# connection = pymysql.connect(
# 		host='127.0.0.1', port=4711,
# 		# host='ruwiki.labsdb', port=3306,
# 		user='u14134',
# 		password='4mlodHqAsy3xTivW',
# 		db='ruwiki_p',
# 		use_unicode=True, charset="utf8"
# )
#
# try:
# 	# with connection.cursor() as cursor:
# 	#     # Create a new record
# 	#     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
# 	#     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
# 	#
# 	# # connection is not autocommit by default. So you must commit to save
# 	# # your changes.
# 	# connection.commit()
#
# 	with connection.cursor() as cursor:
# 		# Read a single record
# 		# sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
# 		# cursor.execute(sql, ('webmaster@python.org',))
# 		tpl = ['Любкер']
# 		time_lastcheck = 20160910000000
# 		sql = """SELECT
# 				  page.page_id,
# 				  page.page_title,
# 				  MAX(revision.rev_timestamp) AS timestamp
# 				FROM page
# 				  INNER JOIN templatelinks
# 					ON page.page_id = templatelinks.tl_from
# 				  INNER JOIN revision
# 					ON page.page_id = revision.rev_page
# 				WHERE templatelinks.tl_namespace = 10
# 				AND page.page_namespace = 0
# 				AND templatelinks.tl_title IN ('%s')
# 				AND revision.rev_timestamp > %d
# 				GROUP BY page.page_title
# 				ORDER BY page.page_title""" % (
# 			','.join(['"' + t + '"' for t in tpl]),
# 			time_lastcheck
# 		)
#
# 		# sql = """SELECT page_title
# 		# 		FROM page
# 		# 		JOIN templatelinks ON tl_from = page_id
# 		# 			WHERE tl_namespace = 10
# 		# 			AND tl_title = '%s'
# 		# 			AND page_namespace = 0""" % 'Любкер'
#
# 		cursor.execute(sql)
#
# 	result = cursor.fetchall()



def wdb_pages():
	tpl = ['Любкер']
	time_lastcheck = 20160910000000
	sql = """SELECT
			  page.page_id,
			  page.page_title,
			  MAX(revision.rev_timestamp) AS timestamp
			FROM page
			  INNER JOIN templatelinks
				ON page.page_id = templatelinks.tl_from
			  INNER JOIN revision
				ON page.page_id = revision.rev_page
			WHERE templatelinks.tl_namespace = 10
			AND page.page_namespace = 0
			AND templatelinks.tl_title IN ('%s')
			AND revision.rev_timestamp > %d
			GROUP BY page.page_title
			ORDER BY page.page_title""" % (
		','.join(['"' + t + '"' for t in tpl]),
		time_lastcheck
	)

	from wikiapi import wdb_query  # contents parameters: api_user, api_pw, wdb_user, wdb_pw
	result = wdb_query(sql)

	# r = result
	if len(result) > 0:
		# print(len(result))
		for rs in result:
			# r = rs['page_title']
			# time_lastedit = rs['timestamp']
			r = rs[0]
			time_lastedit = rs[1]
			r = urllib.parse.quote_from_bytes(r)
			# r = urllib.parse.urlencode(r, encoding='utf8')
			r = urllib.parse.unquote(r, encoding='utf8')
		print(r, time_lastedit)
	return result

result = wdb_pages()

# finally:
# 	connection.close()

import sqlite3

# Подключение к базе
conn = sqlite3.connect(':memory:')
# Создание курсора
c = conn.cursor()
# Создание таблицы
c.execute('''CREATE TABLE users (id INT auto_increment PRIMARY KEY, title VARCHAR, timestamp VARCHAR)''')


# Функция занесения пользователя в базу
def add_user(title, timestamp):
	c.execute("INSERT INTO users (title,timestamp) VALUES ('%s','%s')" % (title, timestamp))
	conn.commit()


# Наполнение таблицы
if len(result) > 0:
	# print(len(result))
	for r in result:
		# print(r[0], r[1])
		t = r[0]
		t = urllib.parse.quote_from_bytes(t)
		# r = urllib.parse.urlencode(r[0], encoding='utf8')
		# t = urllib.parse.unquote(t, encoding='utf8')
		# print(urllib.parse.unquote(r[0], encoding='utf8'))
		# print(r[0], r[1])
		print(t, r[1])
		add_user(t, r[1])

# Делаем запрос в базу
print("Список пользователей:\n")
c.execute('SELECT * FROM users')
row = c.fetchone()

# выводим список пользователей в цикле
while row is not None:
	print("id:" + str(row[0]) + " Логин: " + row[1] + " | Пароль: " + row[2])
	row = c.fetchone()

# закрываем соединение с базой
c.close()
conn.close()
