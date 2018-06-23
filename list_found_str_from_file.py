import vladi_commons
import re
import csv
from lxml import etree
from unidecode import unidecode
import unicodedata

t = vladi_commons.json_data_from_file(
			'/home/vladislav/workspace/temp/lubker/from_ancienhome2.json')
re_img_links = re.compile(r'<img src="([^"> ]+)"')
links = '\n'.join([u for i in t for u in re_img_links.findall(i['text'])])

# 	vladi_commons.file_savetext('/home/vladislav/workspace/temp/lubker/slovnik2.txt', w)
# w = vladi_commons.file_readtext('/home/vladislav/workspace/temp/lubker/slovnik_orig.txt')
# make_pagenums_in_wordlist(w)
pass