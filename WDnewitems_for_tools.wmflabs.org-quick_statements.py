# Для Wikidata:
# Создаёт список для создания элементов и их свойств, для использования в интструменте http://tools.wmflabs.org/wikidata-todo/quick_statements

# Списки свойств.
# Формат текста: '["свойство", "значение"]' в двойных кавычках. Текстовые значения в двойных и одинарных одновременно: '"text"'.
# Квалификаторы продолжаются на той же строке внутри того же "[,]", в том же формате через запятую.

# Общие свойства для всех элементов (чтобы не дублировать).
common_claims = [
		['P31', 'Q3331189'],    # это частный случай понятия : издание
		# ['P361', 'Q23705356'],  # часть от : Толковый словарь В. Даля, изд. №
		['P407', 'Q7737'],      # язык произведения или его названия : русский язык
		['P291', 'Q649'],       # место публикации : 'Q656' Санкт-Петербург, 'Q649' Москва
		# ['P98', 'Q335092'],     # редактор : Иван Александрович Бодуэн де Куртенэ
		# ['P767', 'Q335092'],    # соавтор : Иван Александрович Бодуэн де Куртенэ
		# ['P123', 'Q26202353'],  # издатель : Издательство М.О. Вольфа
		# ['P50', 'Q326499'],     # автор : Владимир Иванович Даль
		# 'P629']  : "Q1970746",  # является изданием или переводом : Толковый словарь В. Даля
		# ['P1476', 'ru:"А — З."'],  # название
]

# Создавать ли новые элементы? False - редактировать существующие указанные в массиве ниже ниже, True - создавать новые, id-номера ниже в private_claims[][0]
do_create_new_items = True

