<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>
 <?php
//$in='wiki.xml';   $out='w-out2.csv';
$in='wiki.xml';    $out='w-out3.csv';

$xml = simplexml_load_file($in);
if($xml) {
foreach ($xml->page as $page) {
	//$title = $page->title;	// echo $title;
	$text  = $page->revision->text;	//echo $text;

	// замена "\n" на "##br##"
	$text = preg_replace("/\n/u", "##BR##", $text);

	$page = explode ('##BR##=', $text);

	foreach($page as $str){
		$str = preg_replace("/##BR##\<\/div\>/u", "", $str);
		$str = preg_replace("/\[\[Категория.*?\]\]/u", "", $str);
		$str = preg_replace('/<section (begin|end)=".*?" \/>(?:##BR##)?/u', "", $str);		
		//$str = preg_replace("/\{\{ТСД.*?\}\}/u", "", $str);
		//$str = preg_replace("/\{\{TOCright.*?\}\}/u", "", $str);
		//$str = preg_replace("/\{\{Шаблон[^{]*?\}\}/u", "", $str);
		//$str = preg_replace("/\{\{Отексте[^{]*?\}\}/u", "", $str);
		// $resl = preg_match("/(\{\{[^{]*?\}\})/u", $str, $r);
		// echo $r1[1].'<br />';
		$result = preg_match("/={2,} *(.*?) *={1,}(?:##BR##)+(.*?)(?:##BR##)*$/u", $str, $found);
		if (!$result) continue;
		$article = $found[2];
		
		// Добавление категорий
		if (mb_stripos($article, '[[Толковый словарь:')) $article = $article.'##BR##[[Категория:ТСД:Со ссылками на переиздание98]]';		
		if (mb_stripos($article, '[ср. ')) $article = $article.'##BR##[[Категория:ТСД:Перенаправления в ботозаливке - "ср."]]';
		
		// Перенаправления
	/*	if (mb_stripos($article, 'см.')) {
			$article = $article.'##BR##[[Категория:ТСД:Перенаправления в ботозаливке - «см.»]]';
			if (mb_stripos($article, 'см. это')) $article = $article.'##BR##[[Категория:ТСД:Перенаправления в ботозаливке - «см. это»]]';
			if (mb_stripos($article, 'см. также')) $article = $article.'##BR##[[Категория:ТСД:Перенаправления в ботозаливке - «см. также»]]';
			if (mb_stripos($article, 'см. на своем месте')) $article = $article.'##BR##[[Категория:ТСД:Перенаправления в ботозаливке - «см. на своем месте»]]';
			if (mb_stripos($article, 'см. выше')) $article = $article.'##BR##[[Категория:ТСД:Перенаправления в ботозаливке - «см. выше»]]';
			if (mb_stripos($article, 'см. ниже')) $article = $article.'##BR##[[Категория:ТСД:Перенаправления в ботозаливке - «см. ниже»]]';
			if (mb_stripos($article, "см. ''<small>")) $article = $article."##BR##[[Категория:ТСД:Перенаправления в ботозаливке - «см. ''<small>»]]";
			if (mb_stripos($article, 'см. <small>')) $article = $article.'##BR##[[Категория:ТСД:Перенаправления в ботозаливке - «см. <small>»]]';
			if (mb_stripos($article, "см. ''")) $article = $article."##BR##[[Категория:ТСД:Перенаправления в ботозаливке - «см. ''»]]";
			
			// // Создание ссылки и перевод терминов в нижний регистр
			// preg_match_all("/([Сс]м\.)( *)(?:'')?(\w+)(?:'')?\./u", $article, $f, PREG_SET_ORDER);
			// foreach ($f as $s) {
				// $article = str_replace($s[1].$s[2].$s[3],  $s[1]." ''[[ТСД/".mb_ucfirst($s[3])."|".$s[3]."]]''",  $article);	
				// $article = $article."##BR##[[Категория:ТСД:Перенаправления в ботозаливке - со ссылкой]]";
			// }
					
			// Создание ссылки и перевод терминов в нижний регистр, с ударением
			if (preg_match_all("/([Сс]м\.)( *)('')?([\ẃ]+)('')?\./u", $article, $f, PREG_SET_ORDER) > 0) {
				foreach ($f as $s) {
					$bezUdareniaIregistr = mb_ucfirst($s[4]);
					$bezUdareniaIregistr = preg_replace("/́/u", "", $bezUdareniaIregistr); // удаление ударения
					$article = str_replace($s[1].$s[2].$s[3].$s[4].$s[5],  $s[1]." ''[[ТСД/".$bezUdareniaIregistr."|".$s[4]."]]''",  $article);				
				}
				// if (mb_stripos($s[4], '́')) $article = $article."##BR##[[Категория:ТСД:Перенаправления в ботозаливке - со ссылкой, с ударением]]";
				// else 
				$article = $article."##BR##[[Категория:ТСД:Перенаправления в ботозаливке - со ссылкой]]";
			} else $article = $article."##BR##[[Категория:ТСД:Перенаправления в ботозаливке - без ссылки]]";
		}
		
		
		$list[] = $found[1]."~".$article; // запись со статьями
		//$list[] = $found[1]; // только заголовки
		
	}
	*/

	//$result = preg_match_all("/\'\'\'(.*?)\'\'\'/", $text, $found);
	//showarray($found);
	//for ($i=1;$i<=10;$i++) {
	//$text=mb_ereg_replace("(=##BR##.*?)'''(.*?)'''(.*?\n)", "\\1<b>\\2</b>\\3", $text);
	//}

	// замена "''' * '''" на "<b></b>"
	//$text=mb_ereg_replace("'''(.*?)'''", "<b>\\1</b>", $text);
	// замена "'' * ''" на "<i></i>"
	//$text=mb_ereg_replace("''(.*?)''", "<i>\\1</i>", $text);



	//$text=mb_ereg_replace("\s+(</[ib]>)([^\s])", "\\1 \\2", $text);
	//$text=mb_ereg_replace("([^\s])(<[ib]>)\s+", "\\1 \\2", $text);
	//$result = preg_match_all("/\s+(<\/[ib]>)([^\s])/u", $text, $found);
	//showarray($found);

	// составление строки для csv - заголовок статьи | название
	//$list[] = $title."~".$text;
}}

//$fs=fopen($out,'w');
// if (fwrite($fs, $title2) === FALSE) {echo "Не могу произвести запись в файл ($filename)";exit;}
// if (fwrite($fs, $text) === FALSE) {echo "Не могу произвести запись в файл ($filename)";exit;}
//fclose($fs);

//showarray($list);
$fp = fopen($out,'w'); foreach ($list as $line) { fputcsv($fp, explode('~',$line));} fclose($fp);


function showarray($t) {echo '<pre>'.print_r($t,1).'</pre>';}

// В верхний регистр 1-ю букву строки
function mb_ucfirst ($word) {return mb_strtoupper(mb_substr($word, 0, 1, 'UTF-8'), 'UTF-8') . mb_substr(mb_convert_case($word, MB_CASE_LOWER, 'UTF-8'), 1, mb_strlen($word), 'UTF-8'); }


?>