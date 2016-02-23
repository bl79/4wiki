<?php
require 'my.php';
require 'vendor/autoload.php';

$fin = 'tsd3-1-pages.xml';
//$fin = '172.xml';
$fout = 'tsd3-wordlist.csv';
$text = file_get_contents($fin);
$pageoffset = 35; // смещение в томах = {17, 2, 2, 4}  35

$xml = simplexml_load_string($text);
foreach ($xml->page as $page) {
    if (preg_match("~/(\d+)$~us", $page->title, $pn)) {
        $sn = (string)$pn[1];
        $t = (string)$page->revision->text;

        preg_match_all('/section begin="(.*?),?".*?section end="\1"/us', $t, $section, PREG_SET_ORDER);
        foreach ($section as $article) {
            if (preg_match("/.*?[^ ]-?1/u", $article[1], $check)) continue;
            if (!preg_match("/\{\{выступ\|[[\d. *]?'''(.*?)[, ?]?'''/u", $article[0], $termin)) continue;
            $termin[1] = preg_replace("/\{\{[Аа]кут\d?\}\}/u", "", $termin[1]);
            $pn = $sn*2-$pageoffset; $pn1 = $pn+1;
            $wordlist[] = array($article[1], $termin[1], $sn, $pn."-".$pn1 );
            //showarray($termin[1]);
            //showarray($article[0]);
        }

        //showarray($wordlist);
        //$list[$pn]['text'] = $t; //showarray($t);
    } else continue;
}
//showarray($wordlist);

// запись файла csv
fsave_csv($fout, $wordlist);
//file_put_contents($fout, implode ('\n\r',$list);
//fsave($fout, implode ("\n",$list));
?>