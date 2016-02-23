﻿ <?php
require 'my.php';
//$fin='0043.fb2';
$fin='tsd3-1-allpages.xml';
//$fin='tsd-3-3ocr.txt';
$fout='tsd3-1ocr-out.csv';
$text = file_get_contents($fin);

$xml = simplexml_load_string($text); //showarray($xml);
foreach ($xml->FictionBook as $page) {
	//showarray($page);	//showarray($page->description->{'title-info'}->{'book-title'});
	//if (preg_match("/Том \d - 0*(\d+)$/us", // 2-4 тома
	if (preg_match("/Том_1_\(Даль_1903\) - 0*(\d+)$/us",  // 1 том
		$page->description->{'title-info'}->{'book-title'}, $found)) {		
		$number = (string) $found[1]; //+2;
		$list[] = array(
			'number' 	=> "Страница:Толковый словарь. Том 1 (Даль 1903).djvu/".$number,
			'text'		=> $page->body->asXML()
		);
	} else continue;
}
	//showarray($list);


foreach ($list as $pn => $page) {
	//showarray($i);
	//showarray($text);
	$t = $page['text'];   
	$t = preg_replace("/\r/u", "", $t); // удалить все \r, работать с \n
	$t = firstCleanTags($t);
//showarray($t);
	$t = smallWithDot($t);

	$t = preg_replace("/(\{\{выступ\|[ '!-~]*)([-а-яёѣѵіѳ́А-ЯЁѢѴІѲ]+\b)/u", "$1'''$2'''$3", $t); // первый термин  → в bold
	$t = str_replace("].''}}", "''].}}", $t);
	$t = preg_replace("/\.?,}}/u", ".}}", $t);
	$t = preg_replace("/(\[Ср\.)\}\}\n\{\{выступ\|/u", "$1 ", $t); 
	$t = preg_replace("/(\w)\}\}\n\{\{выступ\|/u", "$1 ", $t); 
	$t = preg_replace("/\[Си-\./u", "[См.", $t); 
	$t = preg_replace("/ щица/u", " '''—щица'''", $t); 
	$t = preg_replace("/([-—]) /u", "$1", $t); 
	
	// добавление секций
	$t = preg_replace("/(\{\{выступ\|[[\d. ]*''')(.*?)('''.*?\}\})/u", '<section begin="$2" />$1$2$3<section end="$2" />', $t); // +секции
	for ($i=1;$i<=4;$i++) {$t = preg_replace("/(section (?:begin|end)=\"[^\"]*)[́ ˊ']([^\"]*\")/u", '$1$2', $t);} // уборка ударений, ', пробелов из секций
	for ($i=1;$i<=4;$i++) {		// -ДО в <section>
		$t = preg_replace('/(="[^"]*)ѣ([^"]*" \/>)/u', '$1е$2', $t);
		$t = preg_replace('/(="[^"]*)ѳ([^"]*" \/>)/u', '$1ф$2', $t);
		$t = preg_replace('/(="[^"]*)і([^"]*" \/>)/u', '$1и$2', $t);
		$t = preg_replace('/(="[^"]*)ѵ([^"]*" \/>)/u', '$1и$2', $t);
		$t = preg_replace('/(="[^"]*)ъ(" \/>)/u', '$1$2', $t);}

	
		
	$t = ChtoKogo($t);
	$t = cleanApos($t);
	
	// 
	$t = str_replace('±', '{{!}}', $t); // возврат временной замены '±' → '{{!}}'
	$t = str_replace('́', '{{акут}}', $t); // ударения → '{{акут}}'	
	$t = preg_replace("/^[\n\r]+(.*?)[\n\r]+$/us", "$1", $t); // trim страниц
	$t = preg_replace("/\n\r?/u", "##BR##", $t); // \n → ##BR##

	$list[$pn]['text'] = $t; //showarray($t);
}
//showarray($list);

