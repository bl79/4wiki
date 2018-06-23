def j():
	# word = 'ВЕСЬ'
	word = 'ВБ'
	# local list = 'А АЛМ АРА Б БАР БИН БРА В ВАР Вессел ВЛА ВОО Г ГЕМ ГОР ДВА ДИО'
	# --local v = mw.text.split(list, '%s+')
	v = ['БРА', 'В', 'ВАР', 'Вессел', 'ВЛА', 'ВОО', 'Г', 'ГЕМ', 'ГОР', 'ДВА',
		 'ДИО']

	n = 0
	for c in v:  # -- перебор томов
		i = 0
		# bukva = c[i]
		for b in c:  #-- перебор букв тома
			volume_letter = v[n][i]
			volume_lettercode = v[n][i].encode('utf8')  # mw.ustring.codepoint(mw.ustring.upper(v[n]), i)  #-- в томе

			for word_letter in word:
				word_lettercode = word_letter.encode('utf8')  # mw.ustring.codepoint(word, i)  #-- взятие utf8-кода букв по порядку, в слове
				# if word_lettercode:
				if word_lettercode >= volume_lettercode:

					if not v[n + 1]: return n   #-- если последний том

					lennext = len(v[n + 1])
					if i < len(v[n + 1])-1:
						nextvolume_letter = v[n+1][i]
						nextvolume_lettercode = v[n+1][i].encode('utf8')  # mw.ustring.codepoint(mw.ustring.upper(v[n + 1]), i)
						# if nextvolume_lettercode:
						if word_lettercode < nextvolume_lettercode:
							if i == 0: break
							else: return n
						# elif i == 0: break
					# else: return n
				w += 1
			i += 1
		n += 1
	pass

print(j())
pass
