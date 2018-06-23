local word = 'ВЕСЬ'
--local list = 'А АЛМ АРА Б БАР БИН БРА В ВАР Вессел ВЛА ВОО Г ГЕМ ГОР ДВА ДИО'
--local v = mw.text.split(list, '%s+')
local v ={'А', 'АЛМ', 'АРА', 'Б', 'БАР', 'БИН', 'БРА', 'В', 'ВАР', 'Вессел', 'ВЛА', 'ВОО', 'Г', 'ГЕМ', 'ГОР', 'ДВА', 'ДИО'}
local word_lettercode, volume_lettercode, nextvolume_lettercode

for n = 1, #v do -- перебор томов
    for i = 1, #v[n] do -- перебор букв тома
        word_lettercode = mw.ustring.codepoint(word, i) -- взятие utf8-кода букв по порядку, в слове

        if word_lettercode then
            print('letter=' .. word_lettercode)
            volume_lettercode = mw.ustring.codepoint(mw.ustring.upper(v[n]), i) -- в томе

            --return volume_lettercode



            if word_lettercode >= volume_lettercode then

                print('letter=' .. volume_lettercode .. word_lettercode)

                if not v[n + 1] then return n end -- если последний том

                nextvolume_lettercode = mw.ustring.codepoint(mw.ustring.upper(v[n + 1]), i)
                if nextvolume_lettercode then

                    if word_lettercode < nextvolume_lettercode then

                        --return n
                    end
                    --else 	return n
                end
            end
            -- else return n
        end
    end
end