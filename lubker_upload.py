# coding: utf-8
from lxml.html import tostring
import re
import csv
from unidecode import unidecode
import unicodedata
import w3lib.html
from vladi_commons.file_helpers import json_store_to_file, json_data_from_file, file_savelines

CSV_FILE = '/home/vladislav/workspace/temp/lubker/lubker-original.csv'
CSV_OUTFILE = '/home/vladislav/workspace/temp/lubker/lubker_clean.csv'
JSON_FILE = '/home/vladislav/workspace/temp/lubker/from_ancienhome2.json2'
# JSON_FILE = '/home/vladislav/workspace/temp/lubker/from_ancientrome.ru.json'

csv_colnum = None
csv_skip_firstline = True
"""
<p>•Decemviri,</p>
<p>правительственная  <a class="page" href="http://onlineslovari.com/realnyiy_slovar_klassicheskih_drevnostey/page/kollegiya.2926/">коллегия</a>, состоявшая из 10-ти человек; смотря по обязанностям Д., различались следующие роды их: 1) Decemviri agris dividundis, временная комиссия для раздела казенных земель (ager publicus). <em>Liv. </em>31, 4; 2) D. legibus scribendis или ferendis, комиссия, избранная по предложению (lex) народного трибуна Терентилья Арсы в 451 г. до Р. X. из сословия патрициев, для письменного изложения законов, освещенных обычаем, с целью ограничить и судейский произвол консулов. Вместе с тем это учреждение служило превосходным средством к сближению двух сословий, патрициев и плебеев, уравнением их перед законом. Все остальные правительственные должности, не исключая и трибунов (а также и право provocationis) на время были упразднены, так что один из Д. управлял государством и в особенности руководил судопроизводством, а остальные 9, как главною своею обязанностью, заняты были редакцией законов. Чередовались ли они через 10 дней в управлении государством, как утверждает Рейн, или давалась эта верховная власть каждому лишь на один день, пока по истечении 10-ти дней не наступала снова для него очередь, как думают другие,- это зависит от того, в каком смысле понимать слова Тита  <a class="page" href="http://onlineslovari.com/realnyiy_slovar_klassicheskih_drevnostey/page/liviya.3352/">Ливия</a> (3, 33) decumo die ius populo singuli reddebant. Очередной praefectus iuris (<em>Liv. 3, </em>33) пользовался знаками отличия, присвоенными правящему консулу (12 fasces), а прочие децемвиры имели только по одному служителю (accensus). В первый год было изготовлено 10 таблиц законов. При составлении их, по преданию, оказал свое содействие (interpres legum) некто  <a class="page" href="http://onlineslovari.com/realnyiy_slovar_klassicheskih_drevnostey/page/germodor.1568/">Гермодор</a>, философ, бежавший из  <a class="page" href="http://onlineslovari.com/realnyiy_slovar_klassicheskih_drevnostey/page/efes.7433/">Эфеса</a>. <em>Plin. h. n. </em>34, 11. <em>Pompon. de orig. iuris </em>1, 4. <em>Cic. tusc. </em>5, 36. Начертанные законы предварительно представлены были на публичное обсуждение (<em>Liv</em>. 3, 34), затем, после сделанных в них исправлений, одобрены в народном собрании (comitia centuriata), написаны на медных таблицах и выставлены на месте, назначенном для народных собраний (comitium). Тогда оказалась необходимость еще в двух дополнительных таблицах, а потому власть децемвиров была продолжена и на следующий, 450 г. до Р. X. Однако Д. по окончании срока своей, законом утвержденной власти (potestas) не пожелали сложить с себя должность, а удерживали ее за собою незаконным образом (patentia) и на 449 г., конечно, не без тайного соизволения на это патрициев, которым ненавистна была трибунская власть, на то время упраздненная. Последовавший по поводу насильственных действий Аппия, главы Д., против  <a class="page" href="http://onlineslovari.com/realnyiy_slovar_klassicheskih_drevnostey/page/virginii.1266/">Виргинии</a> выход народа (secessio plebis) на Священную гору положил конец их власти; был восстановлен законный порядок управления, и делами республики по-прежнему стали заведовать два консула. Аппий и Оппий сами себя лишили жизни в темнице, остальные же 8 Д. были изгнаны из Рима, а имения их конфискованы. <em>Liv. 3, </em>44-58; 3) Decemviri stlitibus iudicandis, древнейшая  <a class="page" href="http://onlineslovari.com/realnyiy_slovar_klassicheskih_drevnostey/page/kollegiya.2926/">коллегия</a> судей, значение которой представляет своего рода загадку; они решали дела о свободе, о праве гражданства и т. п. На основании leges Valerise Horatisc они вместе с трибунами и плебейскими эдилами объявлены были неприкосновенными (sacrosancti) и, судя по этому, были судьями в делах плебеев. Знаком их судебной власти был жезл, hasta (hastae praeesse). Сюда относящиеся места древних писателей следующие: <em>Liv</em>. 3, 55. <em>Cic. Саесin. </em>33. <em>pro dom. </em>29 <em>legg. 3, 3. Varr. l. l. </em>9, 85. <em>Digest.</em> 1, 1, 2. Август сделал их председателями суда центумвиров, iudicium centumvirale, и избирал их из сословия всадников. В этом виде должность сохранилась очень долго. <em>Suet. Oct. </em>36. <em>Dio Cass. </em>54, 26. <em>Plin. ер. </em>5, 21. <em>Spart. Hadr. 2. </em>Ср.: К. A. Schneider, de centumviralis iudicii apud Romanos origine. Zumpt, über den Ursprung des Centumviralgerichts; 4) Decemviri sacrorum, см. Divinatio.</p>

"""

