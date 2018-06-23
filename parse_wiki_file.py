# -*- coding: utf-8 -*-
import re
import sqlite3
from collections import namedtuple
import pywikibot
import mwparserfromhell as mwp
import requests
from urllib.parse import urlparse, parse_qs, parse_qsl, unquote, quote
from lxml.html import fromstring
import vladi_commons
import lib_for_mwparserfromhell


FI = '/home/vladislav/Загрузки/Викитека-20171212174958.xml'

text = vladi_commons.file_readlines(FI)
wikicode = mwp.parse(text)

tplname = 'статья в словнике3'
tpls = lib_for_mwparserfromhell.listtpls(wikicode, tplname)

