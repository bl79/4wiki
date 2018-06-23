import re
p = [
	{'text': '<p>&aaa</p>'},
	{'text': '<p>&kkk</p><p>bbbb</p><p>&jjj</p><strong><p>&hhh</p><p>mmm</p></strong>'},
	{'text': '<p>&hhh</p>'},
]
d = []
for row in p:
	found = re.findall('((?:<strong>|<em>)?<p>&[^&]+</p>(?:</strong>|</em>)?)', row['text'])
	for f in found:
		d.append(f)
		# [o + y for y in ]
		# i = m.index('t')
		# m.insert(i+1, 'bb')
		# print(m)
print(d)