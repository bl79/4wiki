# -*- coding: utf-8 -*-
import requests
from lxml import etree, html
from urllib.parse import urlencode, quote  # python 3
import re
from vladi_commons.vladi_helpers import file_readlines, file_savetext

html_links_list = 'html_links.txt'
directory_to_save = './html_parsed/'
xpath = r'//*[@id="central_content"]'

html_links = file_readlines(html_links_list)
for pageurl in html_links:
    # html = vladi_commons.file_readtext(file_html)
    # htm = """	"""
    # html_parsed = etree.fromstring(htm)

    r = requests.get(pageurl)  # cached_html
    html_parsed = etree.HTML(r.text)

    div = html_parsed.xpath(xpath)
    if not div:
        continue
    div = str(etree.tostring(div[0], encoding='unicode'))
    # print(str(div))

    # чистка кода
    div = re.sub('''<p align *= *['"]right['"] *> Автор:.+?</p>''', '', div, re.DOTALL)
    div = re.sub('''<font size=['"]1['"] color=['"]#fff['"]>Страница сгенерирована [^<]+</font>''', '', div)

    div = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>' + div + '</body></html>'

    pagename = re.sub(r'(.+:)?(www\.)?(.+\.(ru|com|org))/', '', pageurl)
    pagename = pagename.replace('/', ' - ')
    file_savetext(directory_to_save + pagename + '.htm', str(div))

    pass
