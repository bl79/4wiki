# coding: utf-8
import re
import sys
import roman
import vladi_commons

page_title = False
if len(sys.argv) > 1:
    page_title = sys.argv[1]

# re_any_title = r'\n={2,}\s*([^=\n]+)\s*={2,} *\n'
# r = re.search(re_any_title + r'\n\n*(.*?)' + '((?:' + re_any_title + ')|$)', text, re.S)
wikipages_filename = r'..\temp\AWBwikipage.txt'
text = vladi_commons.file_readtext(wikipages_filename)


# text = '''  '''
# wikicode = mwparserfromhell.parse(text)

def capitalize_headers():
    # регистр букв заголовков в строчные
    import mwparserfromhell
    for header in wikicode.filter_headings():
        t = str(header.title).strip().capitalize()
        t = t.replace('i', 'I')
        t = t.replace('v', 'V')
        t = t.replace('x', 'X')
        header.title = ' ' + t + ' '


def tsd_pagenumber(izdanie, volume, pagenumber_scan):
    offset_of_volumes = [[2, -626, 1, 1], [90, 9, 8, 8], [17, 2, 2, 4]]
    i = izdanie - 1
    v = volume - 1
    if izdanie == 1 or izdanie == 2:
        page_number = str(int(pagenumber_scan) - offset_of_volumes[i][v])
    elif izdanie == 3:
        page_number = str((int(pagenumber_scan) - offset_of_volumes[i][v] - 1) * 2 + 1)
    return str(page_number)


# не работает настраницах OCR ТСД, ибо там часто незакрытые тэги
# import mwparserfromhell
# from lib_for_mwparserfromhell import paramIsEmpty
# wikicode = mwparserfromhell.parse(text)

izdanie = 5
volume = 4

