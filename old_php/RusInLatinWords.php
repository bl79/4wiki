<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title></head><body>
<?php
	require 'tsd-vars.php';
	$f = 'AWBfile.txt';
	$t = file_get_contents($f);

/*$t = "<section begin=\"Фал\" />'''Фалъ''' <small>м. морск.</small> вообще, снасть для подъема чего: рея и косой парусъ подымаются фаломъ; по-русски: дрокъ и подъемна. Фалъ получаетъ названье по рѣе и парусу: Гротъ-марса-фалъ, форъ-бамъ-фалъ, кливеръ-фалъ <small>ипр.</small>{{tsdbr}}{{tsdbr}}<section end=\"Фал\" />

<section begin=\"Фанаберия\" />'''Фанаберія''' <small>ж.</small> спесь, гордость, надменность. Эта дурацкая фанаберія вѣчно носъ подымаетъ! Фанаберистъ, фанаберистка, гордый родомъ или званьемъ своимъ.{{tsdbr}}{{tsdbr}}<section end=\"Фанаберия\" />";*/



	$t = preg_replace_callback('~(begin=[^>]+>)(.*?)(<section end[^>]+>)~us',
			function($found) {
				$s = $found[2];
				$s = RusInLatinWords($s);
				$s = RusInLatinWords($s);
				$s = RusInLatinWords($s);
				$s = RusInLatinWords($s);
				$s = RusInLatinWords($s);
				$s = RusInLatinWords($s);

				$s = oformlenie($s);
				return $found[1] . $s . $found[3];
			},
			$t);
	file_put_contents($f, $t);
echo $t;

