<?php
require 'my.php';
//require './vendor/autoload.php';
//require 'vendor/simple-html-dom/simple-html-dom/simple_html_dom.php';
include('simple_html_dom.php');
$fin='ya.html';    $fout='file_out.csv';
$text = file_get_contents($fin); 

//$html = new simple_html_dom();
// Load from a string
//$html = load("<html><body><p>Hello World!</p><p>We're here</p></body></html>");
//$html = str_get_html("<html><body><p>Hello World!</p><p>We're here</p></body></html>");
//$html = str_get_html("<html><body><p>Hello World!</p><p>We're here</p></body></html>");

$HTMLCode = "<html><body><p>Hello World!</p><p>We're here</p></body></html>";
$dom = new DomDocument();
$dom->preserveWhiteSpace = false;
$dom->loadHTML($HTMLCode);
//$dom->loadHTML($text);
$xpath = new DomXPath( $dom );
//print_r($text);
// Load a file
//$html->load_file($fin);
//$html = file_get_html($fin);
//$a = $html->find('a');

//$pogoda= $xpath->query(".//*[@class='temp']/dd"); // шаг 4
//echo $pogoda->item(0)->nodeValueass='temp']/dd"); // шаг 4
//$dl= $xpath->query("html/body/mediawiki/table/tbody/tr/td/div/dl[6]/dt/a/span");
$dl = $xpath->query(".//*p");

foreach ($dl as $i) {
	echo $i;
}

//echo $dl->item(0)->nodeValue;
print_r($dl);

print_r($xpath);
//print_r($html);
//print_r($a);
/*
foreach ($html->page as $page) {
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
}*/

	//showarray($list);
    //$key = array_search('Р', $list);

//fsave_csv($fout, $list, '~');
