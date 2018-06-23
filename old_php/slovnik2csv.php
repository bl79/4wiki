<?php
require 'tsd-vars.php';
$fin='slovnik.xml';    $fout='slovnik.csv';
$text = file_get_contents($fin); $xml = simplexml_load_string($text);
foreach ($xml->page as $page) {
	$title = $page->title;
	$t  = $page->revision->text;

	preg_match_all("~tsds\s*\|(.*?)\s*\|(.*?)\s*\|(.*?)\s*(?:\|(.*?)\s*)?[|}]~u", $t, $found, PREG_SET_ORDER);

	foreach ($found as $a) {
		$pagename = $a[1];
		$nazvanie_do = $a[2];
		$nazvanie_so = $a[3];
		$pnum = $a[4];
		//$list[] = array($pagename, $nazvanie_do, $nazvanie_so, $pnum); // параметры словника
		$list[] = array('ТСД/'.$pagename); // имена страниц

	}
}
	//showarray($list);
    //$key = array_search('Р', $list);

fsave_csv($fout, $list, '~');
?>