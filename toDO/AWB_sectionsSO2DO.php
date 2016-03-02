<?php
// Скрипт для AWB, запускает функцию конвертации СО в ДО. Могут возникать ошибк если ошибочно не закрыты тэги секций.
require '.\tsd-vars.php';
require 'toDO.php';

$f ='AWBfile.txt';
$txt = file_get_contents($f);
//$txt = "";

//$t = addslashes($t);
$txt = oformlenie($txt);
$txt = $page2DO->sectionToDO($txt);
//$t = stripslashes($t);
//echo htmlspecialchars($t);

//echo $txt;
file_put_contents($f, $txt);
//file_put_contents('ttt.txt', $txt);