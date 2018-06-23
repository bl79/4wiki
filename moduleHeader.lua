local p = {}

local currtitle = mw.title.getCurrentTitle()
local currname = currtitle["text"]
local currlist = currtitle["rootText"]
local beed = require ('Module:BEED')
local issub = false 						-- Для p.subnav()

-- helper
-- проверка переменной, возврат её или nil если пустая
function is(var)
	if (var == '' or var == nil) then return nil  else return var end
end

function p.beed (frame)
	local args = frame.args
	local t = currname or ""
	local title, b_old_spell, new_style, prefix, n, n2
	t = mw.text.split (t, "/")
	-- Разбор имени статьи: ЭСБЕ/<title>[/<part>/...][/ДО]
	if t[1] ~= 'ЭСБЕ' then
		return
	end
	if t[2] == "ДО" or t[2] == "ВТ" then
		title = t[3]
		b_old_spell = (t[2] == "ДО")	-- Если имя статьи начинается на "ЭСБЕ/ДО/"
		new_style = true
		n2 = word_list (nil, nil, "А:83 Г:84 Кош:85 Прусс:86")
		prefix = frame:preprocess ('Энциклопедический словарь Брокгауза и Ефрона/{{ЕДО|ДО|ВТ}}/Словник')
	else
		title = t[2]
		b_old_spell = (t[#t] == "ДО")	-- Если имя статьи оканчивается на "/ДО"
	end
	-- Параметр НАЗВАНИЕ
	local name = args.name
	if name == '' or name == nil then
		name = title
	end
	-- Параметр СЕКЦИЯ
	local section = args.section
	if section == '' or section == nil then
		section = title
	end
	-- Ключ сортировки для {{DEFAULTSORT:}}
	local lang = mw.language.new ('ru')
	local key = lang:ucfirst ( name )
	local firstletter = lang:uc ( mw.ustring.sub ( key, 1, 1 ) )
	-- Ищем месторасположение статьи в сканах
	-- в основных томах:
	local b1 = p.beedScan (frame, 1)  -- том/страница
	local d1 = nil					  -- файл_djvu/страница
	if b1 then
		if b1:find ( "%d+/%d+" ) then
			d1 = beed.djvu (b1)
		end
	end
	-- в дополнительных томах:
	local b2 = p.beedScan (frame, 2)  -- том/страница
	if new_style then b2 = p.beedScan (frame, 1, prefix .. '/' .. n2) end
	local d2 = nil					  -- файл_djvu/страница
	if b2 then
		if b2:find ( "%d+/%d+" ) then
			d2 = beed.djvu (b2)
		end
	end
	-- навигационные ссылки и категории
	local previous, next, subnav, wordlist, categories, contents
	if new_style then
		n = word_list ()
		if b_old_spell then
			if args.name == '' or args.name == nil then name = p.title (frame, prefix .. '/' .. n ) end
			categories = '[[Категория:ЭСБЕ:Дореформенная орфография]][[Категория:ЭСБЕ:ДО:' .. firstletter .. ']]'
			if args.pages ~= 'нет' then contents = '\n' .. beed.transclude ( frame, b1, b2, section, b_old_spell) else contents = '' end
		else
			categories = '[[Категория:ЭСБЕ]][[Категория:ЭСБЕ:' .. firstletter .. ']]'
			if args.pages ~= '' then contents = '\n' .. beed.transclude ( frame, b1, b2, section, b_old_spell) else contents = '' end
		end
		if b1 and b2 then
			subnav = frame:expandTemplate { title = 'ЭСБЕ/списки', args = { n2 } }
			subnav = p.subnav (frame, '[[' .. prefix .. '/' .. n2 .. '|' .. subnav .. ']]' )
		end
		wordlist = frame:preprocess ( '[[' .. prefix .. '|Список{{ЕДО|ъ}} статей ЭСБЕ]]&#x3a;&nbsp;' )
		wordlist = wordlist .. '[[' .. prefix .. '/' .. n .. '|' .. frame:expandTemplate { title = 'ЭСБЕ/списки', args = { n } } .. ']]. '
		previous = p.previous ( frame, prefix .. '/' .. n )
		next = p.next ( frame, prefix .. '/' .. n )
	else
		if b_old_spell then
			wordlist = '[[Викитека:Проект:ЭСБЕ/Словник/ДО|Списокъ статей ЭСБЕ]]&#x3a;&nbsp;[[Индекс:' .. (d1 or d2) .. '|' .. frame:expandTemplate { title = 'ЭСБЕ/Том', args = { (b1 or b2):gsub ('/.+', '') } } .. ']]. '
			previous = p.previous (frame, 'Индекс:' .. (d1 or d2) )
			next = p.next (frame, 'Индекс:' .. (d1 or d2) )
			if args.name == '' or args.name == nil then name = p.title (frame, 'Индекс:' .. (d1 or d2) ) end
			if b1 and b2 then
				subnav = frame:expandTemplate { title = 'ЭСБЕ/Том', args = { b2:gsub ('/.+', '') } }
				subnav = p.subnav (frame, '[[Индекс:' .. d2 .. '|' .. subnav .. ']]' )
			end
			categories = string.format ( '[[Категория:ЭСБЕ:Дореформенная орфография]][[Категория:ЭСБЕ:ДО:%s]]', firstletter )
			if args.pages ~= 'нет' then contents = '\n' .. beed.transclude ( frame, b1, b2, section, b_old_spell) else contents = '' end
		else
			n = word_list ()
			wordlist = '[[Викитека:Проект:ЭСБЕ/Словник|Список статей ЭСБЕ]]&#x3a;&nbsp;'
			wordlist = wordlist .. '[[Викитека:Проект:ЭСБЕ/' .. n .. '|' .. frame:expandTemplate { title = 'ЭСБЕ/списки', args = { n } } .. ']]. '
			previous = p.previous ( frame, 'Викитека:Проект:ЭСБЕ/' .. n )
			next = p.next ( frame, 'Викитека:Проект:ЭСБЕ/' .. n )
			categories = string.format ( '[[Категория:ЭСБЕ]][[Категория:ЭСБЕ:%s]]', firstletter )
			if args.pages ~= '' then contents = '\n' .. beed.transclude ( frame, b1, b2, section, b_old_spell) else contents = '' end
		end
	end
	-- сборка шаблона
	local noauthor = '<span style="font-style:normal">[[Энциклопедический словарь Брокгауза и Ефрона|Энциклопедическ{{ЕДО|і|и}}й словарь Брокгауза и Ефрона]] '
	noauthor = noauthor .. '<span id="header_override" style="display:none">[[Энциклопедический словарь Брокгауза и Ефрона|ЭСБЕ]]. [[Россия|Росс{{ЕДО|і|и}}я]], '
	noauthor = noauthor .. '[[ЭСБЕ/Санкт-Петербург, столица России|Санкт-Петербург{{ЕДО|ъ}}]], [[w:1890 год|1890]]—[[w:1907 год|1907]]</span></span>'
	noauthor = frame:preprocess (noauthor)
	local source = p.beedScan (frame, 3)
	local misc = '[[Файл:Brockhaus Lexikon.jpg|20px]] ' .. wordlist .. source .. (args.alt or '')

	local search = args.search;
	if ( not search or #search == 0 ) then
		search = name;
	end

	return frame:expandTemplate {
		title = 'Отексте',
		args = {
			['НАЗВАНИЕ'] = name,
			['НЕТ_АВТОРА'] = noauthor,
			['ДРУГОЕ'] = misc,
			['ПРЕДЫДУЩИЙ'] = previous,
			['СЛЕДУЮЩИЙ'] = next,
			['НАВИГАЦИЯ'] = subnav,
			['КАЧЕСТВО'] = args.quality,
			['НЕОДНОЗНАЧНОСТЬ'] = args.disambig,
			['ВИКИПЕДИЯ'] = args.w,
			['ВИКИТЕКА'] = args.s,
			['ВИКИСКЛАД'] = args.commons,
			['ВИКИЦИТАТНИК'] = args.q,
			['ВИКИНОВОСТИ'] = args.n,
			['ВИКИСЛОВАРЬ'] = args.wikt,
			['ВИКИУЧЕБНИК'] = args.b,
			['ВИКИВИДЫ'] = args.species,
			['ВИКИДАННЫЕ'] = args.data,
			['ВИКИГИД'] = args.voyage,
			['ПОИСК'] = search,
			['ЕЭБЕ'] = args.eebe,
			['НЭС'] = args.nes,
			['МЭСБЕ'] = args.mesbe,
			['БЭАН'] = args.bean,
			['ЭЛ'] = args.el,
			['БЭЮ'] = args.beyu,
			['РЭСБ'] = args.resb,
			['БСЭ1'] = args.bse1,
			['РБС'] = args.rbs,
			['ТЭ1'] = args.te1,
			['ТЭ2'] = args.te2,
			['ТСД'] = args.tsd,
			['ПБЭ'] = args.pbe,
			['ВЭ'] = args.ve,
			['ГСС'] = args.gss,
			['Британника'] = args.britannica,
			['ADB'] = args.adb,
			['DNB'] = args.dnb,
			['JE'] = args.je,
			['NSRW'] = args.nsrw,
			['NIE'] = args.nie
			}
		} .. categories .. frame:preprocess ( '{{DEFAULTSORT:' .. key .. '}}' ) .. '&nbsp;\n\n<div class="text" style="width:100%"><div class="innertext">' .. contents
end

function p.title (frame, lst) return makelink (frame, "title", lst); end
function p.next (frame, lst) return makelink (frame, "next", lst); end
function p.previous (frame, lst) return makelink (frame, "previous", lst); end
function p.subnav (frame, lst)
	issub = true
	local list = lst or frame.args[1]
	if list == "" or list == nil then return end
	if list:find ("headertemplate") then return list end
	if not list:find ("%[%[.-%]%]") then list = "[[" .. list .. "]]" end
	local previous = p.previous (frame, list)
	if previous == "" then previous = nil end
	local next = p.next (frame, list)
	if next == "" then next = nil end
	issub = false
	return frame:expandTemplate { title = "sub-nav", args = { previous, next, list } }
end

-- Параметр lst м.б. задан только если эта ф-ция вызывается из других ф-ций этого модуля (p.beed()), а не из шаблона или вики-страницы
function makelink (frame, rel, lst)
	local name, list, text, oldspell, type, safe = is(frame.args[1]), frame.args[2], is(frame.args[3]), is(frame.args["ДО"]), frame.args["type"], is(frame.args["safe"])
	local result, found, j

	if not name or lst then name = currname end
	if lst then list = lst elseif (list == "") or (list == nil) then list = currlist end
	if not (name and list) then return end

	name = name:gsub ("^ *%[%[(.-)%]%].*", "%1")
	name = name:gsub ("[#|].+", "")

-- Начало очень странного куска кода
	if name:find ("/ДО$") or name:find ("/ДО/") then
		oldspell = true
	else
		local nameparts = mw.text.split (name, "/")
		if nameparts[1] == "ЭСБЕ" or (nameparts[1] == "РБС" and not issub) then
			if nameparts[2] then
				if nameparts[2] == "ДО" or nameparts[2] == "ВТ" then
					name = table.concat (nameparts, "/", 1, 3)
				else
					name = table.concat (nameparts, "/", 1, 2)
				end
			end
		end
	end
-- Конец очень странного куска кода

	local t
	if safe then
		t = makelist (list, oldspell, true, name)
	else
		t = makelist (list, oldspell, false)	-- Передавать тоже name??? См. выше очень странный кусок кода
	end
	if not t then return end

	for i, v in ipairs (t) do
		if escapePattern(v[1]) == escapePattern(name) then
			found = true
			if rel == "next" then
				j = i+1
			elseif rel == "previous" then
				j = i-1
			else 	-- rel == "title"
				result = v[3] or v[2] or v[1] break
			end
			if t[j] and (t[j][1] ~= "Викитека:Граница списка в оглавлении") then
				if not text then
					if t[j][2] then
						if type == "link" then
							result = t[j][1]
						elseif type == "name" then
							result = t[j][2]
						else
							result = "[[" .. t[j][1] .. "|" .. t[j][2] .. "]]"
						end
					else
						if type == "link" or type == "name" then
							result = t[j][1]
						else
							result = "[[" .. t[j][1] .. "]]"
						end
					end
				else
					if type == "link" then
						result = t[j][1]
					elseif type == "name" then
						result = text
					else
						result = "[[" .. t[j][1] .. "|" .. text .. "]]"
					end
				end
			end
			break		-- found
		end
	end


	if result then result = result:gsub ("^%[%[>", "[[") end

	if found then
		return escapePattern(name)
	else
		if safe then
			return t[1][2]
		else
			error ( string.format ('Страница «%s» в оглавлении «%s» не найдена', name, list))
		end
	end
end

-- тест-функция, возвращает результат парсинга функции makelist, параметры те же.
-- пример вызова: {{#invoke:Header|makelist|ТСД-словник/А/3-е изд.|true|true}}
function p.makelist (frame)
	local l = ''
	local t = makelist ('ТСД-словник/А/3-е изд.', true, true)
	for k, v in pairs( t ) do
	    l = l  .. '<br>' ..  table.concat(v, ', ')
	end
	return l
end

function makelist (listname, oldspell, safe, titlename)
	local result
	if (listname == "") or (listname == nil) then error ('Оглавление не указано') end
	listname = string.gsub (listname, "^ *%[%[(.-)%]%].*", "%1")
	listname = string.gsub (listname, "[#|].+", "")
	local title = mw.title.new (listname)
	if not title then error ('Недопустимое имя оглавления: ' .. listname) end
	local page = title["getContent"]
	local x = page(title)
	if not x then
		if safe then
			return
		else
			error ( string.format ('Оглавление «%s» не найдено', title.text ))
		end
	end
	-- Подстановка переменных
	x = x:gsub("{{PAGENAME}}", title.text)
	x = x:gsub("{{НАЗВАНИЕ_СТРАНИЦЫ}}", title.text)
	-- Шаблоны-ссылки в простыеparse_title ссылки
	if (titlename == nil) or (titlename == "") then titlename = currname end
	local root = p.parse_title (titlename, "root")
	local edition = p.parse_title (titlename, "edition")

	-- маркер-граница списка (в виде шаблона)
	x = x:gsub("{{Начало списка в оглавлении}}", "[[Викитека:Граница списка в оглавлении]]")
	x = x:gsub("{{Конец списка в оглавлении}}", "[[Викитека:Граница списка в оглавлении]]")

	x = x:gsub("{{2О Статья в словнике|", "{{Статья в словнике|") -- 2О - rus. О
	x = x:gsub("{{2O Статья в словнике|", "{{Статья в словнике|") -- 2O - lat. O (alias)
	x = x:gsub("{{[Tt]sds|", "{{Статья в словнике3|") -- ТСД
	x = x:gsub("{{[Тт]сдс|", "{{Статья в словнике3|") -- ТСД
	x = x:gsub("{{[Сс]татья в словнике ТСД|", "{{Статья в словнике3|") -- ТСД

	if edition == "ДО" or edition == "ВТ" then
		-- для {{ЭСБЕ/Статья}}
		x = x:gsub("{{ЭСБЕ/Статья|([^|]-)}}", "[[ЭСБЕ/" .. edition .. "/%1|%1]]")
		x = x:gsub("{{ЭСБЕ/Статья|([^|]-)|[0-9/|]*}}", "[[ЭСБЕ/" .. edition .. "/%1|%1]]")
		-- для {{Статья в словнике}}
		x = x:gsub(       "{{Статья в словнике|([^|]+)||[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1|%1]]")
		x = x:gsub("{{Статья в другом словнике|([^{|}]+)}}", "[[>" .. root .. "/" .. edition .. "/%1|%1]]")
		x = x:gsub("{{Статья в другом словнике|([^{|}]+)|}}", "[[>" .. root .. "/" .. edition .. "/%1|%1]]") -- Не уверен, что надо учитывать этот вариант; м.б. объединен с предыдущим
		x = x:gsub("{{Статья в другом словнике|([^{|}]+)||[^{}]-}}", "[[>" .. root .. "/" .. edition .. "/%1|%1]]") -- Надо посмотреть на практике в словниках -- если совершенно не нужно окажется записывать номера страниц для этого шаблона и от этого откажемся -- эту строку можно будет удалить
		-- ТСД
		x = x:gsub(      "{{Статья в словнике3|([^|]+)|[%s]*|[%s]*|[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1/ДО|%1/ДО]]")
		if edition == "ДО" then
			x = x:gsub(       "{{Статья в словнике|([^{|}]+)|([^{|}]*)|[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1|%2/ДО]]")
			x = x:gsub("{{Статья в другом словнике|([^{|}]+)|([^{}]-)}}", "[[>" .. root .. "/" .. edition .. "/%1|%2/ДО]]")
			x = x:gsub("{{Статья в другом словнике|([^{|}]+)|([^{|}]*)|[^{}]-}}", "[[>" .. root .. "/" .. edition .. "/%1|%2/ДО]]") -- Надо посмотреть на практике в словниках -- если совершенно не нужно окажется записывать номера страниц для этого шаблона и от этого откажемся -- эту строку можно будет удалить
			-- ТСД
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|[%s]*|[^|]+|[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1/ДО|%1]]")
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|([^|]+)|[%s]*|[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1/ДО|%2]]")
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|([^|]+)|[^|]+|[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1/ДО|%2]]")
		else
			x = x:gsub(       "{{Статья в словнике|([^{|}]+)|([^{|}]*)|[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1|%1]]")
			x = x:gsub("{{Статья в другом словнике|([^{|}]+)|([^{}]-)}}", "[[>" .. root .. "/" .. edition .. "/%1|%1]]")
			x = x:gsub("{{Статья в другом словнике|([^{|}]+)|([^{|}]*)|[^{}]-}}", "[[>" .. root .. "/" .. edition .. "/%1|%1]]") -- Надо посмотреть на практике в словниках -- если совершенно не нужно окажется записывать номера страниц для этого шаблона и от этого откажемся -- эту строку можно будет удалить
			-- ТСД
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|[^|]+|[%s]*|[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1|%1]]")
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|[%s]*|([^|]+)|[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1|%2]]")
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|[^|]+|([^|]+)|[^{}]-}}", "[[" .. root .. "/" .. edition .. "/%1|%2]]")
		end
	else
		x = x:gsub("{{ЭСБЕ/Статья|([^|]-)}}", "[[ЭСБЕ/%1|%1]]")
		x = x:gsub("{{ЭСБЕ/Статья|([^|]-)|[0-9/|]*}}", "[[ЭСБЕ/%1|%1]]")
		x = x:gsub(       "{{Статья в словнике|([^|]+)||[^{}]-}}", "[[" .. root .. "/%1|%1]]")
		x = x:gsub("{{Статья в другом словнике|([^{|}]+)}}", "[[>" .. root .. "/%1|%1]]")
		x = x:gsub("{{Статья в другом словнике|([^{|}]+)|}}", "[[>" .. root .. "/%1|%1]]") -- Не уверен, что надо учитывать этот вариант; м.б. объединен с предыдущим
		x = x:gsub("{{Статья в другом словнике|([^{|}]+)||[^{}]-}}", "[[>" .. root .. "/%1|%1]]") -- Надо посмотреть на практике в словниках -- если совершенно не нужно окажется записывать номера страниц для этого шаблона и от этого откажемся -- эту строку можно будет удалить
		x = x:gsub(       "{{Статья в словнике|([^{|}]+)|([^{|}]*)|[^{}]-}}", "[[" .. root .. "/%1|%1]]")
		x = x:gsub("{{Статья в другом словнике|([^{|}]+)|([^{}]-)}}", "[[>" .. root .. "/%1|%1]]")
		x = x:gsub("{{Статья в другом словнике|([^{|}]+)|([^{|}]*)|[^{}]-}}", "[[>" .. root .. "/%1|%1]]") -- Надо посмотреть на практике в словниках -- если совершенно не нужно окажется записывать номера страниц для этого шаблона и от этого откажемся -- эту строку можно будет удалить
		x = x:gsub(      "{{Статья в словнике2|([^|]+)||[^{}]-}}", "[[" .. root .. "/%1|%1]]")
		x = x:gsub(      "{{Статья в словнике2|([^{|}]+)|([^{|}]*)|[^{}]-}}", "[[" .. root .. "/%1|%2]]")
		-- ТСД
		x = x:gsub(      "{{Статья в словнике3|([^|]+)|[%s]*|[%s]*|[^{}]-}}", "[[" .. root .. "/%1|%1]]")
		if oldspell then
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|[%s]*|[^|]+|[^{}]-}}", "[[" .. root .. "/%1|%1]]")
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|([^|]+)|[%s]*|[^{}]-}}", "[[" .. root .. "/%1|%2]]")
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|([^|]+)|[^|]+|[^{}]-}}", "[[" .. root .. "/%1|%2]]")
		else
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|[^|]+|[%s]*|[^{}]-}}", "[[" .. root .. "/%1|%1]]")
			x = x:gsub(      "{{Статья в словнике3|([^|]+)[%s]*|[%s]*|([^|]+)|[^{}]-}}", "[[" .. root .. "/%1|%2]]")
			x = x:gsub(      "{{Статья в словнике3|([^|]+)|[^|]+|([^|]+)|[^{}]-}}", "[[" .. root .. "/%1|%2]]")
		end
	end
	-- x = string.gsub(x, "{{2[OО]|(.-)}}", "[[%1]]") -- не работает
	if oldspell then
		x = string.gsub(x, "{{2О|([^{}|]-)}}", "[[%1/ДО|%1]]") -- cyr. - no pipe
		x = string.gsub(x, "{{2O|([^{}|]-)}}", "[[%1/ДО|%1]]") -- lat. - no pipe
		x = string.gsub(x, "{{2О|([^{}|]-)|[^{}|]-|([^{}]-)}}", "[[%1/ДО|%2]]") -- cyr. - 2 pipes
		x = string.gsub(x, "{{2O|([^{}|]-)|[^{}|]-|([^{}]-)}}", "[[%1/ДО|%2]]") -- lat. - 2 pipes
		x = string.gsub(x, "{{2О|([^{}|]-)|([^{}]-)}}", "[[%1/ДО|%2]]") -- cyr.
		x = string.gsub(x, "{{2O|([^{}|]-)|([^{}]-)}}", "[[%1/ДО|%2]]") -- lat.
	else
		x = string.gsub(x, "{{2О|(.-)}}", "[[%1]]") -- cyr.
		x = string.gsub(x, "{{2O|(.-)}}", "[[%1]]") -- lat.
	end
	-- Убираем лишние фигурные скобки
	x = string.gsub(x, "\n{|", "\n")
	x = string.gsub(x, "\n|}", "\n")
	x = string.gsub(x, "{{Oncolor *|", "")
	x = string.gsub(x, "{{oncolor *|", "")
	x = string.gsub(x, "{{Dotted TOC", "")
	x = string.gsub(x, "{{dotted TOC", "")
	x = string.gsub(x, "{{ВАР", "")
	x = string.gsub(x, "{{ВАР2", "")
	x = string.gsub(x, "{{:MediaWiki:Proofreadpage.index.template", "")
	x = string.gsub(x, "( *{{skip *|)", "…%1")
	-- Удаляем оставшиеся шаблоны и пр.
	x = string.gsub(x, "%b{}", "")
	x = string.gsub(x, "\n== *См%. также *==.*", "")
	x = string.gsub(x, "\n== *Примечания *==.*", "")
	x = string.gsub(x, "\n==[^=\n]-==", "") -- м.б. ссылки в заголовках
	x = string.gsub(x, "\n===[^=\n]-===", "") -- "
	x = string.gsub(x, "\n====[^=\n]-====", "") -- "
	-- Ссылки на неосновное пространство имен, интервики и пр.
	x = string.gsub(x, "%[%[[:#][^%[%]]-%]%]", "")
	x = string.gsub(x, "%[%[%a: *[^%[%]]-%]%]", "") -- Википедия и пр.
	x = string.gsub(x, "%[%[commons: *[^%[%]]-%]%]", "")
	x = string.gsub(x, "%[%[wikilivres: *[^%[%]]-%]%]", "")
	x = string.gsub(x, "%[%[%a%a: *[^%[%]]-%]%]", "") -- интервики
	x = string.gsub(x, "%[%[%a%a%a: *[^%[%]]-%]%]", "") -- интервики
	x = string.gsub(x, "%[%[Категория: *[^%[%]]-%]%]", "")
	x = string.gsub(x, "%[%[Файл: *[^%[%]]-%]%]", "")
	-- Для подстраниц
	x = string.gsub(x, "%[%[/", "[[" .. listname .. "/")
	-- Пробелы
	x = mw.ustring.gsub(x, "%s+", " ")
	local t= {}
	for m in string.gmatch (x, "%[%[[^%[%]]-%]%]") do
		table.insert (t, m)
	end
	if #t == 0 then error ('Пустое оглавление') end
	for i,v in ipairs (t) do
		v = mw.ustring.gsub (v, "[%s_]", " ")
		v = string.gsub (v, "^%[%[ *(.-) *%]%]$", "%1")
		v = string.gsub (v, " +", " ")
		v = string.gsub (v, "'''", "")
		v = string.gsub (v, "''", "")
		v = mw.text.split (v, " *| *")
		local txt = v[2]
		if txt then
			local length = mw.ustring.len (txt)
			local pos = mw.ustring.find (txt, "[ \t\n]+", 40)
			if pos and (pos < length) then
				txt = mw.ustring.sub (txt, 1, pos-1)
				txt = mw.ustring.gsub (txt, "[.,;:]$", "") .. "…"
				txt = mw.ustring.gsub (txt, "(«[^»]-)$", "%1»")
				txt = mw.ustring.gsub (txt, "(%([^%)]-)$", "%1)")
				table.insert(v, 2, txt)
			end
		end
		t[i] = v
	end
	return t
