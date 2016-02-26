<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title></title></head><body>
<?php
	require 'tsd-vars.php';
	$f ='AWBfile.txt';
	$t = file_get_contents($f);

	//$t = addslashes($t);
	$t = RusInLatinWords($t);
	//$t = stripslashes($t);
	//echo htmlspecialchars($t);

	file_put_contents($f, $t);


function RusInLatinWords($t) {
	$t = preg_replace("~([a-z])у([a-z])~u", "\1y\2", $t;
	$t = preg_replace("~([a-z])У([a-z])~u", "\1Y\2", $t;
	$t = preg_replace("~([a-z])к([a-z])~u", "\1k\2", $t;
	$t = preg_replace("~([a-z])К([a-z])~u", "\1K\2", $t;
	$t = preg_replace("~([a-z])е([a-z])~u", "\1e\2", $t;
	$t = preg_replace("~([a-z])Е([a-z])~u", "\1E\2", $t;
	$t = preg_replace("~([a-z])Н([a-z])~u", "\1H\2", $t;
	$t = preg_replace("~([a-z])г([a-z])~u", "\1r\2", $t;
	$t = preg_replace("~([a-z])х([a-z])~u", "\1x\2", $t;
	$t = preg_replace("~([a-z])Х([a-z])~u", "\1X\2", $t;
	$t = preg_replace("~([a-z])і([a-z])~u", "\1i\2", $t;
	$t = preg_replace("~([a-z])І([a-z])~u", "\1I\2", $t;
	$t = preg_replace("~([a-z])В([a-z])~u", "\1B\2", $t;
	$t = preg_replace("~([a-z])а([a-z])~u", "\1a\2", $t;
	$t = preg_replace("~([a-z])А([a-z])~u", "\1A\2", $t;
	$t = preg_replace("~([a-z])р([a-z])~u", "\1p\2", $t;
	$t = preg_replace("~([a-z])Р([a-z])~u", "\1P\2", $t;
	$t = preg_replace("~([a-z])о([a-z])~u", "\1o\2", $t;
	$t = preg_replace("~([a-z])О([a-z])~u", "\1O\2", $t;
	$t = preg_replace("~([a-z])с([a-z])~u", "\1c\2", $t;
	$t = preg_replace("~([a-z])С([a-z])~u", "\1C\2", $t;
	$t = preg_replace("~([a-z])м([a-z])~u", "\1m\2", $t;
	$t = preg_replace("~([a-z])М([a-z])~u", "\1M\2", $t;
	$t = preg_replace("~([a-z])Т([a-z])~u", "\1T\2", $t;
	$t = preg_replace("~([a-z])ь([a-z])~u", "\1b\2", $t;
	return $t;
}