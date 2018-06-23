<?php
// заменяет в статьях текст-секции на <pages index=...>
require 'tsd-vars.php';

$mysqli = new mysqli('localhost','root','','test') OR DIE("Не могу создать соединение ");
$mysqli->query($mysql_init);

$p = $mysqli->query("SELECT * FROM $dbtable WHERE sectionname_so IS NOT NULL ORDER BY id");
while ($row = $p->fetch_assoc()) {
	$pagename = 'ТСД/'.$row['pagename'];
	$pnum = $row['pnum'];
	$snum = $row['snum'];
	$sectionname_so = $row['sectionname_so'];
	$tag = '<pages index="'.$pname4index.'" from='.$snum.' to='.$snum.' onlysection="'.$sectionname_so.'" />';
	$pages[$pagename] = array ($pagename, $snum, $pnum, $tag);
}

echo 'db read - ok<br />';
$mysqli->close();
echo 'db close - ok<br />';

fsave_csv($fout2tagpages, $pages);