# Уникальные свойства для каждого элемента. Сколько списков столько будет элементов.
private_claims = [
	# [
	# 	'Q23705356',	# издание
	# 	# Для редактирования уже существующих элементов их id. Игнорируется если do_create_new_items = False.
	# 	[
	# 		# ['P393', "3"],            # номер издания, для томов и статей не надо
	# 		# ['Lru', "Толковый словарь В. Даля 3-е изд."],  # название элемента
	# 		# P1476 : 'ru:"Толковый словарь живого великорусского языка"',  # название
	# 		# ['P577', '+1903-01-17T00:00:00Z/09'],  # дата публикации
	# 		# ['P1815', '01003972235'],  # идентификатор сканированного издания РГБ
	# 		# ['P361', 'Q23705304', 'P155', '', 'P156', 'Q26203084'],  # состоит из, для списков томов в элементах изданий
	# 		# часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
	# 	]
	# ],
	# [
	# 	'Q23705360',  # издание
	# 	[
	# 		['P527', 'Q26205048'],  # состоит из, для списков томов в элементах изданий
	# 		['P527', 'Q26205045'],
	# 		['P527', 'Q26205046'],
	# 		['P527', 'Q26205047'],
	# 	],
	# ],
	# [
	# 	'Q23705356',  # издание
	# 	[
	# 		['P527', 'Q26205040'],  # состоит из, для списков томов в элементах изданий
	# 		['P527', 'Q26205041'],
	# 		['P527', 'Q26205042'],
	# 		['P527', 'Q26205049'],
	# 	]
	# ],


	# ---------------------------- ниже элементы сущностей более мелкого разряда
	[
		'Q26205040',  # Для редактирования уже существующих элементов их id. Игнорируется если do_create_new_items = False.
		[
			['Lru', "Толковый словарь В. Даля, 2001, том 1"],  # название элемента
			['P1476', 'ru:"А—3"'],  # название
			['P478', '"1"'],     # том
			# ['P577', '+1880-01-17T00:00:00Z/09'],  # дата публикации
			# ['P996', '"Толковый словарь Даля (2-е издание). Том 1 (1880).pdf"'],  # файл с отсканированными данными
			# ['P1957', '"https://ru.wikisource.org/wiki/Индекс:Толковый_словарь_Даля_(2-е_издание)._Том_1_(1880).pdf"'],  # индексная страница Викитеки
			# ['P1815', '"01003895333"'],  # идентификатор сканированного издания РГБ
			['P675', '"xn3NNBAAoScC"'],  # идентификатор Google Book
			['P957', '"5-224-02354-8"'],  # ISBN-10,  ISBN-13 (P212)
			['P361', 'Q26205138'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
			# ['P361', 'Q23705356', 'P156', 'Q26205041'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
		]
	],
	[
		'Q26205041',
		[
			['Lru', "Толковый словарь В. Даля, 2001, том 2"],  # название элемента
			['P1476', 'ru:"И—О"'],  # название
			['P478', '"2"'],     # том
			# ['P577', '+1881-01-17T00:00:00Z/09'],  # дата публикации
			# ['P996', '"Толковый словарь Даля (2-е издание). Том 2 (1881).pdf"'],  # файл с отсканированными данными
			# ['P1957', '"https://ru.wikisource.org/wiki/Индекс:Толковый_словарь_Даля_(2-е_издание)._Том_2_(1881).pdf"'],  # индексная страница Викитеки
			# ['P1815', '"01003895332"'],  # идентификатор сканированного издания РГБ
			['P675', '"lIcGQkEOOuQC"'],  # идентификатор Google Book
			['P957', '"5-224-02436-6"'],  # ISBN-10,  ISBN-13 (P212)
			['P361', 'Q26205138'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
			# ['P361', 'Q23705356', 'P155', 'Q26205040', 'P156', 'Q26205042'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
		]
	],
	[
		'Q26205042',
		[
			['Lru', "Толковый словарь В. Даля, 2001, том 3"],  # название элемента
			['P1476', 'ru:"П—Р"'],  # название
			['P478', '"3"'],     # том
			# ['P577', '+1882-01-17T00:00:00Z/09'],  # дата публикации
			# ['P996', '"Толковый словарь Даля (2-е издание). Том 3 (1882).pdf"'],  # файл с отсканированными данными
			# ['P1957', '"https://ru.wikisource.org/wiki/Индекс:Толковый_словарь_Даля_(2-е_издание)._Том_3_(1882).pdf"'],  # индексная страница Викитеки
			# ['P1815', '"01003895331"'],  # идентификатор сканированного издания РГБ
			['P675', '"5-224-02437-4"'],  # идентификатор Google Book
			['P361', 'Q26205138'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
			# ['P361', 'Q23705356', 'P155', 'Q26205041', 'P156', 'Q26205049'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
		]
	],
	[
		'Q26205049',
		[
			['Lru', "Толковый словарь В. Даля, 2001, том 4"],  # название элемента
			['P1476', 'ru:"C—V"'],  # название
			['P478', '"4"'],     # том
			# ['P577', '+1882-01-17T00:00:00Z/09'],  # дата публикации
			# ['P996', '"Толковый словарь Даля (2-е издание). Том 4 (1882).pdf"'],  # файл с отсканированными данными
			# ['P1957', '"https://ru.wikisource.org/wiki/Индекс:Толковый_словарь_Даля_(2-е_издание)._Том_4_(1882).pdf"'],  # индексная страница Викитеки
			# ['P1815', '"01003895330"'],  # идентификатор сканированного издания РГБ
			['P675', '"5-224-02438-2"'],  # идентификатор Google Book
			['P361', 'Q26205138'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
			# ['P361', 'Q23705356', 'P155', 'Q26205042'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
		]
	],





	[
		'Q26205048',  # Для редактирования уже существующих элементов их id. Игнорируется если do_create_new_items = False.
		[
			['Lru', "Толковый словарь В. Даля. В 2 тт. 2002, том 1"],  # название элемента
			['P1476', 'ru:"А—О"'],  # название
			['P478', '"1"'],     # том
			# ['P577', '+1863-01-17T00:00:00Z/09'],  # дата публикации
			# ['P996', '"Толковый словарь Даля (1-е издание). Часть 1 (1863).pdf"'],  # файл с отсканированными данными
			# ['P1957', '"https://ru.wikisource.org/wiki/Индекс:Толковый_словарь_Даля_(1-е_издание)._Часть_1_(1863).pdf"'],  # индексная страница Викитеки
			# ['P1815', '"01003833539"'],  # идентификатор сканированного издания РГБ
			['P361', 'Q26205137'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
			['P675', '"5-224-03585-6"'],  # идентификатор Google Book
			# ['P361', 'Q23705360' , 'P156', 'Q26205045'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
		]
	],
	[
		'Q26205045',
		[
			['Lru', "Толковый словарь В. Даля. В 2 тт. 2002, том 2"],  # название элемента
			['P1476', 'ru:"П—V"'],  # название
			['P478', '"2"'],     # том
			# ['P577', '+1865-01-17T00:00:00Z/09'],  # дата публикации
			# ['P996', '"Толковый словарь Даля (1-е издание). Часть 2 (1865).pdf"'],  # файл с отсканированными данными
			# ['P1957', '"https://ru.wikisource.org/wiki/Индекс:Толковый_словарь_Даля_(1-е_издание)._Часть_2_(1865).pdf"'],  # индексная страница Викитеки
			# ['P1815', '"01003833541"'],  # идентификатор сканированного издания РГБ
			['P361', 'Q26205137'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
			['P675', '"5-224-03586-4"'],  # идентификатор Google Book
			# ['P361', 'Q23705360', 'P155', 'Q26205048', 'P156', 'Q26205046'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
		]
	],
	# [
	# 	'Q26205046',
	# 	[
	# 		# ['Lru', "Толковый словарь В. Даля 1-е изд., том 3"],  # название элемента
	# 		# # ['P1476', 'ru:"П."'],  # название
	# 		# ['P478', '"3"'],     # том
	# 		# ['P577', '+1865-01-17T00:00:00Z/09'],  # дата публикации
	# 		# ['P996', '"Толковый словарь Даля (1-е издание). Часть 3 (1865).pdf"'],  # файл с отсканированными данными
	# 		# ['P1957', '"https://ru.wikisource.org/wiki/Индекс:Толковый_словарь_Даля_(1-е_издание)._Часть_3_(1865).pdf"'],  # индексная страница Викитеки
	# 		# ['P1815', '"01003833540"'],  # идентификатор сканированного издания РГБ
	# 		# ['P361', 'Q23705360'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
	# 		['P361', 'Q23705360', 'P155', 'Q26205045', 'P156', 'Q26205047'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
	# 	]
	# ],
	# [
	# 	'Q26205047',
	# 	[
	# 		# ['Lru', "Толковый словарь В. Даля 1-е изд., том 4"],  # название элемента
	# 		# # ['P1476', 'ru:"Р—Ѵ."'],  # название
	# 		# ['P478', '"4"'],     # том
	# 		# ['P577', '+1866-01-17T00:00:00Z/09'],  # дата публикации
	# 		# ['P996', '"Толковый словарь Даля (1-е издание). Часть 4 (1866).pdf"'],  # файл с отсканированными данными
	# 		# ['P1957', '"https://ru.wikisource.org/wiki/Индекс:Толковый_словарь_Даля_(1-е_издание)._Часть_4_(1866).pdf"'],  # индексная страница Викитеки
	# 		# ['P1815', '"01003833542"'],  # идентификатор сканированного издания РГБ
	# 		# ['P361', 'Q23705360'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
	# 		['P361', 'Q23705360', 'P155', 'Q26205046'],  # часть от : Толковый словарь В. Даля  # предыдущее по порядку   # следующее по порядку
	# 	]
	# ],
]

result = ''
tab = '\t'  # Табуляция - разделитель значений внутри строки, по формату инструмента Quick_statements
br = '\n'
for private_claims_item in private_claims:
	list = []
	if do_create_new_items:
		list = ['CREATE']                              # Создаёт новый элемент
		item_number = 'LAST'
	else:
		item_number = private_claims_item[0]
	for claim in common_claims:
		list.append(item_number + tab + tab.join(claim))  # 'LAST' - добавление свойства к созданному элементу
	for claim in private_claims_item[1]:
		list.append(item_number + tab + tab.join(claim))
	result += br + br.join(list)                 # Новая строка - разделить команд и claims
print(result)