end

function escapePattern( pattern_str )
	return mw.ustring.gsub( pattern_str, "([%(%)%.%%%+%-%*%?%[%^%$%]])", "%%%1" );
end

function p.beedScan (frame, noframe, lst)
	local list, name, raw = frame.args[1], frame.args[2], frame.args[3]
	local new_style, flag
	if (name == "") or (name == nil) or noframe then name = currname end
	name = name:gsub ("^ЭСБЕ/", "")
	if name:find ("^ДО/") or name:find ("^ВТ/") then
		new_style = true
		flag = mw.ustring.sub (name,  1, 2)
		name = mw.ustring.sub (name, 4)
	end
	name = name:gsub ("/.*", "")
	if (list == "") or (list == nil) or noframe then
		if new_style then
			list = "Энциклопедический словарь Брокгауза и Ефрона/" .. flag .. "/Словник/" .. p.wordlist (frame)
		else
			list = "Викитека:Проект:ЭСБЕ/" .. p.wordlist (frame)
		end
	end
	if lst then list = lst end
	raw = noframe or raw
	if not (name and list) then return end
	local title = mw.title.new (list)
	if not title then error ('Недопустимое имя оглавления: ' .. name) end
	local page = title["getContent"]
	local x = page (title)
	if not x then error ( string.format ('Оглавление «%s» не найдено', title.text )) end
	local m = string.match (x, "{{ЭСБЕ/Статья| *" .. escapePattern (name) .. " *|([^{}]-)}}")
	if m then
		m = mw.text.split (m, "|")
	else
		if string.find (x, "{{ЭСБЕ/Статья| *" .. escapePattern (name) .. " *}}") then
			return "<!-- Скан этой страницы временно отсутствует. -->"
		else
			error ( string.format ('Статья «%s» не найдена в списке «%s».', name, list ))
		end
	end
	local t = {}
	for i, v in ipairs (m) do
		local part = beed.parseVolumeStr(v)
		if part ~= nil then
		  table.insert (t, frame:expandTemplate { title = 'ЭСБЕ/Скан', args = {part.volume, part.page, part.numpages}})
		end
	end
	local volumes = mw.loadData('Module:BEED/volumes')
	local volume_key = ""
	for i, v in ipairs (t) do
		v = string.gsub (v, "&nbsp;", " ")
		volume_key = string.match (v, "''(.-), ")
		if volumes[volume_key] then
			v = string.gsub (v, "([^%p%s]+), ", volumes[volume_key] .. ", с. ")
		else
			v = string.gsub (v, "([^%p%s]+), ", "т. %1, с. ")
		end
		v = string.gsub (v, "''", "")
		t[i] = v
	end
	local result = frame:expandTemplate { title = "ЕДО", args = { "Источникъ", "Источник" }} .. ": " .. table.concat (t, "; ")
	if raw then
		if tonumber (raw) == 1 then
			return m[1]
		elseif tonumber (raw) == 2 then
			return m[2]
		else
			return result
		end
	else
		return result
	end