// запись файла csv
fsave_csv($fout, $list);
//file_put_contents($fout, implode ('\n\r',$list);
//fsave($fout, implode ("\n",$list));


function firstCleanTags($t) {	
	$t = preg_replace('~<binary.*?/binary>~u', '', $t);
	$t = str_replace('{', '[', $t); $t = str_replace('}', ']', $t);
	$t = preg_replace("/([^.])\.\.([^.])/u", "$1.$2", $t);
	$t = preg_replace("/[~§№•■♦►°±*‘’™©®«»“”\"„$^]+/u", "", $t);
	$t = str_replace("&apos;", "", $t);
	$t = preg_replace("/(&gt;|&lt;)/u", "", $t);
	$t = preg_replace("/([^а-яёѣѵі])́/ui", "$1", $t); 
	$t = preg_replace('~<a l:href=.*?a>~u', "", $t); 	
	$t = preg_replace("/([^'])'([^'])/u", "$1$2", $t); // -одиночные '
	$t = preg_replace("/[ \t]+/u", " ", $t);	// пробелы/табуляции в 1 пробел
	
	$t = str_replace('<strong></strong>', '', $t);
	$t = str_replace('<emphasis></emphasis>', '', $t);
	//$t = str_replace('<sub></sub>', '', $t);
	//$t = str_replace('<sup></sup>', '', $t);	
	//$t = preg_replace('\<strong\>( *)/u', "$1'''", $t);	$t = preg_replace('/( *)\<\/strong\>/u', "'''$1", $t);
	$t = str_replace('<strong>', "", $t);	$t = str_replace('</strong>', "", $t);
	$t = preg_replace('~<emphasis>( *)~u', "$1''", $t);$t = preg_replace('~( *)</emphasis>~u', "''$1", $t);
	$t = str_replace('<sub>', '', $t);	$t = str_replace('</sub>', '', $t);
	$t = str_replace('<sup>', '', $t);	$t = str_replace('</sup>', '', $t);
	$t = preg_replace('~<empty-line/>~u', "\n\r", $t);
	$t = preg_replace('~</?section>~u', '', $t);	
	$t = preg_replace('~</?body>~u', '', $t);
	$t = preg_replace('~</?title>~u', '', $t);

	$t = str_replace('€', 'С', $t);
	$t = preg_replace('/[-.,](ж|м)[.,]/u', ' $1.', $t);
	$t = preg_replace('/ (ж|м|ср|см) /ui', ' $1. ', $t);
	$t = str_replace('воеп.', 'воен.', $t);
	$t = preg_replace("/(раст)[ипчцймкляа][.,]/ui", "$1н.", $t);
	$t = preg_replace("/\b[ипчцймкл]ѣм[.,]/ui", "нѣм.", $t);
	$t = str_replace("ем. ''", "см. ''", $t);
	$t = str_replace("&amp;", "а́", $t);	
	$t = str_replace("чбк", "чо́к", $t);	
	$t = preg_replace("/[се]о[ес]т[инп]\./u", "состн.", $t);
	$t = preg_replace("/ііъ\b/u", "нъ", $t);
	$t = preg_replace("/ (м[нипклцйч])[.,]/u", ' $1.', $t);
	$t = preg_replace("/\*/u", "*", $t);
	$t = preg_replace("/ '''([а-яёѣѵіѳѢѴІѲЁ])''' /u", " $1 ", $t);	
	
	$t = preg_replace("/[-−—]с *я/u", "''—ся''", $t);		
	$t = preg_replace("/[-−—](щ|н) *и *к *о *в( *ъ)?/u", "''—$1иков$2''", $t);		
	$t = preg_replace("/[-−—](щ|н) *и *к( *ъ)?/u", "''—$1ик$2''", $t);		
	$t = preg_replace("/[-−—](щ|н) *и *ц *а/u", "''—$1ица''", $t);
	
	
	//$t = preg_replace("/[^]\w'\d\.!?]\}\}/u", '}}', $t); много лишнего находит
	//$t = preg_replace("/ [нпклмчы] /u", " и ", $t); одиночно стоящие согласные без "ъ". Ошибки, ибо находит слова с разрядкой.
	
	$erpipes = "(?:\| *\||II|ll|11|\| *[()] | [()] *\||[][] *[][]|/ */|\|[,i:;,]\|)";
		$t = preg_replace("~([\w\d']+)".$erpipes." ~u", '$1 || ', $t);
		$t = preg_replace("~ ".$erpipes."([\w\d']+)~u", ' || $1', $t);
		$t = preg_replace("~ ".$erpipes." ~u", ' || ', $t);
		$t = preg_replace("~\\\ *\\\~u", ' || ', $t);
	// $t = str_replace('||', '±±', $t); 
	$t = str_replace('|', '±', $t); // временная замена '|' → '±'  // '||' → '{{!}}{{!}}'
	
	$t = str_replace(" 0 ", " О ", $t);	$t = str_replace(" Ѳ ", " О ", $t);
	
	$t = preg_replace("~<p> *І\. +~u", "<p>1. ", $t);
	$t = preg_replace("~(<p>) *''%'' *~u", "$1 2. ", $t);	
	$t = preg_replace("~(<p>) *[-•‘’.,:;!&%$\|\"/] *~u", "$1", $t);
	$t = preg_replace("~(<p>) *\( *~u", "$1[", $t);	
	//$t = preg_replace("/(\<p\>) *'([^'])/u", "$1", $t);	
	$t = preg_replace("~(<p>1.*?)</p>\n*<p>(.*?</p>)\n*<p> *'*%'* *~us", "$1$2 \n\n<p>2. ", $t); // объединнение абзацев начин с % - плохое распозн. '2.'
	$t = preg_replace("~</p>\n*<p>\s*([—,.!?'\[* ]*[а-яёѣѵіѳ])~u", " $1", $t); // объединнение абзацев начин с % - плохое распозн. '2.'
	$t = preg_replace("/%+/u", "", $t);
	
	//$text = str_replace('</p>', '\n', $text);
	//$text = str_replace('<p>', '', $text);
	$t = preg_replace('~ *<p> *~u', '{{выступ|', $t);	$t = preg_replace('~ *</p> *~u', '}}', $t);	 // обёртка в {{выступ|...}}
	$t = preg_replace('/[\n]+(\{\{выступ)/u', "\n\n$1", $t);	
	
	$t = preg_replace("~\}\}(<section end[^>]* />)[\n\s]*<section begin=(\"[^\"]*\") />\{\{выступ\|('*-'* *[а-яёѣѵіѳ].*?\}\})<section end=\2 />~u", " $3$1", $t); // объед. переносов строк:  силь-'''}}<section end="[Переснятие], " />	
		
	$t = preg_replace('/(\{\{выступ\|)[ЗзВв8]\./u', '{{выступ|3.', $t);
	$t = preg_replace('/(\{\{выступ\|)[Чч]\./u', '{{выступ|4.', $t);
	$t = preg_replace("/(выступ\|) *'*(\d)\.?'*\.? */u", "$1$2. ", $t); // удаление ' перед цифрами, + . после
	$t = preg_replace("/(выступ\|) *('+) *\[ */u", "$1[$2", $t); // '''[ - перенос начальной ''' за [
	
	
	return $t;
}


