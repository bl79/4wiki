<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title></head><body>
<?php

require 'tsd-vars.php';

$f ='AWBfile.txt';
$txt = file_get_contents($f);
//$txt = "<section begin=\"Армада\" />'''Арма{{акут}}да, ''армадилъ''''' <small>ипр.</small>, см. ''{{tsdl|армія}}''.{{tsdbr}}{{tsdbr}}<section end=\"Армада\" />";

$txt = preg_replace_callback('~(<section begin="([^"]*(?:[а-яёѣѵіѳА-ЯЁѢѴІѲ-](?: \d)?|[^а-яёѣѵіѳА-ЯЁѢѴІѲ-]\d))" */ *>\s*)(.*?)(\s*<section end="\2" */ *>)~usi',
		function ($s) {
			$t = $s[3];
			//$t = addslashes($t);
			$t = oformlenie($t);
			$t = toDO($t);
			//$t = stripslashes($t);
			//echo htmlspecialchars($t);
			return $s[1].$t.$s[4];},
		$txt);

file_put_contents($f, $txt);


