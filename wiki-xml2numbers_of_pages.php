<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>
 <?php
require 'my.php';
//$in='wiki.xml';   $out='w-out2.csv';
$fin='wiki.xml';    $fout='slovnik s paginaziey.csv';
//$list = array();

$xml = simplexml_load_file($fin);
if($xml) {
foreach ($xml->page as $page) {
	$title = $page->title;
	$text  = $page->revision->text;	
	$nazvanie_DO = '';
	
	$title  = str_replace('ТСД/', '', $title);
	$result = preg_match("/ДОРЕФОРМЕННАЯ_ОРФОГРАФИЯ *= *([\w]+)\n/u", $text, $nazvanie_DO);	
/*	if (!$result) {		
		$titleshort = str_replace('ТСД/', '', $title);
		$titleshort = preg_replace("/(\w+[^йёуеыаоэяиьюъ])( \d+)?$/ui", "\$1ъ\$2", $titleshort);
		if (preg_match("/[ефи]/ui", $titleshort) == 0) $nazvanie_DO[1] = $titleshort;
	}	*/
	preg_match("/2-ИЗД.ТОМ *= *([-—−\d ]+)\n/u", $text, $tom);	
	preg_match("/2-ИЗД.СТРАНИЦА СКАНА *= *([-—−\d ]+)\n/u", $text, $ps);
	preg_match("/2-ИЗД.СТРАНИЦЫ КНИГИ *= *([-—−\d ]+)\n/u", $text, $pb);

	//echo $pb[1];
	//showarray($nazvanie_DO); //[1].' # '$pb[1].' | '.$pb[1]
	
	// формат вывода:  # Ссылка на статью || Название_в_ДО # диапазон книги|диапазон скана (или просто номер первой страницы скана)
	//$list[] = '# '.$title.' || '.$nazvanie_DO[1].' # '.$pb[1].' | '.$ps[1];
	//$list[] = $title.'~'.$nazvanie_DO[1].'~'.$pb[1].'~'.$ps[1];
	$list[] = "$title~$nazvanie_DO[1]~$pb[1]~$ps[1]";
	//$list[] = array($title, $nazvanie_DO[1], $pb[1],$ps[1]);
	//fsave_csv($fout, $list, '~')
	//implode("~", $array);
}
}
	showarray($list);
// запись файла csv
fsave_csv($fout, $list, '~')
//file_put_contents($fout, implode ('\r\n',$list);
//fsave($fout, implode ("\n",$list));

?>