function cleanApos($t) {	
	$t = preg_replace("/([^'])''([- ])''([^'])/u", '$1$2$3', $t); 	// '' ''
	$t = preg_replace("/([^'])'''([- ])'''([^'])/u", '$1$2$3', $t); // ''' '''
	$t = preg_replace("/([^'])'''''([- ])'''''([^'])/u", '$1$2$3', $t); // ''''' '''''
	$t = preg_replace("/([^'])('''''')([^'])/u", '$1$2$3', $t); 	// ''''''
	$t = preg_replace("/([^'])('''')([^'])/u", '$1$2$3', $t); 		// ''''
	$t = preg_replace("/-''' '''-/u", '', $t); 						// -''' '''-
	$t = preg_replace("/([^'])''' '''[-—](\w)/u", '$1$2', $t); 		// ''' '''-\w
	return $t;
}


function smallWithDot($t) {
	$s = 'ж|м|наре?ч?|вм|(?!\[)ср|место?и?м|прила?га?т|более употреб\. мн\. ч|об|на?пр|сокращ|притяжат|прдл|мн|[Мм]н\. ч|ед\. ч|мно?го?кра?т?н?|нескло?н?|[Вв]заимн|ипр|взм|[Вв]о?звр?|[Ии]носказат|[Бб]езли?ч?н?|[Уу]корит|[Уу]велич|[Сс]острадат|стрд|[Лл]ьстит|[Уу]низит|умали?т?|[Пп]резрит|повел|[Лл]аскат|про?ти?во?пло?ж?|[Пп]ере?во?дн|[Нн]а?пр|возм|окнч|ошибч|искаж|ме?ждм?т?|неупотр|малоуп|шуто?ч|одно?кра?т?н?(?:\. (?:не ?употр|не употреб|неупотреб))?|гово?р|прич|ука?за?т|(?:иногда |ино |местами |если )?произн|дейст. по знач. гл.'; // small с точкой
	$s =$s.'|'.'(?:с )?фра?нц?|корел(?:ьск)?|птрб|уф|вост\. тмб|астрх|нвг|вят|вла?д|влгд|ка?вк|ко?стр|мск|пск|пен|сар|сиб|смб|смл|кур|вор|каз-цыв|каз|арх\.\-мез|арх\.\-кем|сѣв\. вост|сѣв\-вост|южн?|запд?|вост|сѣв|(?:с )?[Гг]реч|[Гг]рчск|итал|латн?|[Пп]е?рси?дс?к?|[Пп]ольск|нѣм(?:ецк?)?|как н[еѣ]мецк|[Зз]ырянск|гдв|оре?нб|ол|орл|охотн|остржс|ряз|та?мб|тве?р|яро?сл?|пе?рм|ка?мч|че?рно?мо?р?(?:ск?)?|белмрс|донс|[Чч]еляб|чувашс?к?|чух|татр|[Тт]ата?рс?к?|гола?ндс?|голл|урал\.\-казач|[Ии]спа?н?|[Ии]сланд|ирк|[Мм]адьярск?|[Мм]онго?ль?с?к?|арабск|[Бб]есс?ар(?:абск)?|молд|подольс|болг|слвц|ниж|верх|черем|ма?ло?ро?с|белрс'; // small с точкой
	$s =$s.'|'.'астроном|[Нн]аучн|[Бб]ран|стар|арх|особ|простонард|собират|це?рк|политч|католич|врчб|врач|[Вв] [Мм]атем(?:ат)?|[Фф]из(?:ич)?|мед|анато?м?|воен|[Зз]одческ|[Сс] офенск|[Уу]чен|мо?рск?|солд(?:атск)?|\(?(?:Наум|Шейнъ)\.?\)?|\(на длинной\)|[Бб]ол|[Дд]етск|[Хх]имич|[Гг]орн|[Зз]аводск'; // small с точкой
	$s = $s.'|'.'сказ(?:очн)?|местн|пчеловод|грамматич|мельнич|типогр|ле?то?пи?с?н?|офе?нс?|солеварен|числит|арифметич|[Жж]ивотн|о челов';
	$s = $s.'|'.'Ио\. Экс|Ака?д(?:\. Сло?в?(?:ар.)?)?|Словарь Академии Акад|(?:Сло?в?\. )?Ака?д?|[АА]кад. Сл|(?:Ефр\. )?Сир|Опд|Оп|Пролог|Кол|Дрвн. Вивл|Паралипоменон|Ирмологий|Опис. Румнц|Ратн. Уст(?:ав)?|Разрд|Апокалипсис|Ездра|Соломон|Судебник|Уложение|Приказн|Макка?в|Галат|Сирах|Скрж|Римлян|(?:К\. )?Аксаков|Крылов|Пушкин|Ломоносов|Державин|Грибоедов|Карамзин|Исаия|Акты|Ратный Устав|Слово о Полку Игореве|Кошихи?н|Жуковск|Русская Правда|Измл|Иерем|Ирием|Абакум|Никон(?:\. летопись)?|Тим|(?:Кн\. )?Суд|Соборник|Исхо?д|Левит|Петр|Мрк|Мак|Евр|Лука?|Притч|Псалт?|Псалмы|Посл|[Сс]тар|Лѣтпс|Дѣян|[Уу]мад|[Пп]слт|Иезе?к(?:иль)?|Цар(?:ствен)?\. Кн|(?:Кн(?:\.|ига) (?:\d )?)?Царс?т?|Мин(?:е[яи])?|Руфь|Иис. Нав|Иак|Исх|Иер|Иеремия|Числ|Иоан|Иона|Иов|Улож|Лев|Кор(?:инф(?:янам)?)?|Пет|Кормч\. Кн|Кормч|Криф|Нест(?:о?р)?|стхр|Премудрости Соломона|Иордан|Ефес|(?:Кн\. )?Быт';
	$t = preg_replace("/([['(){} ])((?:отъ |съ |[Вв] )?(?:\b".$s."))('+)\./ui", '$1<small>$2.</small>$3', $t);
	$t = preg_replace("/([['(){} .])((?:отъ |съ |[Вв] )?(?:\b".$s.")\.)/ui", '$1<small>$2</small>', $t); //([]\s,'’;:}()])

	// small с точкой регистрозависимое
	$t = preg_replace("/(\{\{выступ\|[[?\d. ]* '''[\ẃ]+''' (ср\.))\b/u", "$1<small>$2</small>", $t);

	// оптимизация small	
	$t = preg_replace("~</small>([ ']*)(или|и)([ ']*)<small>~u", "$1$2$3", $t);
	$t = preg_replace("~</small>([ '(),.]*)<small>~u", "$1", $t);
	
	return $t;
}


