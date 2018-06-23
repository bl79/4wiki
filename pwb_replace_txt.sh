#!/bin/sh
# https://www.mediawiki.org/wiki/Manual:Pywikibot/replace.py
#
# python c:\pwb\pwb.py replace -family:"commons" -file:"h.txt" "[[Category:Great Soviet Encyclopedia]]" "" {{cc-by-sa-4.0}} {{PD-old-70}}

python3 ~/pwb/pwb.py replace -family:wikisource -page:"Обсуждение:Большая советская энциклопедия/для заливки/том 7" -regex -multiline "^(==+)\s*(.*?)( #.*?)?\s*(==+)$" "\1 [[БСЭ1/\2|\2]]\3 \4" -summary:"заголовки-ссылки" -always -user:Vladis13
# -simulate