re_clean_striptags = re.compile(r'^<[^>]+>\s*(.*?)\s*</[^>]+>$', flags=re.DOTALL)
re_clean_text_doublespaces = re.compile(r' {2,}')
def clean_striptags(s):
	return re_clean_striptags.search(s).group(1)
def clean_doublespaces(s):
	return re_clean_text_doublespaces.sub(' ', s).strip()



# def find_value_of_dict_by_key_in_list(d, key, ):
# 	if d.get(fromKey_pagename_in_url) == url_pn:


def csv_dict_writer(CSV_OUTFILE, fieldnames, data):
	with open(CSV_OUTFILE, "w", newline='') as out_file:
		writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
		writer.writeheader()
		for row in data:
			writer.writerow(row)


def chunks(lst, count):
	# """Разделить список на число частей."""
	start = 0
	for i in range(count):
		stop = start + len(lst[i::count])
		yield lst[start:stop]
		start = stop


def lat_no_diakritiks(s):
	return unidecode(s) if re.search(r"^[A-Z]", s, flags=re.I) else s


def urls_to_wikilink_by_dict(text, lst_of_pages, fromKey_pagename_in_url='filename', toKey_target_anchor='title'):
	re_url = re.compile(r'<a class="page" href="[^">]+page/([^/ "]+)/?" *>(.*?)</a>')
	urls_found = re_url.findall(text)
	for url_pn, anchor in urls_found:
		for d in lst_of_pages:
			if url_pn == d.get(fromKey_pagename_in_url):
				wikipagename = d.get(toKey_target_anchor)
		u = r'<a class="page" href="[^">]+page/%s/?" *>%s</a>' % (url_pn, anchor)
		try:
			text = re.sub(u, '[[РСКД/%s|%s]]' % (wikipagename, anchor), text)
		except:
			print('errorin page: ' + anchor + ' text: ' + text)
	return text


def urls_to_wikilink_by_dict_ancientrome(text, lst_of_pages, fromKey_pagename_in_url='filename', toKey_target_anchor='title_original'):
	urls_found = re.findall(r'(<a [^>]*href="[^">]+/dictio/[^">]+a=([^/ "]+)"[^>]*>(.*?)</a>)', text)

	for full_str, url_pn, anchor in urls_found:
		s = url_pn.split('#')
		for d in lst_of_pages:
			pagename_in_url = d.get(fromKey_pagename_in_url)
			if s[0] == pagename_in_url:
				pagename_target = d.get(toKey_target_anchor)
				# u = r'<a class="page" href="[^">]+page/%s/?" *>%s</a>' % (url_pn, anchor)
				try:
					if not s[1].startswith('sel='):
						pagename_target = pagename_target + '#' + s[1]
				except:
					pass
				text = text.replace(full_str, '[[РСКД/%s|%s]]' % (lat_no_diakritiks(pagename_target), anchor))
				break
		# try:
		# 	text = re.sub(full_str, '[[РСКД/%s|%s]]' % (wikipagename, anchor), text)
		# except:
		# 	print('errorin page: ' + anchor + ' text: ' + text)
	return text


