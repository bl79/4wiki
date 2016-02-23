 <?php
require 'my.php';
require 'vendor/autoload.php';

$fin='checkedpages.xml';
$fout='razr-list.txt';
//$text = file_get_contents($fin); $xml = simplexml_load_string($text);
$xml = simplexml_load_file($fin);
foreach ($xml->page as $page) {
	$text  = $page->revision->text;
	$text = str_replace('{{Акут}}', '', $text); // ударения → '{{акут}}'	
	if (preg_match_all("/\{\{razs\|[-—−]([\w]*\b)[, ]?\}\}/u", $text, $found)) {
		//showarray($found);
		$list[] = $found[1];
	}
}
	use Belt\Belt;
	$list = Belt::flatten($list);
	$uniq = Belt::unique($list);
	sort($uniq);
	$sortcounts = array_count_values($list);	
	//arsort($sortcounts); showarray($sortcounts);
	//krsort($sortcounts); showarray($sortcounts);
	showarray($uniq);

//showarray($list);

// запись файла csv
//fsave_csv($fout, $list);
file_put_contents($fout,  implode(PHP_EOL, $uniq));
//fsave($fout, implode ("\n",$list));


?>