end

function p.pagenum (frame)
	local type, name, listno, list, _phard, _psoft = frame.args[1], frame.args["name"], frame.args["listno"], frame.args["list"], frame.args["phard"], frame.args["psoft"]
	if (name == "") or (name == nil) then name = currname end
	local phard, psoft

	if (_phard == nil) and (_psoft == nil) then
		if not list then
			list = word_list (nil, name, nil, 'full', listno)
		end
		if (list == "") or (list == nil) then return end

		-- local root = p.parse_title (name, 'root')
		-- local edition = p.parse_title (name, 'edition')
		local subpages = p.parse_title (name, 'subpages')
		if subpages == nil or subpages == "" then
			subpages = p.parse_title (name, 'subpages1')
		end
		subpages = subpages:gsub ("/.*", "")

		-- list title object
		local title = mw.title.new (list)
		if not title then error ('Недопустимое имя оглавления: ' .. subpages) end
		local page = title["getContent"]
		local x = page (title)
		if not x then error ( string.format ('Оглавление «%s» не найдено', title.text )) end

		-- Аналогично makelist()
		x = x:gsub("{{2О Статья в словнике|", "{{Статья в словнике|") -- 2О - rus. О
		x = x:gsub("{{2O Статья в словнике|", "{{Статья в словнике|") -- 2O - lat. O (alias)
		x = x:gsub("{{[Tt]sds|", "{{Статья в словнике3|") -- ТСД
		x = x:gsub("{{[Тт]сдс|", "{{Статья в словнике3|") -- ТСД
		x = x:gsub("{{[Сс]татья в словнике ТСД|", "{{Статья в словнике3|") -- ТСД

		subpages = escapePattern (subpages)

		phard = mw.ustring.match (x, "{{Статья в словнике2?|[%s]*" .. subpages .. "[%s]*|[^|]*|([^{|}]*)}}")
		if not phard then
			phard, psoft = mw.ustring.match (x, "{{Статья в словнике2?|[%s]*" .. subpages .. "[%s]*|[^|]*|([^|]*)|([^{|}]*).-}}")
		end
		if not phard then
			phard = mw.ustring.match (x, "{{Статья в словнике3|[%s]*" .. subpages .. "[%s]*|[^|]*|[^|]*|([^{|}]*)}}")
		end
		if not phard then
			phard, psoft = mw.ustring.match (x, "{{Статья в словнике3|[%s]*" .. subpages .. "[%s]*|[^|]*|[^|]*|([^|]*)|([^{|}]*).-}}")
		end
	else
		phard = _phard
		psoft = _psoft
	end

	local t1, t2 = {}, {}
	if phard then
		t1 = mw.text.split (phard, "/")
	end
	if psoft then
		t2 = mw.text.split (psoft, "/")
	end

	if type == "phard" then
		return phard or ""
	elseif type == "hard" then
		return t1[1] or ""
	elseif type == "pagination" then
		return t1[2] or ""
	elseif type == "psoft" then
		return psoft or ""
	elseif type == "soft" then
		return t2[1] or ""
	elseif type == "stop" then
		return t2[2] or ""
	elseif type == "skip" then
		return t2[3] or ""
	elseif type == "test" then
		return x
	end