function ChtoKogo($t) {
	$chars = '-, А-яЁ́ёѣѵіѳѢѴІѲ()';
	
	$s = 'безлично|что на что|что|кому|чего во что|чего у кого|куда или на что|что кому или на что|за что|кого от чего|что куда или кому|кому что или о чем|от кого|от чего|к чему|чему|чего кому|чего куда|кому чем|по ком|куда|зачем|над чем|кому или чему|с чем|кого чем|с кем|чья|в чем или к чему|откуда|из или у кого|до чего|во что|п?о чем|что во что или куда|противу кого|с кем|в чем|перед кем|в кого|что кого|с кого|на кого|куда или во что|что во что|у кого|кому что|во что|кому или от чего|кого|чего|кто|кому|что или чем|кого во что|где|чем|кого куда|к кому|что кому|что чем|кого|на что|что от кого|пред кем|куда|кому на что|при ком или у кого';
	$s = '(?:'.$s.')[,:;]?';
	
	for ($i=1;$i<=4;$i++) {	$t = preg_replace("/(\{\{выступ\|[[\d. ]*'''[".$chars."]+[]?*!]?'''[]?*!]?(?:,| или\b| и\b)? *(?:[".$chars."]*)?(?:,? ))(".$s.")/u", "$1<small>$2</small>", $t); }	
		
	for ($i=1;$i<=4;$i++) {	$t = preg_replace("/(\{\{!\}\}) *(".$s.")( ".$s.")?( ".$s.")?( ".$s.")?/u", "$1 <small>$2$3$4$5</small>", $t); }
	
	return $t;
}
?>