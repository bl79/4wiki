<?php // <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>

// вывод на экран форматированный
function showarray($t) {echo '<pre>'.print_r($t,1).'</pre>';}

// В верхний регистр 1-ю букву строки
function mb_ucfirst ($word) {
	return mb_strtoupper(mb_substr($word, 0, 1, 'UTF-8'), 'UTF-8') . mb_substr(mb_convert_case($word, MB_CASE_LOWER, 'UTF-8'), 1, mb_strlen($word), 'UTF-8'); 
}


// запись файла csv
function fsave_csv($fout, $text, $delimiter=',') {
	$fp = fopen($fout,'w'); if ($fp) {
	//fputcsv($fp, $titles);
	foreach ($text as $line) { 
		fputcsv($fp, $line, $delimiter); //explode($fields_separator, $line));
	}
	fclose($fp);}
}

// запись файла
function fsave($fname, $text) {
	$fs=fopen($fname,'wt');
	 if (fwrite($fs, $text) === FALSE) {echo "Не могу произвести запись в файл ($fname)";exit;}
	fclose($fs);
}

// mysql инициация
$mysql_init = "SET NAMES 'utf8'; SET CHARACTER SET 'utf8'; SET SESSION collation_connection = 'utf8_general_ci'; SET TIME_ZONE = '+03:00'";


?>