end

function p.wordlist (frame, noframe)
	local list = frame.args[1];
	local name = frame.args[2];
	local supplement = frame.args[3];
	local type = frame.args["type"];
	local listno = frame.args["listno"];
	return word_list (list, name, supplement, type, listno);
end;

function word_list (list, name, supplement, type, listno)
	local digits = 2
	local root, n, flag, title, new_style, prefix
	if (name == "") or (name == nil) then name = currname end
	n = mw.text.split (name, "/")
	if #n == 1 then return end
	if n[2] == "ДО" or n[2] == "ВТ" then
		if #n == 2 then
			return
		else
			flag, title = n[2], n[3]
			new_style = true
		end
	else
		title = n[2]
	end
	title = title:gsub ("%b()$", "")
	title = title:gsub (",", "00000")
	if n[1] == "БЭАН" then
		title = title:gsub ("^Св%. ", "")
		title = title:gsub ("^От ", "")
	elseif n[1] == "ЭСБЕ" then
		title = title:gsub ("^д’Еон", "Еон")
		title = title:gsub ("^д’Аннунцио", "Аннунцио")
	end
	title = title:gsub ("[%p%s]", "")
	--title = title:gsub ("00000", ", ")
	title = title:gsub ("ё", "е")
	if (list == "") or (list == nil) then
		if n[1] == "ЭСБЕ" then
			if new_style then
				root = "Энциклопедический словарь Брокгауза и Ефрона/" .. flag .. "/Словник/"
			else
				root = "Викитека:Проект:ЭСБЕ/"
			end
			digits = 3
			list = [[A N А Аг Аз Ал Ало Ам Ан Анк Ао Ар Арм Ас Ау Б Бак Бар Бас Бб Бел Бем Бер Бес Би Био Бл Бо Бок Бор Бр Бри Бу Буо Бх
			В Вам Вас Вве Вел Вер Вес Виа Вим Вкл Вои Вом Вр Вы Г Гал Гао Гва Гем Гер Гжа Гим Гл Го Гом Гос Гра Грж Гуа Гуп
			Д Дао Деа Дел Дер Дж Ди Дио До Доо Дуа Е Ел Ж Жи З Зап Зе Зл И Иж Ил Ин Ио Ис Й
			К Кай Кам Кан Кар Карл Кас Кв Ке Ки Кл Км Коа Кол Ком Кон Коо Кос Кра Крж Ку Кур Л Лан Леа Лем Ли Лио Ло Лу Ль
			М Мак Мам Мар Мас Меа Мек Мер Ми Мир Мо Моо Мп Мх Н Нар Не Нем Ни Но Нр О Ог Ол Ор Ос От
			П Пан Пас Пеа Пер Пес Пи Пир Пл По Пол Пом Пос Пра Прж Про Пс Пф Р Рал Ре Рек Ри Роа Рок Ру Рш
			С Сал Сан Сар Сб Се Сем Сер Си Син Ск Сл Со Сом Сп Ста Сти Су Сф Т Тан Теа Теп Ти То Тра Три Тс У Ум Ус
			Ф Фе Фео Фи Фио Фо Фр Фт Х Хе Хм Хр Ц Це Ци Ч Чер Чж Ш Шар Ше Ши Шм Шт Щ Э Эк Эм Эр Ю Я Ян Яя+]]
			if supplement then list = supplement end
		elseif n[1] == "БЭАН" then
			root = "Библейская энциклопедия архимандрита Никифора/Словник/"
			list = 'А:А Б:Б В:В Г:Г Д:Д Е:Е Ж:Ж З:З И:И К:К Л:Л М:М Н:Н О:О П:П Р:Р С:С Т:Т У:У Ф:Ф Х:Х Ц:Ц Ч:Ч Ш:Ш Щ:Щ Э:Э Ю:Ю Я:Я Яя:0'
		elseif n[1] == "МЭСБЕ" then
			root = "Малый энциклопедический словарь Брокгауза и Ефрона/Словник/"
			list = [[A А Агуас Аланс Альфр Анемн Араго Асб Б Бандель Батш Бенас Библия. Боброва Боркг Бриар Букса
			В Варне Венз Вие Вкусо Ворв Г Гань Геку Гершт Глейхенр Горбы Гренг Д Делес Диаме Дониц Е Ж З Зеленч
			И Индос К Камера Каркасс Квип Клавик Кола Контор Кошкар Крыс Л Легит Литейный М Маннит Медв Мизе Монн
			Н Несторис О Ону П Пегу Пинде Полиц Призы Р Резек Родил С Сарай Секу Сиги Славя Социн Страсбургер
			Т Тенез Торговоес У Ф Фисо Х Ц Ч Ш Шипуч Ъ Эмболия Ю Яя+]]
		elseif n[1] == "ЕЭБЕ" then
			if new_style then
				root = "Еврейская энциклопедия Брокгауза и Ефрона/" .. flag .. "/Словник/"
			else
				root = "Еврейская энциклопедия Брокгауза и Ефрона/Словник/"
			end
			list = [[A:01 Alt:02 Ar:03 Be:04 Bu:05 C:09 D:07 E:16 F:15 G:06 I:08 Jude:09
			L:10 Mi:11 O:12 Pro:13 Sc:14 Ste:16 Sti:14 Tr:15 Ty:14 V:15 Veri:05 Z:15
			А:01 Алгар:02 Алгу:01 Алмо:02 Ар:02:03 Арабско:03 Бе:04 Бед:04:05 Бее:04 Беж:04:05 Без:04
			Бел:04:05 Бем:04 Берж:04:05 Берз:04 Беч:04:05 Би:04 Бресс:04:05 Брет:05
			Гад:05:06 Гае:06 Дан:06:07 Дани:06 Данф:07 Иа:08 Иб:07 Ибнэ:07:08 Иссо:16
			Ист:08 Иудан:09 Иудап:08 Иудг:09 Иф:08 К:09 Ладен:09:10 Лади:10 Медн:11 Меж:10
			Мелец:11 Мели:10 Мен:11 Менан:10 Меры:11 Мес:10 Мест:10:11 Мет:10 Мехо:11
			Мехол:10 Мещ:10:11 Миб:10 Миддот:10:11 Миди:11 Обет:12 Обеч:11 Обы:12 Пени:13 Пенин:12
			Песн:13 Песс:12 Преш:13 Прж:12 Прокл:13 Сарае:14 Телес:15 Телех:14 Трани:14:15 Транс:15
			Федо:16 Фей:15 Феод:16 Фер:15 Фесс:16 Фест:15 Фив:16 Фиг:15 Фим:16 Фин:15
			Шем:15:16 Шемо:16 Яя:00]]
		elseif n[1] == "ПБЭ" then
			root = "Православная богословская энциклопедия/ВТ/Словник/"
			list = [[A:00 Can:26 Cl:30 Col:31 Com:32 Κοινη:28 Κοινή:31
			А:01 Ад:02 Алф:01:02 Аль:02 Ам:03 Ап:04 Архео:05 Б:06 Бе:06:07 Би:06 Бо:07 В:08 Ват:09 Ве:09:10 Ви:09 Вл:10
			Г:11 Гера:11:13 Герб:11 Ги:12 Гум:12:13 Гур:12 Д:13 Де:13:14 Ди:13 Донс:14 Е:15 Ел:16 Ж:17
			Иа:20 Иако:20:21 Иам:20 Ив:18 Ие:20 Иерар:20:26 Иерат:20 Иеро:21 Из:18 Ии:21 Ик:18
			Ио:21 Иоанн:22:21 Ион:23 Ип:19 Иу:23 Иуда:23:26 Иуде:23 Иф:19 Ия:23 Йог:22 Йон:23
			К:24 Кад:24:25 Казанская:24:26 Казанский:25:25 Каи:24 Календарь.:25 Кано:26 Карме:27
			Кв:28 Кинн:29:30 Кино:29 Кл:30 Книгаи:31 Книгак:30 Книгиз:31 Книгин:30 Книгип:31 Колон:32
			Л:00 С:20:21 Я:00]]
			-- Статьи на 'Иоанн' относятся к 21 или 22 списку, точнее автоматически определить невозможно
			-- Есть несколько статей на С и др. буквы, также требующих ручного определения
		elseif n[1] == "РБС" then
			root = "Русский биографический словарь/ДО/Словник/"
			list = [[А:01 Алексе:01:02 Алекси:02 Ано:03 Б:04 Бау:05 Бег:05:08 Бет:06 Бол:07 Бу:08
			Г:09 Гв:10 Гербер:11 Гол:24 Д:12 Де:12:13 Ди:13 Ж:14 З:15 Зд:16
			Иа:19 Иб:17 Ие:19 Иж:17 Ии:19 Ик:18 Ио:19 Иоас:20 Ип:18 Иу:20 Иф:18
			К:21 Кач:22 Кн:23 Кос:24 Л:25 Лен:26 Лес:26:27 Лет:26:27 Леф:26 Лов:27
			Н:28 О:29 Ол:30 П:31 Пар:32 Пев:32:37 Пер:33:37 Пи:33 Пл:34 Поз:35 Поп:36 Прит:37
			Р:38 Ред:38:42 Рейт:39 Реп:39:42 Рер:39 Реш:39:42 Рж:39 Рих:40 Ром:41 Руд:42
			С:43 Се:44 Сев:44:48 Сес:44 Сим:45 Сме:46 Сми:45 Сне:46 Стар:47 Суворо:48 Т:49 Тен:50
			Ф:51 Фаво:64 Фавс:51 Фадд:64 Фаде:51:64 Фед:64:51 Фез:51
			Фео:64 Ферап:64 Ферб:51 Фету:52 Феф:64 Фех:51 Фив:64 Фиг:51 Фин:52 Фиод:64 Фиор:52 Флее:64 Флей:52 Фом:64:52 Фон:52
			Х:53 Ц:54 Ч:55 Черн:56 Ш:57 Ше:58 Шн:59 Щ:60 Э:61 Ю:62 Я:63 Яя:00]]
			-- Некоторые фамилии на 'Фаде', 'Фед' и 'Фом' имеют двоякое написание, определять вручную
		elseif n[1] == "ВЭ" then
			root = "Военная энциклопедия (Сытин, 1911—1915)/ВТ/Словник/"
			list = [[A:01 C:11 G:08 M:15
			А:01 Алжир:01:02 Алжирскиеэ:02 Арал:03
			Б:04 Бег:04:05 Без:04 Бел:04:05 Бем:04 Бом:04:05 Бомбар:05
			Веж:05:07 Верещ:05:06 Верея:06:07 Вз:06 Воин:06:07 Вой:07 Восс:06 Вост:07
			Гие:08 Гиз:07 Гимр:08 Две:08:09 Дви:08 Двин:09 Ели:10 Ие:11:12 Иж:10 Инк:11
			Калья:12 Кобл:13 Креп:13:14 Крес:13 Крук:14 Лес:14:15 Леф:14 Линту:15
			Мед:15:16 Ми:15 Миа:15:16 Мик:15 Минв:16 Минг:15 Минны:15:16 Мино:16
			Неж:16:17 Нен:16 Ниа:16:17 Ник:16 Нит:17 Пау:18 Я:00]]
		elseif n[1] == "ЭЛ" then
			root = "Энциклопедический лексикон/ДО/Словник/"
			list = [[D:15 De:16 A:01 А:01 Алм:01:02 Ало:02 Аль:01 Альм:01:02 Альп:02 Ар:02:03 Ара:02 Аран:03:01
			Б:04 Баррер:05 Бег:05:07 Би:05 Бино:06 Бранд:06:07 Брани:07 Булгаков:07:12
			В:08 Вар:08:09 Варшава:09:12 Вас:09 Вессел:10:12 Вл:11 Воо:12 Вреде:12:14
			Г:13 Гемо:14 Горны:14:15 Горо:15
			Д:15:17 Дв:16:17 Дио:16:17 Дип:16 Дл:17 Я:00]]
		elseif n[1] == "БСЭ1" then
			root = "Викитека:Проект:БСЭ1/Словник/"
			list = [[A:01
			А:01 Акон:02 Анрио:03 Атол:04 Бары:05 Бессар:06 Больн:07 Буковы:08 Варлен:09 Венгр:10
			Вильо:11 Воден:12 Волч:13 Высше:14 Гейль:15 Германия:16 Гимна:17 Город:18 Граци:19 Гурьевк:20
			Дейл:21 Джуц:22 Дод:23 Евре:24 Железо:25 Зазу:26 Зерновыеэ:27 Империалис:28 Интерполяция:29 История:30
			Камбо:31 Кауч:32 Классы:33 Конкурс:34 Крестьянскаяг:35 Ларт:36 Лилль:37 Мамми:38 Мерав:39 Мон:40
			Наган:41 Нидерланды:42 Оклад:43 Пализ:44 Перемыш:45 Пола:46 Призн:47 Рави:48 Робе:49 Ручно:50
			Серн:51 Созн:52 Страти:53 Телецк:54 Трихоц:55 Украинц:56 Фе:57 Флора:58 Францо:59 Хол:60
			Ч:61 Шахта:62 Э:63 Электрофор:64 Эфем:65 Яяя:00]]
		elseif n[1] == "ТСД" and supplement == "2" then
			root = "ТСД-словник/"
			list = [[А:А Б:Б Би:Би В:В Во:Во Вы:Вы Г:Г Д:Д Дон:Дон Е:Е Ж:Ж З:З Зал:Зал Заст:Заст
			И:И Изу:Изу І:І К:К Ки:Ки Кор:Кор Л:Л М:М Н:Н Нак:Нак Нар:Нар Не:Не О:О Обц:Обц Ор:Ор Ото:Ото
			П:П Перел:Перел Пи:Пи Под:Под Подт:Подт Пок:Пок Поо:Поо Пор:Пор Пот:Пот Приг:Приг Про:Про Прор:Прор
			Р:Р Расп:Расп С:С Сл:Сл Сп:Сп Т:Т У:У Ф:Ф Х:Х Ц:Ц Ч:Ч Ш:Ш Щ:Щ
			Ъ:Ъ-Ы-Ь Ы:Ъ-Ы-Ь Ь:Ъ-Ы-Ь Ѣ:Ѣ Э:Э Ю:Ю Ѧ:Ѧ Я:Я Ѳ:Ѳ Ѵ:Ѵ]]
		elseif n[1] == "ТСД" and supplement == "3" then
			root = "ТСД-словник/"
			list = [[А:А Б:Б Би:Би В:В Во:Во Вы:Вы Г:Г Д:Д Дон:Дон Е:Е Ж:Ж З:З Зал:Зал Заст:Заст
			И:И Изу:Изу І:І К:К Ки:Ки Кор:Кор Л:Л М:М Н:Н Нак:Нак Нар:Нар Не:Не О:О Обц:Обц Ор:Ор Ото:Ото
			П:П Перел:Перел Пи:Пи Под:Под Подт:Подт Пок:Пок Поо:Поо Пор:Пор Пот:Пот Приг:Приг Про:Про Прор:Прор
			Р:Р Расп:Расп С:С Сл:Сл Сп:Сп Т:Т У:У Ф:Ф Х:Х Ц:Ц Ч:Ч Ч1:Ч1 Ш:Ш Щ:Щ
			Ъ:Ъ-Ы-Ь Ы:Ъ-Ы-Ь Ь:Ъ-Ы-Ь Ѣ:Ѣ Э:Э Ю:Ю Ѧ:Ѧ Я:Я Ѳ:Ѳ Ѵ:Ѵ]]
		elseif n[1] == "ГСС" then
			root = "Географическо-статистический словарь Российской империи/ДО/Словник/"
			list = [[А:01 Але:02 Ап:03 Б:04 Бе:05:07 Бо:06 Бу:07 В:08:11 Вес:09:11 Вн:10 Вор:11 Г:12 Гом:13
			Д:14:16 Дз:15 Дон:16 Е:17 Ж:18 З:19 И:20:21 Ип:21 К:22 Кам:23 Карб:24 Кв:25:31 Кис:26:31 Ког:27 Ком:28 Кр:29 Кс:30 Курж:31
			Л:32:33 Лиф:33 М:34 Мар:35 Мей:36:38 Ми:36:37 Мис:37 Мос:38 Н:39 Не:39:42 Ни:40 Но:41 Новоп:42 О:43 Оли:44 Оре:45 Оси:46
			П:47 Пе:47:51 Перл:48:51 Пи:49 Пол:50 При:51 Р:52 Ре:52:53 Ри:52 Рос:53 С:54 Санн:55
			Сб:56 Се:56:62 Сер:57:62 Си:57:58 Сир:58 Сок:59 Ст:60 Сте:60:61 Стр:61 Сэ:62
			Т:63 Тас:64 Тен:65 Теш:65:68 Ти:65 То:66 Тос:67 Тум:68 У:69 Ус:70 Ф:71 Х:72 Хи:73
			Ц:74 Ч:75 Черл:76 Чес:77 Ш:78 Шен:79 Щ:80 Ю:81 Я:82 Ян:83 Яяя:00]]
		else
			root = n[1] .. "/ДО"
			list = ""
		end
	end
	if type == "full" then prefix = root else prefix = "" end
	-- разбиение списка начальных букв словников в массив, по символам ' ' и ':'
	if (listno == "") or (listno == nil) and (list ~= "") then
		local m = mw.text.split (list, '%s+')
		for i, v in ipairs (m) do
			v = mw.text.split (v, ':')
			if not v[2] then v[2] = string.format ("%0" .. digits .. "d", i) end
			m[i] = v
		end
		-- поиск соответствующего словника по заголовку статьи
		for i = 1, #m do
			if title >= m[i][1] and title < m[i+1][1] then
				-- сборка викиссылки к словнику
				if m[i][3] then
					local t = makelist (root .. m[i][2])
					if t then
						for j, v in ipairs (t) do
							if escapePattern(v[1]) == escapePattern(name) then
								return prefix .. m[i][2]
							end
						end
					end
					return prefix .. m[i][3]
				else
					return prefix .. m[i][2]
				end
			end
		end
	else
		return prefix .. (listno or "")
	end
	return "Oops"
