<?php
// 1. извлекает списки из словников.xml с шаблонами tsds. словники дожны быть одного тома.
// 2. извлекает статьи перечисленные в словниках из все-статьи-тсд.xml - скачанная категория "ТСД:Статьи из 2-го издания‎"
// 3. помещает их в БД mysql. там надо отсортировать статьи и провериить те у которых значения =null
// 4. затеи вторым скриптом db2indexpage.php делается csv для заливки
require 'tsd-vars.php';
$table = array();

$xml = simplexml_load_file($fwordlist);
foreach ($xml->page as $page) {
	//$title = $page->title;
	$t  = $page->revision->text;
	preg_match_all("~tsds\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*(?:\|\s*(.*?)\s*)?[|}]~u", $t, $found, PREG_SET_ORDER);
	foreach ($found as $a) {
		if ($a[2] == '') $a[2] = $a[1];
		if ($a[3] == '') $a[3] = $a[1];
		if (!$a[3]) $a[3] = '';
		if (!$a[4]) $a[4] = '';
			else preg_match("~^(\d+)~u", $a[4], $pag);
		$table[$a[1]] = array(
			'pagename' => $a[1],
			'nazvanie_do' => $a[2],
			'nazvanie_so' => $a[3],
			'pnum' => $pag[1],
			'snum' => $pag[1] + $offset,
		);
		unset($pag);unset($a);
	}
}
unset($xml);unset($page);unset($found);
echo 'wordlist - ok\n';


$xml = simplexml_load_file($fallpages);
foreach ($xml->page as $page) {
	$pagename = str_replace('ТСД/', '', $page->title);
	if (!$pagename or !array_key_exists($pagename, $table)) continue;
	$t = $page->revision->text;
	//$t = preg_replace("/\n/u", "##BR##", $t);
	for ($i=1; $i<=4; $i++) {$t = preg_replace("~(<div[^>']+)'[^>]*>~u", '$1"', $t);} unset($i);
	if (!preg_match('~\{\{tom\| *2 *\| *\d *\}\}[\s\Wa-zA-Z]*(?:<!--)?\s*section begin="(.*?)" */>\s*(?:-->)?\s*(.*?)\s*(?:<!--)?\s*<section end="\1"~us', $t, $found)) {
		if(strpos($t, '#перенаправление')) $table[$pagename]['is_redirect'] = 1;
			else $table[$pagename]['is_redirect'] = 2;
		continue;
		}
	if (!$found[2] or $found[2]==null) { $found[2] = ''; $found[1] = $pagename.'-1'; }
	//elseif ($table[$pagename]) {
	$table[$pagename]['sectionname_so'] = $found[1];
	//'sectionname_do' => $found[1],
	$table[$pagename]['section_so'] = toSO($found[2]);
	$table[$pagename]['section_do'] = toDO($table[$pagename]['section_so']);
	if (preg_match("/^(.*?[^ ])\-?1$/u", $table[$pagename]['sectionname_so'], $found))
		$table[$pagename]['sectionname_do'] = $found[1];
	//}
}
unset($xml);unset($page);unset($pages);
echo 'text file - ok\n';


$mysqli = new mysqli('localhost','root','','test') OR DIE("Не могу создать соединение ");

$mysql_init = "SET NAMES 'utf8'; SET CHARACTER SET 'utf8'; SET SESSION collation_connection = 'utf8_general_ci'; SET TIME_ZONE = '+03:00'";
$mysqli->query($mysql_init);

foreach ($table as $p => $a) {
	$keys = array();$values = array();;
	foreach ($a as $k => $v) {
		$keys[] = $k;
		$values[] = '"'.addslashes($v).'"';
		}
	$q="INSERT IGNORE INTO ".$dbtable." (".implode(",",$keys).") VALUES (".implode(",",$values).");";
	$result = $mysqli->query($q) or die($mysqli->error);
	//unset($values);
}
echo 'db wrote - ok\n';

/*
//INSERT IGNORE INTO tsd2_pages pnum, t_so, t_do
//"SELECT pnum, sectionname_do, section_do, sectionname_so, section_so FROM tsd2 WHERE pnum = $pnum ORDER BY id")) {

$pages = array();
$t_so = ''; $t_do = ''; $page = '';
$pnum = 1;
while ($p = $mysqli->query("select * from tsd2 where pnum = $pnum ORDER BY id")) {
	$t_so = ''; $t_do = '';
	while ($row = $p->fetch_assoc()) {
		$t_so = $t_so.
				'<section begin="'.$row['sectionname_do'].'" />'.
				$row['section_do'].
				'<section end="'.$row['sectionname_do'].'" />\n\n';
		$t_do = $t_do.
				'<section begin="'.$row['sectionname_so'].'" />'.
				$row['section_so'].
				'<section end="'.$row['sectionname_so'].'" />\n\n';
	}
	$snum = $row['snum']
	if(fmod($pnum,2)==0) $page = '{{колонтитул|'.$snum.'||}}';	else $page = $page.'{{колонтитул|||'.$snum.'}}';
	$pages[$pnum] = $page.$t_so.'\n\n{{свр}}\n\n'.$t_do;
	$pnum++;
}
echo 'db read - ok<br />';*/
$mysqli->close() or die($mysqli->error);
echo 'db close - ok\n';


/*
$pages = array();
$t_so = ''; $t_do = ''; $page = '';
//$pnum = 1;
for ($pnum = 1;;$pnum++ ) {
	foreach ($table as $a) {
		if ($a['pnum'] == $pnum) {
			$pages['pnum']['t_so'] = $pages['pnum']['t_so'] . '<section begin="' . $a['sectionname_do'] . '" />' . $a['section_do'] . '<section end="' . $a['sectionname_do'] . '" />\n\n';
			$pages['pnum']['t_do'] = $pages['pnum']['t_do'] . '<section begin="' . $a['sectionname_so'] . '" />' . $a['section_so'] . '<section end="' . $a['sectionname_so'] . '" />\n\n';
		}
	}
}
foreach ($pages as $pnum => $pt) {
	if (fmod($pnum, 2) == 0) $page = '{{колонтитул|'.$pnum.'||}}'; else $page = '{{колонтитул|||'.$pnum.'}}';
	$pages = $page. $pt[$pnum]['t_do'] . '\n\n{{свр}}\n\n' . $pt[$pnum]['t_so'];
}
*/



function toSO($t) {
	$t = oformlenie($t);
	//$t = str_replace('{{акут}}','́', $t);	$t = str_replace('{{акут3}}','ˊ', $t);
	$t = preg_replace("~\n+ *(\{\{tsdbr)~u", "$1", $t);

	$t = str_replace("на ть и на ся", "на ''ть'' и на ''ся''", $t);
	return $t;
}

//fsave_csv($fout, $list, '~')
