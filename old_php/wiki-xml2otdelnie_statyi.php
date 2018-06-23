<?php
require 'my.php';
require 'vendor/autoload.php';
$fin='wiki.xml';    $fout='statyi.csv';

$text = file_get_contents($fin);
$xml = simplexml_load_string($text);
//showarray($text);
//showarray($xml);
foreach ($xml->page as $page) {
	//showarray($page);
	$title = $page->title;
	$t  = $page->revision->text;
	
	$title  = str_replace('ТСД/', '', $title);
	$t = preg_replace("/\n/u", "##BR##", $t);

	$result = preg_match("~\{\{tom\|2\|\d\}\}.*?(<section begin=\")(.*?)(\" */>)(?:##BR##)?(.*?)(?:##BR##)?(<section end=.*?>)~us", $t, $found);
	//if ($result) {		showarray($found); }
/*	if (!$result) {     \{\{tom\|2\|\d\}\}	[-\s\na-zA-Z\d="':<>]*
		$titleshort = str_replace('ТСД/', '', $title);
		$titleshort = preg_replace("/(\w+[^йёуеыаоэяиьюъ])( \d+)?$/ui", "\$1ъ\$2", $titleshort);
		if (preg_match("/[ефи]/ui", $titleshort) == 0) $nazvanie_DO[1] = $titleshort;
	}	*/

	//echo $pb[1];
	//showarray($nazvanie_DO); //[1].' # '$pb[1].' | '.$pb[1]
	
	// формат вывода:  # Ссылка на статью || Название_в_ДО # диапазон книги|диапазон скана (или просто номер первой страницы скана)
	//$list[] = '# '.$title.' || '.$nazvanie_DO[1].' # '.$pb[1].' | '.$ps[1];
	//$list[] = $title.'~'.$nazvanie_DO[1].'~'.$pb[1].'~'.$ps[1];
	$list[] = array($title, $found[1].$found[2].$found[3].$found[4].$found[5]);
	//showarray($found);

	//$list[] = array($title, $nazvanie_DO[1], $pb[1],$ps[1]);
	//fsave_csv($fout, $list, '~')
	//implode("~", $array);
}
	showarray($list);
	
// запись файла csv
//fsave_csv($fout, $list, '~')
//file_put_contents($fout, implode ('\r\n',$list);
//fsave($fout, implode ("\n",$list));

?>