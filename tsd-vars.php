<?php
require 'my.php';
require 'vendor/autoload.php';

$tom	= 1;
switch ($tom) {
	case 1:
		$offset 		= 90;
		$startpage 		= 1;
		$maxpages 		= 723;
		$pname4index	= 'Толковый словарь Даля (2-е издание). Том 1 (1880).pdf';
		break;
	case 2:
		$offset 		= 9;
		$startpage 		= 1;
		$maxpages 		= 807;
		$pname4index 	= 'Толковый словарь Даля (2-е издание). Том 2 (1881).pdf';
		break;
	case 3:
		$offset 		= 8;
		$startpage 		= 1;
		$maxpages 		= 576;
		$pname4index	= 'Толковый словарь Даля (2-е издание). Том 3 (1882).pdf';
		break;
}
$pname 			= 'Страница:'.$pname4index.'/';
$prefix			= 'tsd2_dop';
$dbtable 		= $prefix.'_'.$tom;
$fprefix 		= $prefix.'-'.$tom.'-';
$fwordlist		= $fprefix.'wordlist.xml';
$fallpages		= $fprefix.'allpages.xml';
$fout2index		= $fprefix.'pages2index.csv';
$fout2tagpages	= $fprefix.'articles2tagpages.csv';
$br = '##BR##';


// общая оптимизация и оформление
function oformlenie($t) {
	$t = preg_replace("/ +/u", " ", $t); // двойные пробелы
	$t = str_replace('||', '{{!}}{{!}}', $t);
	$t = str_replace('́','{{акут}}', $t);	$t = str_replace('ˊ','{{акут3}}', $t);
	$t = str_replace('{{акут}}{{акут}}','{{акут}}', $t);	$t = str_replace('{{акут3}}{{акут3}}','{{акут3}}', $t);
	// обработано $t = preg_replace("~(?<![][{}<:.|/-])(\b[a-z]+[a-z ]+[a-z]+\b)(?![\}</])~ui", "{{lang|la|$1}}", $t); // {{lang}}
		$t = preg_replace("~\b([A-Z]\. +)(\{\{lang\|la\|)~u", "$2$1", $t); // {{lang}}

	// оптимизация '' ''
	$t = preg_replace(" +('''?'?'?)(или|и)('''?'?'?) +", "$1 $2 $3", $t);
	$t = preg_replace("~([\w.,])''([,.])? +''(\w)~u", "$1$2 $3", $t);		// (\w)''[,.]? ''(\w)
	$t = preg_replace("~([\w.,])'''([,.])? +'''(\w)~u", "$1$2 $3", $t);		// (\w)'''[,.]? '''(\w)
	$t = preg_replace("~([\w.,])'''''([,.])? +''(\w)~u", "$1$2''' $3", $t);		// '''''[,.]? ''
	$t = preg_replace("~([\w.,])''([,.])? +'''''(\w)~u", "$1$2 '''$3", $t);		// ''[,.]? '''''
	$t = preg_replace("~'''''([,.])? +'''''~u", "$1 ", $t);		// '''''[,.]? '''''
	$t = str_replace("'',''' ", ",''''' ", $t);
	$t = preg_replace("~\.''' ''(\w)~u", ". '''''$1", $t);

	// оптимизация <small>
	$t = preg_replace("~</small>('*)<small>~ui", "$1", $t);				// <small>'*<small>
	$t = preg_replace("~</small>'' ''<small>~ui", " ", $t);				// </small>'' ''<small>
	$t = preg_replace("~</small> <small>~ui", " ", $t);					// </small> <small>
	$t = preg_replace("~</small>(''|,) +<small>~ui", "$1 ", $t);        // </small>'' <small>
	$t = preg_replace("~</small> ''<small>~ui", " ''", $t);				// </small> ''<small>
	$t = preg_replace("~</small> +(или|и) +<small>~ui", " $1 ", $t);    // </small> (или|и) <small>
	$t = preg_replace("~</small>'' +(или|и) +<small>~ui", "'' $1 ", $t);// </small>'' (или|и) <small>
	$t = preg_replace("~</small> +(или|и) +''<small>~ui", " $1 ''", $t);// </small> (или|и) ''<small>

	// перенос пунктуации внутрь выделения жирным текстом
	$t = preg_replace("~((?:'')?''')((?:[][()\w ́ˊ,—-]|\{\{акут\}\})+)('''(?:'')?)([,.;!])~ui", "$1$2$4$3", $t);    // '''слово'''[,.;!] → '''слово,'''
	$t = preg_replace("~((?:\w|\{\{акут\}\})+)(''''')([,.;!])~ui", "$1$3$2", $t);    // слово'''''[,.;!]
	return $t;
}