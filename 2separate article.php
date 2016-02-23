<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>
 <?php
$in='w-out2.txt';
$out = "articles.csv";

$fp = fopen($in, 'rt');  // Текстовый режим
//$t = fgetcsv ($fp);

while (($t = fgetcsv ($fp)) !== FALSE) {
	//showarray($t);
	//echo $t[1];
	//
	$page = explode ('##BR##=', $t[1]);
	//echo $str;
	//showarray($page);
	//echo $page[1];
	foreach($page as $str){
		//echo $str.'<br />';
		//echo $page[1];
		$str = preg_replace("/\[\[Категория.*?\]\]/u", "", $str);
		//$str = preg_replace("/\{\{ТСД.*?\}\}/u", "", $str);
		//$str = preg_replace("/\{\{TOCright.*?\}\}/u", "", $str);
		//$str = preg_replace("/\{\{Шаблон[^{]*?\}\}/u", "", $str);
		//$str = preg_replace("/\{\{Отексте[^{]*?\}\}/u", "", $str);
		// $resl = preg_match("/(\{\{[^{]*?\}\})/u", $str, $r);
		// $resl = preg_match("/(\{\{[^{]*?\}\})/u", $str, $r);
		// $resl = preg_match("/(\{\{[^{]*?\}\})/u", $str, $r);
		// $resl = preg_match("/(\[\[Категория.*?\]\])/u", $str, $r1);
		// echo $r1[1].'<br />';
		$result = preg_match("/={3,} *(.*?) *={1,}(?:##BR##)+(.*?)(?:##BR##)*$/u", $str, $found);
		if (!$result) continue;
		//showarray($found);
		$list[] = $found[1]."~".$found[2];
	}
}
fclose($fp);


//$text = file_get_contents ($in);
//explode (  , $text )

// замена "<b></b>" на "''' * '''"
//$text=mb_ereg_replace("'''(.*?)'''", "<b>\\1</b>", $text);
///$text=preg_replace("/<\/?b>/u", "'''", $text);
// замена "<i></i>" на "'' * ''"
///$text = preg_replace("/<\/?i>/u", "''", $text);
//$text=mb_ereg_replace("''(.*?)''", "<i>\\1</i>", $text);


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


//showarray($list);
$fp = fopen($out,'w'); foreach ($list as $line) { fputcsv($fp, explode('~',$line));} fclose($fp);

///file_put_contents ($out, $text );

function showarray($t) {echo '<pre>'.print_r($t,1).'</pre>';}

?>