# re_title_origein = re.compile(r'^\s*<p>[\s•]*(.*?)(,|\s+или|[\s\n]*</p>[\s\n]*<p>)')
re_title_string_replace = re.compile(r'^<p>(.*?)</p>[\s\n]*<p>', flags=re.DOTALL)
re_clean_text_prefixchar = re.compile(r'^<p>[\s•]*')
# re_clean_text_prefixchar = re.compile(r'^<p>[\s•]*')




def split_items_per_artiles(csv_iter):
	# разделение статей
	d = []
	for row in csv_iter:
		# if row['filename'] != 'avgila.32': continue
		foundall = re.findall('((?:<strong>|<em>)?<p>\s*•[^•]+</p>(?:</strong>|</em>)?)', row['text'])
		# if len(foundall) >1:
		# 	pass
		for found in foundall:
			i = foundall.index(found)
			d.append({
				'filename': row['filename'] if i == 0 else '',
				'text': found,
				'url_article': row['url_article'] if i == 0 else '',
				'title': row['title'] if i == 0 else '#no_rus_title %s' % str(i)
			})
		pass
	pass
	return d


pass




def clean_csv(csv_iter, csv_url2wiki_names=None):
	# предварительная частка csv
	for row in csv_iter:
		# if row['filename'] != 'amvrosiya.326': continue
		text_new = row['text']
		text_new = re.sub('</p>\n*<em>\n*<p>', '</p><p><em>', text_new)
		text_new = re.sub('</p>\n*<strong>\n*<p>', '</p><p><strong>', text_new)
		row['text'] = text_new

	# предварительная частка csv
	for row in csv_iter:
		# if row['filename'] != 'amvrosiya.326': continue
		text_new = row['text']
		text_new = re.sub('</p>\n*<em>\n*<p>', '</p><p><em>', text_new)
		text_new = re.sub('</p>\n*<strong>\n*<p>', '</p><p><strong>', text_new)
		text_new = text_new.replace('<strong></strong>', '').replace('<b></b>', '').replace('<em></em>', '')
		# чистка двойных пробелов
		text_new = re_clean_text_doublespaces.sub(' ', text_new.strip())
		# викификация url
		# csv_iter_full = vladi_commons.read_csv_dict(CSV_FILE)
		if csv_url2wiki_names:
			text_new = urls_to_wikilink_by_dict(text_new, csv_url2wiki_names)
		else:
			text_new = urls_to_wikilink_by_dict(text_new, csv_iter)
		#
		text_new = re_clean_text_prefixchar.sub('<p>', text_new)
		text_new = text_new.replace('</p>\n<p>', ' </p><p>')
		text_new = re_title_string_replace.sub(r'<p>\1 ', text_new)  # r'^<p>(.*?)[\s\n]*</p>[\s\n]*<p>',
		row['text'] = re_clean_text_doublespaces.sub(' ', text_new)
	# print(text_new)
	return csv_iter


