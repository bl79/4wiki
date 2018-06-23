import vladi_commons
import re
import csv
from unidecode import unidecode
import unicodedata

def make_pagenums_in_wordlist(w):
	textovka_dic = vladi_commons.json_data_from_file('/home/vladislav/workspace/scrapy/lubker/from_ancienhome2.json2')
	for i in textovka_dic:
		if re.search(r"^[A-Z]", i['title_original'], flags=re.I):
			t = unidecode(i['title_original'])
		else:
			t = i['title_original']
		t = unicodedata.normalize('NFC', t)
		if not i.get('pagenum'):
			i['pagenum'] = ''
		w = re.sub(r'словнике3\|%s\|([^|}]+)\|\}' % t, r'словнике3|%s|%s|%s}' % (t, i['title'], i['pagenum']), w)
		if t not in w:
			print(t)
			w = w + '\n# {{статья в словнике3|%s|%s|%s}}' % (t, i['title'], i['pagenum'])

	pass
	vladi_commons.file_savetext('/home/vladislav/workspace/temp/lubker/slovnik2.txt', w)
w = vladi_commons.file_readtext('/home/vladislav/workspace/temp/lubker/slovnik_orig.txt')
make_pagenums_in_wordlist(w)



# создание списка страниц-переменований для gwb
lst = []
for word in re.findall(r'словнике3\|(Έ[^|}]+)\|', w):
	lst.append('РСКД/' + word)
	lst.append('РСКД/' + word.replace('Έ', 'Ἐ'))
vladi_commons.file_savetext('/home/vladislav/workspace/4wiki/pages2rename4.txt', '\n'.join(lst))