end

--[=[
Функция parseTitle
Разбивает название страницы на сегменты в соответствии с механизмом редакций

Использование:
{{#invoke:Header|parseTitle|segment|[name]}}

Допустимые значения segment:
	root: корневая часть названия со списком редакций
	edition: первый уровень подстраниц (обозначение текущей редакции)
	fulledition: полный путь к текущей редации от корня
	subpages: остальные уровни подстраниц как единое целое
	subpages1: все уровни подстраниц (если механизм редакций не используется)
	isPRS: true, если название редакции соответствует ДО, иначе false
	test: выводит все компоненты, для тестирования поведения
]=]
function p.parseTitle (frame)
	local segment, name = frame.args[1], frame.args[2]
	if (name == "") or (name == nil) then name = currname end
	return p.parse_title (name, segment)
end

function p.parse_title (title, s)
	local name = title
	local parts = {}
	-- выделение корневого элемента
	if name:find ("^[^/%(%)]+%([^%(%)]+/[^%(%)]+%)/") then
		parts.root = name:gsub ("^([^/%(%)]+%([^%(%)]+/[^%(%)]+%))/.+", "%1")
		name = name:gsub ("^[^/%(%)]+%([^%(%)]+/[^%(%)]+%)/", "")
	elseif name:find ("^[^/%(%)]+%([^%(%)]+/[^%(%)]+%)$") then
		parts.root = name
		name = ""
	elseif name:find ("/") then
		parts.root = name:gsub ("^([^/]+)/.+", "%1")
		name = name:gsub ("^[^/]+/", "")
	else
		parts.root = name
		name = ""
	end
	parts.subpages1 = name
	if name:find ("/") then
		parts.edition = name:gsub ("^([^/]+)/.+", "%1")
		parts.subpages = name:gsub ("^[^/]+/", "")
	else
		parts.edition = name
		parts.subpages = ""
	end
	if parts.edition ~= "" then
		parts.fulledition = parts.root .. "/" .. parts.edition
		parts.isPRS = (parts.edition == "ДО") or parts.edition:find("^.+ +%(ДО%)$") or parts.subpages1:find("/ДО$")
	else
		parts.fulledition = ""
	end
	if parts.isPRS then
		parts.isPRS = true
	else
		parts.isPRS = false
	end
	if s == "test" then
		return "title: " .. title .. ", root: " .. parts["root"] .. ", edition: " .. parts["edition"] .. ", fulledition: " .. parts["fulledition"] ..
			", subpages: " .. parts["subpages"] .. ", subpages1: " .. parts["subpages1"] .. ", isPRS: " .. tostring(parts["isPRS"])
	else
		return parts[s]
	end
end

function p.editionsList (frame)
	local mode = frame.args[1]
	local edition = p.parse_title (currname, "edition")
	local flag = ""
	local edition_pre = ""
	if (edition == "ДО") or (edition == "ВТ") then -- для словарей
		flag = "|" .. edition .. "|"
		edition_pre = "Редакция "
	elseif edition:find ( "^.*%([^%(%)]+%)$" ) then
		flag = edition:gsub ("^.*%(([^%(%)]+)%)$", "|%1|")
	end
	-- не соответствует схеме именования редакций
	if flag == "" or not string.find ("|ДО|СО|ВТ|ВТ1|ВТ2|ВТ:Ё|ВТ:У|", flag) then return end
	local name = p.parse_title (currname, "root")
	local subs = p.parse_title (currname, "subpages")
	-- поддержка ДО
	--local str_toc = frame:expandTemplate { title = "ЕДО", args = { "оглавленіе", "оглавление" }}
	local str_editions = frame:expandTemplate { title = "ЕДО", args = { "Редакціи", "Редакции" }}
	local title = mw.title.new (name)
	if not title then error ('Недопустимое имя списка: ' .. name) end
	local page = title["getContent"]
	local x = page (title)
	-- список редакций отсутствует или пуст
	if not x or not ( x:find ("\n%*") or x:find ("^%*") ) then
		return "'''[[" .. name .. "|" .. str_editions .. "]]'''"
	end
	-- чистка списка редакций
	x = x:gsub ("\n%s*\n", "\n") -- пустые строки
	x = x:gsub ("^.-\n%*", "*") -- текст до начала списка
	x = x:gsub ("\n[^%*].+", "\n") -- текст после конца списка
	x = x:gsub ("%]%].-\n", "]]\n") -- текст после ссылок
	local y = x -- альтернативный список
	y = y:gsub ("%[%[([^%[%]/]-/)([^%[%]|]-)|[^%[%]]-%]%]", "[[%1%2|" .. edition_pre .. "%2]]") -- edition как отображаемый текст
	x = x:gsub ("%[%[/", "[[" .. name .. "/") -- относительные ссылки в абсолютные
	y = y:gsub ("%[%[/", "[[" .. name .. "/") -- относительные ссылки в абсолютные
	-- добавление ссылок на оглавления (для подстраниц)
	if subs ~= nil and subs ~= "" and mode ~= "short" then
		x = x:gsub ("%* *%[%[([^%[%]|]-)|([^%[%]]-)%]%]",  "<tr><td></td><td style='padding-right:1em;'>[[%1/" .. subs .. "|%2]]</td><td><small>([[%1|огл.]])</small></td></tr>")
		y = y:gsub ("%[%[([^%[%]|]-)|([^%[%]]-)%]%]", "[[%1/" .. subs .. "|%2]]")
	else
		x = x:gsub ("%* *(%[%[[^%[%]|]-|[^%[%]]-%]%])",  "<tr><td></td><td>%1</td></tr>")
	end
	-- добавление значка для ДО
	x = x:gsub ("</td>(<td[^<>]->%[%[[^%[%]|]- %(ДО%) *|[^%[%]]-%]%])", "[[File:Ять 4.jpg|16px|link=|Дореформенная ор{{ф}}ограф{{и}}я]]&nbsp;</td>%1")
	x = x:gsub ("</td>(<td[^<>]->%[%[[^%[%]|]- %(ДО%)/[^%[%]|]-|[^%[%]]-%]%])", "[[File:Ять 4.jpg|16px|link=|Дореформенная ор{{ф}}ограф{{и}}я]]&nbsp;</td>%1")
	x = x:gsub ("</td>(<td[^<>]->%[%[[^%[%]|]-/ДО *|[^%[%]]-%]%])</td>", "[[File:Ять 4.jpg|16px|link=|Дореформенная ор{{ф}}ограф{{и}}я]]&nbsp;</td>%1")
	x = x:gsub ("</td>(<td[^<>]->%[%[[^%[%]|]-/ДО/[^%[%]|]-|[^%[%]]-%]%])</td>", "[[File:Ять 4.jpg|16px|link=|Дореформенная ор{{ф}}ограф{{и}}я]]&nbsp;</td>%1")
	-- оформление списка
	x = "<table>\n" .. x .. "\n<tr><td colspan=3 style='text-align:center;'><small>([[" .. name .. "|список{{ъ}} редакц{{и}}й]])</small></td></tr>\n</table>"
	x = "<div id='editions_toggle'>\n'''" .. str_editions .. "'''\n<div id='editions_cont'>\n" .. frame:preprocess(x) .. "</div></div>"
	x = x .. "<div id='altEditions' style='display:none;'>\n\n" .. frame:preprocess(y) .. "\n</div>"
	if mode == "flag" then
		return flag
	else
		return x
	end
end

function p.fixarrowlink (frame)
	local link = frame.args[1]
	link = link:gsub ("^←%s*%[%[([^%[%]|]+)|([^%[%]]+)%]%]%s*$", "<span style='display:table-cell;vertical-align:middle;font-size:200%%;'>[[%1|⇦]]</span> <span style='display:table-cell;vertical-align:middle;width:100%%;'>[[%1|%2]]</span>")
	link = link:gsub ("^←%s*%[%[([^%[%]|]+)%]%]%s*$", "<span style='display:table-cell;vertical-align:middle;font-size:200%%;'>[[%1|⇦]]</span> <span style='display:table-cell;vertical-align:middle;width:100%%;'>[[%1|%1]]</span>")
	link = link:gsub ("^←%s*([^%[].*)$", "<span style='display:table-cell;vertical-align:middle;font-size:200%%;'>⇦</span> <span style='display:table-cell;vertical-align:middle;width:100%%;'>%1</span>")
	link = link:gsub ("^%s*%[%[([^%[%]|]+)|([^%[%]]+)%]%]%s*→$", "<span style='display:table-cell;vertical-align:middle;width:100%%;'>[[%1|%2]]</span> <span style='display:table-cell;vertical-align:middle;font-size:200%%;'>[[%1|⇨]]</span>")
	link = link:gsub ("^%s*%[%[([^%[%]|]+)%]%]%s*→$", "<span style='display:table-cell;vertical-align:middle;font-size:100%%;'>[[%1|%1]]</span> <span style='display:table-cell;vertical-align:middle;font-size:200%%;'>[[%1|⇨]]</span>")
	link = link:gsub ("^%s*(.*[^%]])%s*→$", "<span style='display:table-cell;vertical-align:middle;font-size:100%%;'>%1</span> <span style='display:table-cell;vertical-align:middle;font-size:200%%;'>⇨</span>")
	return link
end

-- Преобразует переданную текстовую строку в ссылку, если она не содержит ссылок;
-- в противном случае, возвращает ее без изменений
function p.linkify (frame)
	local link = frame.args[1]
	if link == nil or link == "" then return end
	if not link:find ("%[%[") then
		link = "[[" .. link .. "]]"
	end
	return link
end

function p.test (frame)
	local a = frame.args[1]
	local t = makelist (a)
	for i, v in ipairs (t) do
		v = table.concat (v, ' @@@ ')
		t[i] = v
	end
	return table.concat (t, '\n')
end

return p