def clean_csv_ancientrome(dic, csv_url2wiki_names=None):

	dic = make_titles_original(dic)

	# предварительная частка csv
	for row in dic:
		# if row['filename'] != 'amvrosiya.326': continue
		text_new = row['text']
		# text_new = clean_striptags(text_new)
		text_new = clean_doublespaces(text_new)
		text_new = re.sub('</p>\n*<em>\n*<p>', '</p><p><em>', text_new)
		text_new = re.sub('</p>\n*<strong>\n*<p>', '</p><p><strong>', text_new)
		#
		text_new = text_new.replace('­', '')
		text_new = re.sub(r'</i>([. ]+)<i>', r'\1', text_new).replace('</i>.', '.</i>')
		text_new = re.sub(r'<a (?:id|name)="(.*?)"></a>', r'{{якорь|\1}}', text_new)
		text_new = re.sub(r'<a href="http://ancientrome.ru/(?:art|antlitr|dictio/dict.htm\?let=)[^>"]+"[^>]*>(.*?)</a>', r'\1', text_new)
		# text_new = re.sub(r'<font class="gr">(.*?)</font>', r'{{lang|gr|\1}}', text_new)
		text_new = re.sub(r'<font class="gr">(.*?)</font>', r'\1', text_new)
		text_new = re.sub(r'<(?:font|span) class="pr2">(.*?)</(?:font|span)>', r'{{razr2|\1}}', text_new)
		text_new = re.sub(r'([^ ])\{\{razr2\| ', r'\1 {{razr2|', text_new)
		text_new = re.sub(r'<font class="kav">(.*?)</font>', r'\1', text_new)
		text_new = re.sub(r'<font color[^>]+>(.*?)</font>', r'{{№|\1}}', text_new)
		text_new = w3lib.html.remove_comments(text_new)

		text_new = re.sub(r'^<p><strong>[А-ЯЁ\W]+</strong></p>\s*', '', text_new, flags=re.IGNORECASE)
		text_new = re.sub(r'\r\n', r'\n', text_new)
		text_new = re.sub(r'<p>(.*?)</p>', r'\n\n\1', text_new, flags=re.DOTALL)
		text_new = re.sub(r'\n\n+', r'\n\n', text_new)
		text_new = text_new.replace('<br>', '\n')

		if '<table' in text_new:
			text_new = re.sub(r'$', r'{{img}}', text_new)

		row['text'] = text_new.strip()

		if row.get('pagenum'):
			row['pagenum'] = row['pagenum'][0]
		# row['title'] = row['title'].strip("',.• \t")
		row['title'] = row['title'].strip("',.• \t")



	# предварительная частка csv
	for row in dic:
		# if row['filename'] != 'amvrosiya.326': continue
		text_new = row['text']
		text_new = re.sub('</p>\n*<em>\n*<p>', '</p><p><em>', text_new)
		text_new = re.sub('</p>\n*<strong>\n*<p>', '</p><p><strong>', text_new)
		text_new = text_new.replace('<strong></strong>', '').replace('<b></b>', '').replace('<em></em>', '')
		# чистка двойных пробелов
		text_new = re_clean_text_doublespaces.sub(' ', text_new.strip())
		# викификация url
		# csv_iter_full = vladi_commons.read_csv_dict(CSV_FILE)
		if csv_url2wiki_names:
			text_new = urls_to_wikilink_by_dict_ancientrome(text_new, csv_url2wiki_names)
		else:
			text_new = urls_to_wikilink_by_dict_ancientrome(text_new, dic)
		#
		text_new = re_clean_text_prefixchar.sub('<p>', text_new)
		text_new = text_new.replace('</p>\n<p>', ' </p><p>')
		# text_new = re_title_string_replace.sub(r'<p>\1 ', text_new)  # r'^<p>(.*?)[\s\n]*</p>[\s\n]*<p>',
		row['text'] = re_clean_text_doublespaces.sub(' ', text_new)
	# print(text_new)
	return dic

# CSV_FILE_2 = '/home/vladislav/workspace/temp/lubker/rus_wordlist_from_site.csv'
# csv_iter = vladi_commons.read_csv_dict(CSV_FILE_2)
# # csv_iter = split_items_per_artiles(csv_iter)
# pass
# csv_url2wiki_names = vladi_commons.read_csv_dict(CSV_FILE)   # для викификации url
# csv_new = clean_csv(csv_iter, csv_url2wiki_names)
# keys = csv_iter[0].keys()
# CSV_OUTFILE_2 = '/home/vladislav/workspace/temp/lubker/wordlists.csv'
# csv_dict_writer(CSV_OUTFILE_2, keys, csv_iter)

re_clean_empty_tags = re.compile(r'<(strong|b|em)></(strong|b|em)>')