function RusInLatinWords($t) {
	$t = preg_replace("~([a-zA-Z])у([a-zA-Z])~u", "$1y$2", $t);
	$t = preg_replace("~([a-zA-Z])У([a-zA-Z])~u", "$1Y$2", $t);
	$t = preg_replace("~([a-zA-Z])к([a-zA-Z])~u", "$1k$2", $t);
	$t = preg_replace("~([a-zA-Z])К([a-zA-Z])~u", "$1K$2", $t);
	$t = preg_replace("~([a-zA-Z])е([a-zA-Z])~u", "$1e$2", $t);
	$t = preg_replace("~([a-zA-Z])Е([a-zA-Z])~u", "$1E$2", $t);
	$t = preg_replace("~([a-zA-Z])Н([a-zA-Z])~u", "$1H$2", $t);
	$t = preg_replace("~([a-zA-Z])г([a-zA-Z])~u", "$1r$2", $t);
	$t = preg_replace("~([a-zA-Z])х([a-zA-Z])~u", "$1x$2", $t);
	$t = preg_replace("~([a-zA-Z])Х([a-zA-Z])~u", "$1X$2", $t);
	$t = preg_replace("~([a-zA-Z])і([a-zA-Z])~u", "$1i$2", $t);
	$t = preg_replace("~([a-zA-Z])І([a-zA-Z])~u", "$1I$2", $t);
	$t = preg_replace("~([a-zA-Z])В([a-zA-Z])~u", "$1B$2", $t);
	$t = preg_replace("~([a-zA-Z])а([a-zA-Z])~u", "$1a$2", $t);
	$t = preg_replace("~([a-zA-Z])А([a-zA-Z])~u", "$1A$2", $t);
	$t = preg_replace("~([a-zA-Z])р([a-zA-Z])~u", "$1p$2", $t);
	$t = preg_replace("~([a-zA-Z])Р([a-zA-Z])~u", "$1P$2", $t);
	$t = preg_replace("~([a-zA-Z])о([a-zA-Z])~u", "$1o$2", $t);
	$t = preg_replace("~([a-zA-Z])О([a-zA-Z])~u", "$1O$2", $t);
	$t = preg_replace("~([a-zA-Z])с([a-zA-Z])~u", "$1c$2", $t);
	$t = preg_replace("~([a-zA-Z])С([a-zA-Z])~u", "$1C$2", $t);
	$t = preg_replace("~([a-zA-Z])м([a-zA-Z])~u", "$1m$2", $t);
	$t = preg_replace("~([a-zA-Z])М([a-zA-Z])~u", "$1M$2", $t);
	$t = preg_replace("~([a-zA-Z])Т([a-zA-Z])~u", "$1T$2", $t);
	$t = preg_replace("~([a-zA-Z])ь([a-zA-Z])~u", "$1b$2", $t);
	
	$t = preg_replace("~у([a-zA-Z]{2,})~u", "y$1", $t);
	$t = preg_replace("~У([a-zA-Z]{2,})~u", "Y$1", $t);
	$t = preg_replace("~к([a-zA-Z]{2,})~u", "k$1", $t);
	$t = preg_replace("~К([a-zA-Z]{2,})~u", "K$1", $t);
	$t = preg_replace("~е([a-zA-Z]{2,})~u", "e$1", $t);
	$t = preg_replace("~Е([a-zA-Z]{2,})~u", "E$1", $t);
	$t = preg_replace("~Н([a-zA-Z]{2,})~u", "H$1", $t);
	$t = preg_replace("~г([a-zA-Z]{2,})~u", "r$1", $t);
	$t = preg_replace("~х([a-zA-Z]{2,})~u", "x$1", $t);
	$t = preg_replace("~Х([a-zA-Z]{2,})~u", "X$1", $t);
	$t = preg_replace("~і([a-zA-Z]{2,})~u", "i$1", $t);
	$t = preg_replace("~І([a-zA-Z]{2,})~u", "I$1", $t);
	$t = preg_replace("~В([a-zA-Z]{2,})~u", "B$1", $t);
	$t = preg_replace("~а([a-zA-Z]{2,})~u", "a$1", $t);
	$t = preg_replace("~А([a-zA-Z]{2,})~u", "A$1", $t);
	$t = preg_replace("~р([a-zA-Z]{2,})~u", "p$1", $t);
	$t = preg_replace("~Р([a-zA-Z]{2,})~u", "P$1", $t);
	$t = preg_replace("~о([a-zA-Z]{2,})~u", "o$1", $t);
	$t = preg_replace("~О([a-zA-Z]{2,})~u", "O$1", $t);
	$t = preg_replace("~с([a-zA-Z]{2,})~u", "c$1", $t);
	$t = preg_replace("~С([a-zA-Z]{2,})~u", "C$1", $t);
	$t = preg_replace("~м([a-zA-Z]{2,})~u", "m$1", $t);
	$t = preg_replace("~М([a-zA-Z]{2,})~u", "M$1", $t);
	$t = preg_replace("~Т([a-zA-Z]{2,})~u", "T$1", $t);
	$t = preg_replace("~ь([a-zA-Z]{2,})~u", "b$1", $t);

	$t = preg_replace("~([a-zA-Z]{2,})у~u", "$1y", $t);
	$t = preg_replace("~([a-zA-Z]{2,})У~u", "$1Y", $t);
	$t = preg_replace("~([a-zA-Z]{2,})к~u", "$1k", $t);
	$t = preg_replace("~([a-zA-Z]{2,})К~u", "$1K", $t);
	$t = preg_replace("~([a-zA-Z]{2,})е~u", "$1e", $t);
	$t = preg_replace("~([a-zA-Z]{2,})Е~u", "$1E", $t);
	$t = preg_replace("~([a-zA-Z]{2,})Н~u", "$1H", $t);
	$t = preg_replace("~([a-zA-Z]{2,})г~u", "$1r", $t);
	$t = preg_replace("~([a-zA-Z]{2,})х~u", "$1x", $t);
	$t = preg_replace("~([a-zA-Z]{2,})Х~u", "$1X", $t);
	$t = preg_replace("~([a-zA-Z]{2,})і~u", "$1i", $t);
	$t = preg_replace("~([a-zA-Z]{2,})І~u", "$1I", $t);
	$t = preg_replace("~([a-zA-Z]{2,})В~u", "$1B", $t);
	$t = preg_replace("~([a-zA-Z]{2,})а~u", "$1a", $t);
	$t = preg_replace("~([a-zA-Z]{2,})А~u", "$1A", $t);
	$t = preg_replace("~([a-zA-Z]{2,})р~u", "$1p", $t);
	$t = preg_replace("~([a-zA-Z]{2,})Р~u", "$1P", $t);
	$t = preg_replace("~([a-zA-Z]{2,})о~u", "$1o", $t);
	$t = preg_replace("~([a-zA-Z]{2,})О~u", "$1O", $t);
	$t = preg_replace("~([a-zA-Z]{2,})с~u", "$1c", $t);
	$t = preg_replace("~([a-zA-Z]{2,})С~u", "$1C", $t);
	$t = preg_replace("~([a-zA-Z]{2,})м~u", "$1m", $t);
	$t = preg_replace("~([a-zA-Z]{2,})М~u", "$1M", $t);
	$t = preg_replace("~([a-zA-Z]{2,})Т~u", "$1T", $t);
	$t = preg_replace("~([a-zA-Z]{2,})ь~u", "$1b", $t);
	
	$t = preg_replace("~\bУ\. +(\{\{lang\|\w+\|)~u", "$1Y. ", $t);
	$t = preg_replace("~\bК\. +(\{\{lang\|\w+\|)~u", "$1K. ", $t);
	$t = preg_replace("~\bЕ\. +(\{\{lang\|\w+\|)~u", "$1E. ", $t);
	$t = preg_replace("~\bН\. +(\{\{lang\|\w+\|)~u", "$1H. ", $t);
	$t = preg_replace("~\bХ\. +(\{\{lang\|\w+\|)~u", "$1X. ", $t);
	$t = preg_replace("~\bІ\. +(\{\{lang\|\w+\|)~u", "$1I. ", $t);
	$t = preg_replace("~\bВ\. +(\{\{lang\|\w+\|)~u", "$1B. ", $t);
	$t = preg_replace("~\bА\. +(\{\{lang\|\w+\|)~u", "$1A. ", $t);
	$t = preg_replace("~\bР\. +(\{\{lang\|\w+\|)~u", "$1P. ", $t);
	$t = preg_replace("~\bО\. +(\{\{lang\|\w+\|)~u", "$1O. ", $t);
	$t = preg_replace("~\bС\. +(\{\{lang\|\w+\|)~u", "$1C. ", $t);
	$t = preg_replace("~\bМ\. +(\{\{lang\|\w+\|)~u", "$1M. ", $t);

	$t = preg_replace("~([a-zA-Z]{2,})ъ~u", "$1", $t);

	// регулярка оиска по дампу
	//	[a-zA-Z][уУкКеЕНгхХіІВаАрРоОсСмМТь]+[a-zA-Z]|[уУкКеЕНгхХіІВаАрРоОсСмМТь]+[a-zA-Z]{2,}|[a-zA-Z]{2,}[уУкКеЕНгхХіІВаАрРоОсСмМТь]+|\b[УКЕНХІВАРОСМТ]\. +\{\{lang\|\w+\|

	return $t;
}





