<?php
// сохранение из БД в csv для страниц индекса
require 'tsd-vars.php';

$mysqli = new mysqli('localhost','root','','test') OR DIE("Не могу создать соединение ");
$mysqli->query($mysql_init);

//INSERT IGNORE INTO tsd2_pages pnum, t_so, t_do
//"SELECT pnum, sectionname_do, section_do, sectionname_so, section_so FROM tsd2 WHERE pnum = $pnum ORDER BY id")) {
$pages = array();
for ($pnum = $startpage; $pnum <= $maxpages; $pnum++) {
	$p = $mysqli->query("SELECT * FROM $dbtable WHERE sectionname_so IS NOT NULL AND pnum = $pnum ORDER BY id"); // is_redirect=3 AND
	if (!$p) continue;
	$t_so = ''; $t_do = ''; $page = ''; $snum ='';
	while ($row = $p->fetch_assoc()) {
		$t_do = $t_do.'<section begin="'.$row['sectionname_do'].'" />'.$row['section_do'].'<section end="'.$row['sectionname_do'].'" />'.$br.$br;
		$t_so = $t_so.'<section begin="'.$row['sectionname_so'].'" />'.$row['section_so'].'<section end="'.$row['sectionname_so'].'" />'.$br.$br;
		$snum = $row['snum'];
	}
	//if(fmod($pnum,2)==0) $colontitul = '{{колонтитул|'.$pnum.'||}}';	else $colontitul = '{{колонтитул|||'.$pnum.'}}';
	$colontitul = (fmod($pnum,2)==0) ? '{{колонтитул|'.$pnum.'||}}' : '{{колонтитул|||'.$pnum.'}}';
	$t_so = preg_replace("/tsdl\|((?:[-\w\d —?]|\{\{акут\d?\}\})+)\}\}/u", "tsdl|$1||so}}", $t_so);
	$text = $colontitul . $br.$br . $t_do . $br.$br.'{{свр}}'.$br.$br . $t_so;
	$text = preg_replace("/\n/u", $br, $text);
	$pages[$snum] = array ($pname.$snum, $text);
}
echo 'db read - ok<br />';
$mysqli->close();
echo 'db close - ok<br />';

fsave_csv($fout2index, $pages);