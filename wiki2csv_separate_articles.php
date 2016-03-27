<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>
 <?php
 require 'my.php';

 $fin='poverya.txt';    $fout='w-out.csv';
 $main_title = "О поверьях, суевериях и предрассудках русского народа (Даль)";
 $pagename = $main_title."/";
 $header = "{{".$main_title."/header}}";
 $footer = "{{".$main_title."/footer}}";

 $t = file_get_contents($fin);
 $t = preg_replace("/^(==+ *([^\n]+) *==+)/um", "#page#$1", $t);
 $t = preg_replace("/\r?\n/u", "##BR##", $t);
 $pages = explode('#page#', $t);

 foreach($pages as $p){
	 	$result = preg_match("/==+ *(.*?) *==+(.*)/us", $p, $found);
	 	// $found[1] = mb_ucfirst($found[1]); регистр заголовков, все строчными, первую букву прописной
	 	$str[] = [
				$pagename . $found[1],
				//"$header##BR##<center><big>'''$found[1]'''</big></center>$found[2]$footer"
				"$header##BR##== $found[1] ==$found[2]$footer"
		];
	}

fsave_csv($fout, $str)

?>