<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>
 <?php
$in='w-out3.txt';
$out='w-out.txt';

//$fp = fopen($in, 'rt'); // Текстовый режим
$text = file_get_contents ($in);
	
// замена "<b></b>" на "''' * '''"
//$text=mb_ereg_replace("'''(.*?)'''", "<b>\\1</b>", $text);
$text=preg_replace("/<\/?b>/u", "'''", $text);	
// замена "<i></i>" на "'' * ''"
$text = preg_replace("/<\/?i>/u", "''", $text);	
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
//$fp = fopen($out,'w'); foreach ($list as $line) { fputcsv($fp, explode('~',$line));} fclose($fp);
file_put_contents ($out, $text );

function showarray($t) {echo '<pre>'.print_r($t,1).'</pre>';}

?>