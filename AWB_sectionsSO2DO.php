<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title></head><body>
<?php

require 'tsd-vars.php';


$txt = "<section begin=\"Армада\" />'''Арма{{акут}}да, ''армадилъ''''' <small>ипр.</small>, см. ''{{tsdl|армія}}''.{{tsdbr}}{{tsdbr}}<section end=\"Армада\" />";




// <section begin="([^"]*[^\d])" */ *>
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


printf ($txt);


function replace($t)
{
	//$t = $t[0].'iiii';
	$t = 'iiii';
  return $t;

}
