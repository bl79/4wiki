<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>
 <?php
mb_internal_encoding('UTF-8');
setlocale(LC_ALL, 'ru_RU.UTF-8');
$in='wiki.xml';
$out='w-out2.csv';
//$DoShiftForFirstWordsInLines =  true; //закомментировать если не надо
//$DoShiftForFirstWordsInLinesInQoutes =  true; //закомментировать если не надо

$xml = simplexml_load_file($in);
if($xml) {
foreach ($xml->page as $page) {
	$title = $page->title;	// echo $title;
	$text  = $page->revision->text;	//echo $text;

	// Перевод слов из прописных буквами в строчные // в начале строк первые слова
	if ($DoShiftForFirstWordsInLines) {
		if ($result = preg_match_all("/\n\[?([А-ЯЁ́])([-, А-ЯЁ́]{1,}[^-[?,а-яё <(|])\b */u", $text, $found)) {

		foreach ($found[1] as $i => $bukva) {
			$str0 = $bukva.$found[2][$i];
			$str1 = "'''".$bukva.mb_convert_case($found[2][$i], MB_CASE_LOWER, "UTF-8")."'''";
			//echo $str0." ".$str1."<br>";
			$text = mb_ereg_replace("\n".$str0."\b", "\n".$str1, $text);  //	echo $text. "<br>";
			//showarray ($text);
			}
		//showarray($str);	unset($str1);unset($found);
		}
		//showarray ($found);
	}

	if ($DoShiftForFirstWordsInLinesInQoutes) {
		$result = preg_match_all("/\n'''([А-ЯЁ́])(.*?)\b'''/u", $text, $found);	}

	// Перевод заголовков в нижний регистр
	// preg_match_all("/(={5} *)([^=]+)( *={5})/u", $text, $found, PREG_SET_ORDER);
	// foreach ($found as $s) {
		// $text = str_replace($s[1].$s[2].$s[3],  $s[1].mb_ucfirst($s[2]).$s[3],  $text);	}

	// замена "\n" на "##br##"
	$text = mb_ereg_replace("\n", "##BR##", $text);

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
	$list[] = $title."~".$text;
}}

//$fs=fopen($out,'w');
// if (fwrite($fs, $title2) === FALSE) {echo "Не могу произвести запись в файл ($filename)";exit;}
// if (fwrite($fs, $text) === FALSE) {echo "Не могу произвести запись в файл ($filename)";exit;}
//fclose($fs);

//showarray($list);
$fp = fopen($out,'w'); foreach ($list as $line) { fputcsv($fp, explode('~',$line));} fclose($fp);


function showarray($t) {echo '<pre>'.print_r($t,1).'</pre>';}

// В верхний регистр 1-ю букву строки
function mb_ucfirst ($word) {
return mb_strtoupper(mb_substr($word, 0, 1, 'UTF-8'), 'UTF-8') . mb_substr(mb_convert_case($word, MB_CASE_LOWER, 'UTF-8'), 1, mb_strlen($word), 'UTF-8');
}

?>