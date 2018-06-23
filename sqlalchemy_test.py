# -*- coding: utf-8 -*-

import urllib.parse

class sqla:

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
				AND templatelinks.tl_title IN (%s)
				AND revision.rev_timestamp > %d
				GROUP BY page.page_title
				ORDER BY page.page_title""" % (
			','.join(['"' + t + '"' for t in tpl]),
			time_lastcheck
		)

		from wikiapi import wdb_query  # contents parameters: api_user, api_pw, wdb_user, wdb_pw
		result = wdb_query(sql)

		# r = result
		# if len(result) > 0:
		# 	# print(len(result))
		# 	for rs in result:
		# 		# r = rs['page_title']
		# 		# time_lastedit = rs['timestamp']
		# 		r = rs[0]
		# 		time_lastedit = rs[1]
		# 		r = urllib.parse.quote_from_bytes(r)
		# 		# r = urllib.parse.urlencode(r, encoding='utf8')
		# 		r = urllib.parse.unquote(r, encoding='utf8')
		# 	print(r, time_lastedit)
		return result


	def create_session(config):
		from sqlalchemy import create_engine
		from sqlalchemy.orm import sessionmaker
		# engine = create_engine(config['DATABASE_URI'])
		# engine = create_engine('sqlite:///:memory:', echo=True)
		db_engine = create_engine(config, echo=True)
		# создадём таблицы
		# metadata.create_all(db_engine)
		metadata.create_all(db_engine)
		# начинаем новую сессию работы с БД
		Session = sessionmaker(bind=db_engine)
		session = Session()
		# session._model_changes = {}
		return session


	from sqlalchemy import create_engine
	from sqlalchemy.orm import sessionmaker
	from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
	from sqlalchemy.orm import mapper
	from sqlalchemy.sql import join, select
	# from sqlalchemy import *

	metadata = MetaData()
	pages_table = Table('pages', metadata,
						# Column('id', Integer, primary_key=True),
						Column('page_id', Integer, primary_key=True, unique=True),
						Column('title', String, unique=True,index=True),
						Column('timeedit', Integer),
						)

	errrefs_table = Table('refs', metadata,
						  Column('id', Integer, primary_key=True,autoincrement=True),
						  Column('page_id', String),
						  Column('citeref', String),
						  Column('link_to_sfn', String),
						  Column('text', String)
						  )

	timecheck_table = Table('timecheck', metadata,
						  Column('page_id', Integer, primary_key=True, unique=True),
						  Column('lastcheck', Integer),
						  )

	class Page(object):
		def __init__(self, page_id, title, timeedit):
			self.page_id = page_id
			self.title = title
			self.timeedit = timeedit

	class Ref(object):
		def __init__(self, page_id, citeref, link_to_sfn, text):
			self.page_id = page_id
			self.citeref = citeref
			self.link_to_sfn = link_to_sfn
			self.text = text

	class Timecheck(object):
		def __init__(self, lastcheck, page_id=''):
			self.page_id = page_id
			self.lastcheck = lastcheck


	session = create_session('sqlite:///:memory:')

	mapper(Page, pages_table)
	mapper(Ref, errrefs_table)
	mapper(Timecheck, timecheck_table)

	# new_page = Page(2, "Вася", 8888)
	# new_ref = Ref(2, "ccccc", '#linkref', 'textlink')


	# result = wdb_pages()
	result = [[1, "Вася", 5555], [2, "Пе́тя", 8888]]
	# print(result)

	if len(result) > 0:
		# print(len(result))
		for rs in result:
			# r = rs['page_title']
			# time_lastedit = rs['timestamp']
			r = rs[1]
			# time_lastedit = rs[1]
			# r = urllib.parse.quote_from_bytes(r)
			# r = urllib.parse.urlencode(r, encoding='utf8')
			# r = urllib.parse.unquote(r, encoding='utf8')
			# print(r)
			new_page = Page(rs[0], r, rs[2])
			# print(new_page)
			session.add(new_page)
			print(rs[0], r, rs[2])

	# session.add(new_page)
	session.commit()

	# print(new_page)

	# print(new_page.title)  # Напечатает <User('Вася', 'Василий', 'qweasdzxc'>
	# query = session.query(User, Role, Product, Order, UserStatus)
	# query = query.join(UserRole,
	# 				   UserRole.user_id == User.id)  # r = session.query(title).join(Album).filter(Album.id == 10).count()

	# посмотрим что уже есть в базе данных
	# for instance in session.query(Page):
	# 	print(instance)

	# join_obj = pages_table.join(errrefs_table,
	# 							pages_table.c.page_id == errrefs_table.c.page_id)  # r = session.query(title).join(Album).filter(Album.id == 10).count()
	# query = select([pages_table.c.title, pages_table.c.timeedit]).select_from(join_obj)
	# r = session.execute(query).fetchall()

	query = select([Page.page_id, Page.title, Page.timeedit]).select_from(Page)
	r = session.execute(query).fetchall()

	# with Session() as session:
	# 	query = session.query(pages_table.title)
	# 	records = query.all()
	print(r)

	# совершаем транзакцию
	session.commit()

	import time
	session.add(Timecheck(time.strftime('%Y%m%d%H%M%S')))
	session.commit()


	import vladi_commons
	warning_tpl_name = 'Нет полных библиографических описаний'
	names_sfn_templates = ([
		'sfn', 'sfn0', 'Sfn-1',
		'Harvard citation', 'Harv',
		'Harvard citation no brackets', 'Harvnb', 'Harvsp',
		'Harvcol', 'Harvcoltxt', 'Harvcolnb', 'Harvrefcol',
	])
	tpls = vladi_commons.type_str2list(warning_tpl_name) + vladi_commons.type_str2list(names_sfn_templates)
	print(tpls)
