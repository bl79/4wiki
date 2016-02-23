<?php
header('Content-type: text/plain');

$N = 1000000;

$start = microtime(true);
for($i = 0; $i < $N; $i++) {
	$a = rand(0, 100000);
	if($a % 2 == 1) $p = 'нечетное';
	else $p = 'четное';
}
$stop = microtime(true);
printf("%%: %f\n", $stop-$start);


$start = microtime(true);
for($i = 0; $i < $N; $i++) {
	$a = rand(0, 100000);
	if($a & 1 == 1) $p = 'нечетное';
	else $p = 'четное';
}
$stop = microtime(true);
printf("&: %f\n", $stop-$start);


$start = microtime(true);
for($i = 0; $i < $N; $i++) {
	$a = rand(0, 100000);
	if(gettype($a/2) == 'double') $p = 'нечетное';
	else $p = 'четное';
}
$stop = microtime(true);
printf("f: %f\n", $stop-$start);