if page_title:
    pagenames = re.search(r'(^.+)/(.*?)$', page_title)

    if pagenames:
        basepagename = pagenames.group(1)
        scan_pagenumber = pagenames.group(2)
        if izdanie >= 1 and izdanie <= 3:
            page_number = tsd_pagenumber(izdanie, volume, scan_pagenumber)
        if izdanie == 5:
            page_number = int(scan_pagenumber) - 889

        text = re.sub(r'{{колонтитул(?:{{акут3?}}|.)*?}}', '', text, flags=re.DOTALL)
        c2 = " — "
        c2 = "Объясненіе сокращеній"
        # c2 = "Послѣсловіе"
        # c2 = "Объясненіе шрифтовъ, знаковъ и пр"

        c = re.search(r"{{[Кк]олонтитул\s*\|[^|]*\|['\s.]*(.*?)['\s.]*\|[^|]*}}", text, flags=re.DOTALL)
        if c:
            if c.group(1) and not re.match('^\s*$', c.group(1)):
                c2 = c.group(1)
                # c2 = c2.replace('{{акут}}', '́')
                # c2 = c2.replace('{{акут3}}', '&#x02CA;')
                re.sub(
                    r'({{колонтитул(?:{{акут3?}}|.)*?}})',
                    text,
                    flags=re.DOTALL)
        else:
            text = re.sub(r'(<noinclude>\s*<pagequality[^>]+>.*?</noinclude>)', r'\1{{колонтитул|||}}', text,
                          flags=re.DOTALL)

        if izdanie == 2:
            colontitul = vladi_commons.wiki_colontitul(
                vladi_commons.label_interpages(page_number, page_number, ''),
                "'''%s.'''" % c2,
                vladi_commons.label_interpages(page_number, '', page_number))
        elif izdanie == 3:
            colontitul = vladi_commons.wiki_colontitul(
                page_number,
                "'''%s.'''" % c2,
                str(int(page_number) + 1))
        elif izdanie == 5:
            colontitul = vladi_commons.wiki_colontitul(
                vladi_commons.label_interpages(page_number, roman.toRoman(page_number), ''),
                # "%s" % c2,
                "'''%s.'''" % c2,
                vladi_commons.label_interpages(page_number, '', roman.toRoman(page_number)))

        text = re.sub('{{колонтитул(?:{{акут3?}}|.)*?}}', colontitul, text, flags=re.DOTALL)

        # for template in wikicode.filter_templates():
        # if template.name.matches(('колонтитул')):
        # if template.has(2) and not paramIsEmpty(template, 2):
        # c2 = str(template.get(2).value.strip())
        # else:
        # c2 = ' — '
        # template.get(2).value = "'''%s.'''" % c2
        # template.get(1).value = vladi_commons.label_interpages(page_number, page_number, '')
        # template.get(3).value = vladi_commons.label_interpages(page_number, '', page_number)
        # # wikicode.remove(template)
        # text = str(wikicode)

        # text = re.compile(r'(^\s*<noinclude>\s*<pagequality[^>]+>.*?)((?:<div class="indent">)?.*?</noinclude>.*?)({{колонтитул.*?}})', re.DOTALL, re.IGNORECASE).sub(r'\1\3\2',
        # text)
        # колонтитул в шапку
        text = re.sub(
            # r'(^\s*<noinclude>.*?<pagequality[^>]+>)(<div class=[\'"]?indent[\'"]?>\s*|)?(.*?</noinclude>.*?)({{[Кк]олонтитул(?:{{акут3?}}|.)*?}})',
            # r'\1\4\2\3',
            # r'(^\s*<noinclude>\s*<pagequality[^>]+>.*?)\s*((?:<div class="indent">)?.*?</noinclude>.*?)({{колонтитул(?:{{акут3?}}|.)*?}})',
            r'(<noinclude>\s*<pagequality[^>]+>.*?)\s*((?:<div class="indent">)?.*?</noinclude>.*?)({{колонтитул(?:{{акут3?}}|.)*?}})',
            r'\1\3\2',
            text,
            flags=re.DOTALL)
        # flags=re.DOTALL | re.IGNORECASE)

        text = re.sub(r'(\s*<noinclude>.*?</noinclude>)\s*', r'\1', text, flags=re.DOTALL)



        # text = re.sub(r'.*?', r'h', text)

        # title = ''
        # for texta in wikicode.nodes:

        # if hasattr(texta, 'title'):
        # 	title_ = re.search(r'^\s*(\d+)\.?\s*$', str(texta.title))
        # 	if title_:
        # 		# if texta.value == '\n={2,}\s*([^=\n]+)\s*={2,} *\n'
        # 		# 	title = texta.value
        # 		title = str(title_.group(1))
        # 	# print(texta.title)
        # 	# print(type(texta))
        # 	# print(str(texta))


        # r = re.search(re_any_title + r'\n\n*(.*?)' + '((?:' + re_any_title + ')|$)', text, re.S)
        # for p in r.groups():
        # print(p)

        # print(part)
        # title = r.group(2)

        # if re.search(r'^\d+\.?$', title):
        # print(title)
        # title = p.group(1).strip()

        # section = mwparserfromhell.parse(p)
        # title = str(section.heading()).strip()
        # for part in section.filter_headings():
        # 	title = str(part.title).strip()
        # for texta in section.filter_text():
        # 	print(texta)

        #
        # if hasattr(texta, 'value'):
        # 	# print(texta.value)
        # 	texta.value = re.sub(r'^(\d+)\. ', '{{стих|глава= %s|стих= %s|цвет=gray}} '    % (title, r'\1'), texta.value)
        # 	texta.value = re.sub(r'\n(\d+)\. ', '\n{{стих|глава= %s|стих= %s|цвет=gray}} ' % (title, r'\1'), texta.value)
        # 	texta.value = re.sub(r' (\d+)\. ', ' {{стих|глава= %s|стих= %s|цвет=gray}} '   % (title, r'\1'), texta.value)
        # 	pass
        #

pass
# text = str(wikicode)
# print(str(wikicode))
# print(text)

vladi_commons.file_savetext(wikipages_filename, text)
# vladi_commons.file_savetext(wikipages_filename, 'll')

