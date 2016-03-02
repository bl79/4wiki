<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title>Конвертер современной орфографии в дореформенную</title></head><body><?php

const ABIG = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮѢѴІѲ';    // весь алфавит прописными
//const AKUT = "\{\{[Аа]кут\d?\}\}|[́ˊ]"; // ударения
//const AKUT = "́ˊ"; // ударения
//const WORD = "\b(?:[-\w]|".AKUT.")+\b"; // слово
const WORD = "\b(?:[-\ẃˊ]+)\b"; // слово
const S = 'цкнгшщзхфвпрлджчсмтб';                    // согласные буквы, кроме 'ьъ'
const G = 'ёЁеуыаоэяиюѣѢѵѴіІ';                        // гласные
const A = 'ёйцукенгшщзхъфывапролджэячсмитьбюѣѵіѳ';    // весь алфавит
const PR = '(?:[Пп]ри|[Нн]а|[Пп]ере|[Пп]о|[Пп]од|[Зз]а|[Сс]о?|[Ии]з|[Вв]|[Оо]т)?'; // приставки
//$excl = "(?<!tsd[ls]\|\b.*?)"; // исключать слова в шаблонах. вставить в начало правило замены

require "regexps.php";


$t = "еделяется: если за словом идёт слово ";
$regexps = array (
	'если'	=> 'астен.',
	);

$t = preg_replace_callback("~(?<![[<{|/:])(".WORD.")~u",
	function ($word) {
		$w = $word[1];
		global $regexps;
		//$stopwords = array('lang','small','tsdl','tsds','tsdbr','section','begin','end', 'акут', 'Файл', 'File');
		//if (in_array($w, $stopwords)) return $w;
		foreach ($regexps as $substr => $r)
			$w = preg_replace('~'.$substr.'~u', $r, $w);
		return $w;
	},
	$t);

// foreach ($regexps as $substr => $r)		$t = preg_replace('~'.$substr.'~u', $r, $t);

echo $t;