def make_titles_original(dict):
	import w3lib.html
	# re_title_string = re.compile(r'^<p>(.*?)([,.<]|\s+\(|\s+(или|и) |\s+\d|[\s\n]*</p>)')
	re_title_string = re.compile(r'^(?:\{\{(?:№|якорь|№).*?\}\})*[\[\]\W\d]*(.*?)([,.<—]|[А-ЯЁ]|\s+\(|\s+(или|и) |\s+\d|$)', flags=re.I)
	for row in dict:
		# try:
		text_new = row['text']
		# text_new = clean_striptags(text_new)



		#
		# tags_p = re.findall(r'<p>(.*?)</p>', text_new, flags=re.DOTALL)
		# for row in tags_p:
		# 	s = w3lib.html.remove_tags(row)
		# 	w = re.search(r'^[\W\d]*([^А-ЯЁ].*?)', s, flags=re.IGNORECASE)
		# 	if w:
		# 		row['title_original'] = w.group(1).strip("',.• ")
		# 		break

		text_new_plain = w3lib.html.remove_tags(text_new)
		for r in text_new_plain.splitlines():
			# title_original =
			if re.search(r'^[\[\]\W\d«]*[^А-ЯЁ]', r, flags=re.IGNORECASE|re.MULTILINE):
				# o = title_original.group(1)
				title_original = re_title_string.search(r)
				n = title_original.group(1)
				row['title_original'] = n.strip("',.• \t")
				break

			# title_string = re_title_string.search(text_new_plain).group(1)
			# title_string = title_string.group(1).strip("',.• ")
			# title_original = re.sub(r'(<font.*?>)?(.*?)(</font>)?', r'\1\2\3', title_string.group(1).strip("',.• "))
			# row['title_original'] = title_string.strip("',.• ")

		# 	pass
		# except:
		# 	print(row)
	return dict

