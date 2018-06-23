local moduleHeader = require('Module:Header')

local t = {
    ['title'] = '',
    ['currname'] = '',
    ['oldspell'] = '',
    ['tom'] = '',
    ['god_toma'] = '',
    [1] = {
        ['pagename'] = '',
        ['termin_so'] = '',
        ['termin_do'] = '',
        ['list'] = '',
        ['wordlist_str'] = '',
        ['numpage_scan'] = '',
        ['numpage_book'] = '',
        ['next'] = '',
        ['previous'] = '',
    },
    [2] = {
        ['pagename'] = '',
        ['termin_so'] = '',
        ['termin_do'] = '',
        ['list'] = '',
        ['wordlist_str'] = '',
        ['numpage_scan'] = '',
        ['numpage_book'] = '',
        ['next'] = '',
        ['previous'] = '',
    },
    [3] = {
        ['pagename'] = '',
        ['termin_so'] = '',
        ['termin_do'] = '',
        ['list'] = '',
        ['wordlist_str'] = '',
        ['numpage_scan'] = '',
        ['numpage_book'] = '',
        ['next'] = '',
        ['previous'] = '',
    },
    ['bukvi_toma'] = {
        { 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З' },
        { 'И', 'І', 'К', 'Л', 'М', 'Н', 'О' },
        { 'П' },
        { 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Ѣ', 'Э', 'Ю', 'Ѧ', 'Я', 'Ѳ', 'Ѵ' }
    }, -- в ТСД-3 буква 'Р' в 3-м томе
    ['god_toma'] = { { 1863, 1865, 1865, 1866 }, { 1880, 1881, 1882, 1882 }, { 1903, 1905, 1907, 1909 } }
}




-- Номер тома по первой букве названия статьи. На вход: 1) номер издания, 2) слово - название статьи в ДО, при умолчании берётся {{SUBPAGE}}; может даваться номер тома из [[шаблон:Tom]], который возвращается.
function tomcalc(izdanie, nazvanie)
    local str = mw.text.trim(nazvanie)
    local bukva
    if (#str == 1 and string.match(str, '%d+')) then return str --если на входе цифра возвращаем её как номер тома и выход
    else bukva = first_letter_subpage(str)
    end --если дано название то его первая буква, иначе - названия статьи
    if (bukva == 'І' or bukva == 'I') then return '2' end --Добавлена латин.'I', ибо из-за бага Lua славян. 'І' может не распознаваться.
    if (tostring(izdanie) == '3' and bukva == 'Р') then return '3' end --в ТСД-3 буква 'Р' в 3-м томе
    for tom, bukvi in pairs(t['bukvi_toma']) do
        for _, bukva_toma in pairs(bukvi) do
            if (bukva == bukva_toma) then return tom end
        end
    end
end

-- Возврат: первая буква слова статьи ({{SUBPAGE}}) в верхнем регистре. Иначе если подан входной параметр слово, то возврат его первой буквы.
function first_letter_subpage(str)
    if (str == nil or str == '' or mw.ustring.find(str, '/ДО')) then return
    --mw.ustring.upper(mw.ustring.sub(mw.title.getCurrentTitle().text,5,5))
    end
    local fb = mw.ustring.sub(str, 1, 1)
    if (fb == 'і' or fb == 'І' or fb == 'i' or fb == 'I') then return 'І' end --баг Lua с распознаванием буквы
    local _, _, b = mw.ustring.find(str, '([а-яёѣѵіѳА-ЯЁѢѴІѲѦ])')
    return mw.ustring.upper(b)
end


-- Расчитывает страницу скана по странице книге, добавляя смещение.  Возврат: стр.скана.
function pagecalc(izdanie, tom, pagebook, pagination)
    local izdanie, tom, pagination = tonumber(izdanie), tonumber(tom), tonumber(pagination)
    local poffset1, chet
    local pb = tonumber(mw.ustring.match(tostring(pagebook), '%d+')) --только первые цифры диапазона страниц
    if pb <= 0 then return end

    if izdanie == 1 then
        local offset = { 2, -626, 1, 1 } -- смещение в ТСД-1, в 4 томах
        --в 4 томе ошибка: номера 467-468 у двух пар страниц, этим сбита последующая пагинация
        if (tom == 4 and ((pb >= 469) or ((pb == 467 or pb == 468) and pagination == 2))) then poffset1 = 3 else poffset1 = offset[tom] end
        return pb + poffset1
    end
    if izdanie == 2 then
        local offset = { 90, 9, 8, 8 }
        return pb + offset[tom]
    end
    if izdanie == 3 then
        -- в ТСД-3 нумеруются колонки, а не страницы; по 2 на страницу, из них первая - нечётная
        local _, x = math.modf(pb / 2) -- проверка что чётная
        if x ~= 0 then chet = 1 else chet = 0 end
        local offset = { 17, 2, 2, 4 }
        return (pb + chet) / 2 + offset[tom]
    end
end


-- Возвращает ссылку на индекс 1—3-го издания. Параметры: номер издания (1—3), том, nazvanie_DO, страница скана, страницы книги. При неуказанной странице скана вернёт ссылку на индекс тома, при указаной — на страницу в индексе.
function indexlink(izdanie, tom, pagescan, pagebook, linkonly)
    local izdanie, tom, pagescan = tonumber(izdanie), tonumber(tom), tonumber(pagescan)
    -- при автоопределении тома по первой букве термина возникли нюансы
    local god = t[izdanie]['god']

    if (izdanie == 1) then
        if (pagescan ~= nil) then
            if (linkonly == nil) then
                return '[[Страница:Толковый словарь Даля (1-е издание). Часть ' .. tom .. ' (' .. god .. ').pdf/' .. pagescan .. '|ТСД-1 (' .. god .. ') т. ' .. tom .. ', с. ' .. pagebook .. ']]'
            else
                return 'Страница:Толковый словарь Даля (1-е издание). Часть ' .. tom .. ' (' .. god .. ').pdf/' .. pagescan
            end
        else
            if (linkonly == nil) then
                return '[[Индекс:Толковый словарь Даля (1-е издание). Часть ' .. tom .. ' (' .. god .. ').pdf|ТСД-1 (' .. god .. ') т. ' .. tom .. ']]'
            else
                return 'Индекс:Толковый словарь Даля (1-е издание). Часть ' .. tom .. ' (' .. god .. ').pdf'
            end
        end
    elseif (izdanie == 2) then
        if (pagescan ~= nil) then
            if (linkonly == nil) then
                return '[[Страница:Толковый словарь Даля (2-е издание). Том ' .. tom .. ' (' .. god .. ').pdf/' .. pagescan .. '|ТСД-2 (' .. god .. ') т. ' .. tom .. ', с. ' .. pagebook .. ']]'
            else
                return 'Страница:Толковый словарь Даля (2-е издание). Том ' .. tom .. ' (' .. god .. ').pdf/' .. pagescan
            end
        else
            if (linkonly == nil) then
                return '[[Индекс:Толковый словарь Даля (2-е издание). Том ' .. tom .. ' (' .. god .. ').pdf|ТСД-2 (' .. god .. ') т. ' .. tom .. ']]'
            else
                return 'Индекс:Толковый словарь Даля (2-е издание). Том ' .. tom .. ' (' .. god .. ').pdf'
            end
        end
    elseif (izdanie == 3) then
        if (pagescan ~= nil) then
            if (linkonly == nil) then
                return '[[Страница:Толковый словарь. Том ' .. tom .. ' (Даль ' .. god .. ').djvu/' .. pagescan .. '|ТСД-3 (' .. god .. ') т. ' .. tom .. ', с. ' .. pagebook .. ']]'
            else
                return 'Страница:Толковый словарь. Том ' .. tom .. ' (Даль ' .. god .. ').djvu/' .. pagescan
            end
        else
            if (linkonly == nil) then
                return '[[Индекс:Толковый словарь. Том ' .. tom .. ' (Даль ' .. god .. ').djvu|ТСД-3 (' .. god .. ') т. ' .. tom .. ']]'
            else
                return 'Индекс:Толковый словарь. Том ' .. tom .. ' (Даль ' .. god .. ').djvu'
            end
        end
    end
end

function make_link(prefix, pagename, text)
    return '[[' .. prefix .. pagename .. '|' .. text .. ']]'
end

-- helper: проверка переменной, возврат её или nil если пустая
function is(var)
    if (var == '' or var == nil) then return nil else return var end
end

----------------------------------------------------------------------------------------------------------

local currtitle = mw.title.getCurrentTitle() -- текущая страница
local pagename = currtitle["text"]
local currlist = currtitle["rootText"]
-- currname = 'ТСД/Алык/ДО' -- тест
local nameparts = mw.text.split(pagename, "/")
t['title'] = nameparts[2]
t['pagename'] = nameparts[1] .. nameparts[2]
if nameparts[3] == 'ДО' then t['oldspell'] = '/ДО' end

for i = 3, 1, -1 do -- izdanie
local list, wordlist_str, tom, tso, tdo, ts, previous, next, tns, tnb
list = moduleHeader.wordlist({ args = { nil, pagename, tostring(i) } })

if is(list) then
    -- list = 'А'
    t[i]['list'] = list
    wordlist_str = 'ТСД-словник/' .. list .. '/' .. tostring(i) .. '-е изд.'
    t[i]['wordlist_str'] = wordlist_str

    tom = tomcalc(i, pagename)
    t[i]['tom'] = tom

    t[i]['god'] = t['god_toma'][i][tom]


    tso = moduleHeader.title({ args = { pagename, wordlist_str, ['safe'] = true } })
    if is(tso) then t[i]['termin_so'] = tso end
    tdo = moduleHeader.title({ args = { pagename, wordlist_str, ['ДО'] = true, ['safe'] = true } })
    if is(tdo) then t[i]['termin_do'] = tdo end

    previous = moduleHeader.previous({ args = { pagename, wordlist_str, ['type'] = 'name', ['safe'] = true } })
    if is(previous) then
        t[i]['previous'] = previous
        t[i]['link_previous'] = make_link(nameparts[1] .. '/', t['previous'] .. t['oldspell'], t['previous'] .. t['oldspell'])
    end

    next = moduleHeader.next({ args = { pagename, wordlist_str, ['type'] = 'name', ['safe'] = true } })
    if is(next) then
        t[i]['next'] = next
        t[i]['link_next'] = make_link(nameparts[1] .. '/', t['next'] .. t['oldspell'], t['next'] .. t['oldspell'])
    end

    tnb = moduleHeader.pagenum({ args = { 'hard', ['name'] = pagename, ['list'] = wordlist_str } })
    if is(tnb) then t[i]['numpage_book'] = tnb end

    if is(tnb) then tns = pagecalc(i, tom, tnb) end
    if is(tns) then t[i]['numpage_scan'] = tns end

    t[i]['indexlink'] = indexlink(i, tom, tns, tnb)
end
end



-- t[3]['previous'] = moduleHeader.previous({args={'ТСД/Алык', 'ТСД-словник/А/3-е изд.', ['safe']=true}})
-- t[3]['termin_so'] = moduleHeader.title({args={'ТСД/Алык', 'ТСД-словник/А/3-е изд.', ['safe']=true}})
-- t[i]['next'] = moduleHeader.next({args={nil, pagename, wordlist_str, ['safe']=true}})

return t
