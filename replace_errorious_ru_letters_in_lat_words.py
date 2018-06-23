import re
import vladi_commons
from unidecode import unidecode
import pywikibot

t = """
"""
SITE = pywikibot.Site('ru', 'wikisource')
TEXTOVKA_TITLE = 'РСКД/Словник по лат.-греч. алфавиту'
wp = pywikibot.Page(SITE, TEXTOVKA_TITLE)
t = wp.get()

# re.sub("s#Словник\|([^|]*[А-ЯЁ][^|]*)#РСКД/\1#igp", )

# rus - слева, lat - справа
replaces = """\
А A
В B
С C
Х X
М M
К K
Н H
Р P
О O
Т T
Е E
ь b
с c
х x
к k
а a
р p
о o
и u
у y
г r
е e
""".splitlines()
repl_letters = [r.split(' ') for r in replaces]

replaces2gr = """\
u υ
o ο
о ο
к κ
k κ
p ρ
р ρ
А Α
A Α
a α
а α
П Π
т τ
t τ
N Ν
Н Η
H Η
B Β
В Β
Г Γ
у γ
y γ
Д Δ
E Ε
Е Ε
Z Ζ
Ѳ Θ
I Ι
i ι
Л Λ
л λ
М Μ
M Μ
v ν
O Ο
О Ο
п π
Р Ρ
P Ρ
T Τ
Т Τ
Y Υ
У Υ
Ф Φ
ф φ
Х Χ
X Χ
""".splitlines()
repl_letters_2gr = [r.split(' ') for r in replaces]

# while True:
# 	foundwords = re.findall(r"РСКД/Словник\|([^|]*?[А-ЯЁ])", t, flags=re.I)
# 	if not len(foundwords):
# 		break
	# for word in foundwords:
	# 	for r in repl_letters:
	# 		word.replace(r[0], r[1])


pages2rename = set()

re_ru_in_lat = re.compile(r"РСКД/Словник\|([^Α-Ω|]*?[А-ЯЁ][^Α-Ω|]*)\|", flags=re.I)
re_lat_in_gr = re.compile(r"РСКД/Словник\|([A-Z][^|]*?[Α-Ω][^|]*?)\|", flags=re.I)
re_gr_in_lat = re.compile(r"РСКД/Словник\|([^A-Z][^|]*?[A-Z][^|]*?)\|", flags=re.I)
re_ru_in_notru = re.compile(r"РСКД/Словник\|([^|]*?[А-ЯЁ][^|]*?)\|", flags=re.I)
re_1notlat = re.compile(r"РСКД/Словник\|([^A-Z][A-Z])\|", flags=re.I)
re_1lat = re.compile(r"РСКД/Словник\|([A-Z][^|]*)\|", flags=re.I)
# words2replace = re_1notlat.findall(t)

words2replace = re_1lat.findall(t)
# words2replace = re_lat_in_gr.findall(t)
# words2replace = re_gr_in_lat.findall(t)
# words2replace = re_ru_in_notru.findall(t)
# words2replace = re_ru_in_notru.findall(t)



for s in words2replace:
	n = s
	for c in repl_letters:
		n = re.sub(c[0], c[1], n)
	n = n.replace('ў', 'y')
	n = unidecode(n)
	# s_ununi = unidecode(s1)
	# s1 = str(s_ununi.encode("ascii"))
	if s != n:
		pages2rename.add('РСКД/%s\nРСКД/%s' % (s, n))
	t = t.replace("РСКД/Словник|%s" % s, "РСКД/Словник|%s" % n)


vladi_commons.file_savelines('pages2rename_mix_gr.txt', pages2rename)

pass
#
# for r in repl_letters:
# 	words2replace = re.findall(r"РСКД/Словник\|([^|]*?[А-ЯЁ])", t, flags=re.I)
# 	for word in words2replace:
# 		word_new = re.sub(r"(РСКД/Словник\|[^|]*)%s" % r[0], r"\1%s" % r[1], t, flags=re.I)
# 	t_new = re.sub(r"(РСКД/Словник\|[^|]*)%s" % r[0], r"\1%s" % r[1], t, flags=re.I)
# 	pass


pass