def make_wordlist_textovka(csv_iter):
	wordlist = []
	re_title_string = re.compile(r'^<p>(.*?)([,.<]|\s+\(|\s+(или|и) |\s+\d|[\s\n]*</p>)')

	# обработка
	for row in csv_iter:
		# if row['filename'] != 'dares.1843': continue
		# row['text'] = """<p>Batāvi (Batavi y Lucan. 1, 431),</p>\n<p>Βαταυοί, Βατάουοι, народ, вышедший из Германии и поселившийся сначала на острове, образуемом Рейном, Вагалием и Мозой, так называемый insula Batavorum (<em>Tac. Germ. </em>29. <em>hist. </em>4, 12. <em>Caes. b. g. </em>4, 10); потом он распространился далее к югу и земля их стала называться Батавией. Из городов следует назвать: Batavodurum или Noviomagus (н. Пимвеген) на Вагалии, крепости Arenacum, Arenatium (н. Арнгейм), Trajectum (н. Утрехт) на Рейне, Lugdunum Batavorum недалеко от устьев Рейна - самый значительный город (н. Лейден). Римляне смотрели на Б. сначала не как на побежденных, но скорее как на союзников, и Б. оказывали им большую помощь во время германских войн, особенно своей превосходной конницей. <em>Tac. апп. </em>2, 8. <em>hist. </em>4, 12, 17. <em>Germ. </em>29. Но мало-помалу зависимость становилась для них обременительной, и когда исчезла вера в непобедимость римского оружия, в Батавии происходили неоднократно восстания; значительнейшим из них было восстание при Веспасиане 69-70 гг. от Р. X., под предводительством Клавдия <a class="page" href="http://onlineslovari.com/realnyiy_slovar_klassicheskih_drevnostey/page/tsivilis.7048/">Цивилиса</a>. Оно было, как известно, неудачно (<em>Tac. hist. </em>4, 12-37. 54-80. 5, 14-26); но все-таки они не платили с этих пор податей, и римляне всегда относились к ним с уважением. <em>Tac. Germ. </em>29.</p>"""
		# row['text'] = """<p>Spino,</p>\n<p>маленькая речка у Рима, которая, наравне с Альмоном, <a class="page" href="http://onlineslovari.com/realnyiy_slovar_klassicheskih_drevnostey/page/tiberin.6225/">Тиберином</a> и Нодином, призывалась в древней молитве авгуров (<em>Cic</em>. <em>п. d. </em>3, 20, 52), потому что при торжественном священнодействии нельзя было переходить рек, из которых каждая была посвящена какому-нибудь божеству <em>(Tac. ann. </em>1, 79), не совершив по поводу этого гадания (auspicium).</p>"""
		text_new = row['text']
		text_new = re_clean_text_doublespaces.sub(' ', text_new).strip()
		#
		# # text_new = re.sub(r'^<p>(.*?)[\s\n]*</p>[\s\n]*<p>', r'<p>\1 ', text_new)
		# # text_new = re_title_string_replace.sub(r'<p>\1 ', text_new)

		# text_new = text_new.replace('<strong>', "").replace('</strong>', "")

		# html → wiki
		text_new = re.sub(r'([^ ])<(em|i|b|strong)> ', r'\1 <\2>', text_new)
		text_new = re.sub(r' </(em|i|b|strong)>([^ ])', r'</\1> \2', text_new)
		text_new = re.sub(r'<(em|i|b|strong)>\(', r'(<\1>', text_new)
		text_new = re.sub(r'\)</(em|i|b|strong)>', r'</\1>)', text_new)
		text_new = re_clean_empty_tags.sub('', text_new)
		# text_new = text_new.replace('<strong></strong>', '').replace('<b></b>', '').replace('<em></em>', '')

		# text_new = text_new.replace('<p>', r'\n\n').replace('</p>', '').strip()
		text_new = text_new.replace('<em>', "''").replace('</em>', "''")
		text_new = text_new.replace('<i>', "''").replace('</i>', "''")
		text_new = text_new.replace('<b>', "'''").replace('</b>', "'''")

		text_new = text_new.replace(' ]]', "]] ")
		text_new = text_new.replace(' }}', "}} ")
		text_new = re.sub(r"(\n'''.*?''') \.", r"\1. ", text_new)
		text_new = re.sub(r"([^.,\n'])''\.", r"\1.''", text_new)
		text_new = re.sub(r"\.'' Strab.''", r". ''Strab.''", text_new)
		text_new = re.sub(r"([^'])''([.\s]+)''([^'])", r"\1\2\3", text_new)
		text_new = re.sub(r"''[HН][oо]т\.", r"''Hom.", text_new)
		text_new = re.sub(r"Hom. [тm][еe][тm]", r"Hom. mem", text_new)
		text_new = re.sub(r"''[AА][rг][rг]\.", r"''Arr.", text_new)
		text_new = re.sub(r"''[XХ][eе][nп]\.", r"''Xen.", text_new)
		text_new = re.sub(r"''[HН]dt\.", r"''Hdt.", text_new)
		text_new = re.sub(r"''[CС][uи][rг]t\.", r"''Curt.", text_new)
		text_new = re.sub(r"''[CС][uи][п]", r"''Curt.", text_new)
		text_new = re.sub(r"''[XХ][eе][nп]\. [HН][eе]ll", r"''Xen. Hell", text_new)
		text_new = re.sub(r" р\. (\d)", r" p. \1", text_new)
		text_new = re.sub(r"(\d)'' ", r"\1 ''", text_new)

		# +ссылки после " см. "
		for s in re.findall(r'см\. ([\w]+)', text_new):
			if s in ['это', 'пример', 'толковат', 'рис', 'также', 'примеч']: continue
			text_new = re.sub(r'см\. %s' % s, r'см. [[РСКД/%s|%s]]' % (lat_no_diakritiks(s), s), text_new)
		for s in re.findall(r'см\. \{\{razr2\|([\w]+)\}\}', text_new):
			text_new = re.sub(r'см\. \{\{razr2\|%s\}\}' % s, r'см. {{razr2|[[РСКД/%s|%s]]}}' % (lat_no_diakritiks(s), s), text_new)

		# первый термин в bold
		text_new = re.sub(r"^([\w ]+\w[,.]?)", r"'''\1'''", text_new)

		text_new = re.sub(r'<img [^>]*src="[^>" ]*/([^>" .]+).([^>" ]+)"[^>]*width="([^>" ]+)"[^>]*>', r"[[File:\1 (RDCA).\2|\3px]]", text_new)

		if row.get('prim'):
			p = row['prim'][0]
			p = w3lib.html.remove_tags(p, which_ones=('div', 'br'))
			p = w3lib.html.remove_comments(p)
			p = p.replace('<i>(Прим. ред. сайта)</i>', '').replace('<i>(Прим. ред. сай­та)</i>', '').replace('<b>ПРИМЕЧАНИЯ</b>', '').replace(
				'<b>ПРИМЕЧАНИЯ РЕДАКЦИИ САЙТА</b>', '')
			p = p.replace('<br>','').replace('<p></p>','').replace('<li></li>','').replace('<span class="z1"></span>','')
			p = re.sub(r'<font class="gr\d?">(.*?)</font>', r'\1', p)
			text_new = re.sub(r'<sup><a [^>]*href=\"#n.*?</a></sup>',
							  r'{{примечание ВТ|%s}}' % p.strip(), text_new)
			text_new = re.sub(r'$', r'\n\n{{примечания ВТ}}', text_new)
			print(p)
			pass
		# text_new = re.sub(r'\{\{примечание ВТ\|(?:<br>|<p></p>|<li></li>)\}\}',						  r'{{примечание ВТ|%s}}' % p.strip(), text_new)
		# text_new = text_new.replace('<i>(Прим. ред. сайта)</i>','').replace('<b>ПРИМЕЧАНИЯ</b>','').replace('<b>ПРИМЕЧАНИЯ РЕДАКЦИИ САЙТА</b>','')
		# row['prim'] = row['prim'].replace('<br>','')
		# text_new = text_new.replace('<p></p>','').replace('<li></li>','')
		text_new = re.sub(r'<sup><a id=\"tba\".*?</a></sup>', r'{{примечание ВТ|}}', text_new)

		# text_new = text_new.replace('<strong>', "'''").replace('</strong>', "'''")
		# print(text_new)
		if '#no_rus_title' in row['title']:
			row['title'] = row['title_original']


		text_new = text_new.replace('<span class="z1"></span>', '{{psp}}')
		text_new = re.sub(r'<nobr>(.*?)</nobr>', r'{{nobr|\1}}', text_new)


		text_new = text_new.replace('\xad', '')
		text_new = normalize_diakritiks(text_new)
		row['text'] = re_clean_text_doublespaces.sub(' ', text_new)

		wordlist.append([row['title'], row['title_original']])

	# CSV_OUTFILE_2 = '/home/vladislav/workspace/temp/lubker.csv'
	# csv_dict_writer(CSV_OUTFILE_2, csv_iter[0].keys(), csv_iter)

	# WORDSLIST = '/home/vladislav/workspace/temp/lubker/wordslist2.txt'
	# wordlist = sorted(wordlist, key=lambda v: v[0])
	# w = ("# {{РСКД/Словник|%s|%s|}}" % (i[0], i[1]) for i in wordlist)
	# vladi_commons.file_savelines(WORDSLIST, w)

	return csv_iter

pass

def normalize_diakritiks(t):
	import unicodedata
	t_new = unicodedata.normalize('NFD', t)
	t_new = t_new.replace('\uf008', '\u0301').replace('\uf014', '\u0313')
	t_new = unicodedata.normalize('NFC', t_new)
	return t_new

# csv_iter = vladi_commons.read_csv_dict(CSV_OUTFILE_2)
# make_wordlist_textovka(csv_iter)
pass

def make_wikipage(filename, dic, title1='title', title2='title_original', text='text', parts2separate=1):
	wiki_articles_list = []
	for i in dic:
		p = "== [[РСКД/%s|%s]] # %s ==\n%s\n" % (lat_no_diakritiks(i[title2]), i[title2], i[title1], i[text])
		if i[title2] == 'Acca Larentia':
			pass
		wiki_articles_list.append(unicodedata.normalize('NFC', p))
	lst = list(chunks(wiki_articles_list, parts2separate))
	for part in lst:
		file_savelines(filename + str(lst.index(part)), part)


dic = json_data_from_file(JSON_FILE)
# re.compile()
# for i in textovka_dic:
# 	i['text'] = re.subi['text']
# 	i['title_original'] = i['text']
# dic = make_titles_original(textovka_dic)
dic = clean_csv_ancientrome(dic)
dic = make_wordlist_textovka(dic)
json_store_to_file(JSON_FILE + '3', dic)

WIKI_OUTFILE = '/home/vladislav/workspace/temp/lubker/lubker.wiki'
make_wikipage(WIKI_OUTFILE, dic, parts2separate=5)

print(8)
pass