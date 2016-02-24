<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title>Конвертер современной орфографии в дореформенную</title>
</head>
<body>
<pre style="white-space:pre-wrap;"><?php
	if (isset($_POST["text"])) { 
		$t = $_POST["text"];


		require 'tsd-vars.php';
		$t = addslashes($t);
		$t = oformlenie($t);
		$t = toDO($t);
		$t = stripslashes($t);
		echo htmlspecialchars($t);


/*
		$s = 'цкнгшщзхфвпрлджчсмтб'; // согласные буквы, кроме 'ьъ'
		$a = 'ёйцукенгшщзхъфывапролджэячсмитьбюѣѵіѳ'; // весь алфавит


		$t = str_replace('{{акут}}','́', $t);	$t = str_replace('{{акут3}}','ˊ', $t);
		$t = preg_replace("/([цкнгшщзхфвпрлджчсмтб])([][ ,?!:;'\"()*<])/u", "$1ъ$2", $t);
		$t = preg_replace("~([цкнгшщзхфвпрлджчсмтб])(\.) *$~u", "$1ъ$2", $t); // в конце текста
			$t = preg_replace("~([цкнгшщзхфвпрлджчсмтб])(\.)( *\{\{tsdbr)~u", "$1ъ$2$3", $t);
		$t = preg_replace("~([цкнгшщзхфвпрлджчсмтбу])е(?![-{])\b~u", "$1ѣ", $t); // ѣ в конце слов
			$t = preg_replace("~\b([нж])ѣ\b~ui", "$1е", $t);
			$t = preg_replace("~\b([Чч]етыр)ѣ\b~u", "$1е", $t);
			$t = preg_replace("~\b([Вв]ообщ)ѣ\b~u", "$1е", $t);
		$t = preg_replace("~([цкнгшщзхфвпрлджчсмтб])(\. +)(?!</small|[ёйцукенгшщзхъфывапролджэячсмитьбюѣѵіѳ])~u", "$1ъ$2", $t);
			$t = preg_replace('~\b(с)([мв])ъ\.~ui','$1$2.', $t);
			$t = preg_replace('~астенъ\.~u','астен.', $t);
			$t = preg_replace("/(г)лагъ./ui", "$1лаг.", $t);
			$t = preg_replace("/\bпадъ./u", "пад.", $t);
			$t = preg_replace("/\bюжъ./u", "юж.", $t);
			$t = preg_replace("/\b(ж|м|ср|мн)ъ\./u", "$1.", $t);
			$t = preg_replace("~\((\w?\w?[цкнгшщзхфвпрлджчсмтб])ъ\)~u", "($1)", $t);
			$t = preg_replace("~ъ([()])~u", "$1", $t);
		$t = preg_replace("~и([оею])~u", "і$1", $t);	// іо   - i перед глассной
		$t = preg_replace("~(\w)е([е])~u", "$1ѣ$2", $t);	// ѣо   - ѣ перед глассной
		$t = preg_replace("/\bсев\b/u", "сѣв", $t);
		$t = preg_replace("/\bнем(ецк)?\b/u", "нѣм$1", $t);
		$t = preg_replace("/\bи пр\b/u", "ипр", $t);
		$t = preg_replace("/\b(в)иде\b/ui", "видѣ", $t);
		$t = preg_replace("/\b(м)ехъ\b/ui", "мѣхъ", $t);
		$t = preg_replace("/\b(б)олее\b/ui", "$1олѣе", $t);
		$t = preg_replace("/\b(м)енее\b/ui", "$1енѣе", $t);
		$t = preg_replace("/\b(е)[ёе]\b/ui", "$1я", $t);
		$t = preg_replace("/\b([кчт])емъ\b/ui", "$1ѣмъ", $t);
			$t = preg_replace("/\b(г)де\b/ui", "$1дѣ", $t);
		//$t = preg_replace("/\b(в)се\b/ui", "$1сѣ", $t);
			$t = preg_replace("/\b(в)сѣ\b/ui", "$1се", $t);
		$t = preg_replace("/(в)се([хм])ъ\b/ui", "$1сѣ$2ъ", $t);
		$t = preg_replace("/\b(д)ве\b/ui", "$1вѣ", $t);
		$t = preg_replace("/\b(д)ейст/ui", "$1ѣйст", $t);
		$t = preg_replace("/(с)вет/ui", "$1вѣт", $t);
		$t = preg_replace("/\b(р)асс/ui", "$1азс", $t);
		$t = preg_replace("/\b(б)есс/ui", "$1езс", $t);
		$t = preg_replace("/\bИордан\b/u", "Іордан", $t);
		$t = preg_replace("/\bИоанн\b/u", "Іоанн", $t);
		$t = preg_replace("/(г)рех/ui", "$1рѣх", $t);
		$t = preg_replace("/\b(н)едел\b/ui", "$1едѣл", $t);
		$t = preg_replace("/\b(н)еделе\b/ui", "$1едѣлѣ", $t);
		$t = preg_replace("/\b(х)леб/ui", "$1лѣб", $t);
		$t = preg_replace("/\b(з)вѣр/ui", "$1вѣр", $t);
		$t = preg_replace("/\b(р)ек[еѣ]/ui", "$1ѣкѣ", $t);
			$t = preg_replace("/\b([Рр])ек(а|ой|у)/u", "$1ѣк$2", $t);
			$t = preg_replace("/\b([Рр])еч(е?н|к|уш)/u", "$1ѣч$2", $t);
		$t = preg_replace("/ристиан/u", "ристіан", $t);
		$t = preg_replace("/(ч)еловек/ui", "$1еловѣк", $t);		
			$t = preg_replace("/(с)осед/ui", "$1осѣд", $t);
			
		// окончания
		$t = preg_replace("/(\w)ий(ся)?\b/u", "$1ій$2", $t);
		$t = preg_replace("/(\w)кие\b/u", "$1кіе", $t);
		$t = preg_replace("/(\w)ни([яю])\b/u", "$1ні$2", $t);
		$t = preg_replace("/(\w)еть(ся)?\b/u", "$1ѣть$2", $t);
		$t = preg_replace("/(\w)евать\b/u", "$1ѣвать", $t);
		$t = preg_replace("/(\w)енный\b/u", "$1ѣнный", $t);
		$t = preg_replace("/(\w)ого\b/u", "$1аго", $t);
			$t = preg_replace("/\b(в)сякаго\b/ui", "$1сякого", $t);
			$t = preg_replace("/\b(э)таго\b/ui", "$1того", $t);
			$t = preg_replace("/\b(к)аго\b/ui", "$1ого", $t);
			$t = preg_replace("/\b(м)наго\b/ui", "$1ного", $t);
			$t = preg_replace("/\b(т)аго\b/ui", "$1ого", $t);
		$t = preg_replace("/стве/u", "ствѣ", $t);
		$t = preg_replace("/ели([аи])\b/u", "ѣли$1", $t);
		$t = preg_replace("/евать\b/u", "ѣвать", $t);
		$t = preg_replace("/(\w)и([ияе])\b/u", "$1і$2", $t);

		$t = preg_replace("/(т)акжѣ/ui", "$1акже", $t);
		$t = preg_replace("/(з)атем/ui", "$1атѣм", $t);
		$t = preg_replace("/(з)де(сь|ш|в)/ui", "$1дѣ$2", $t);
		$t = preg_replace("/(н)ескольк/ui", "$1ѣскольк", $t);
		$t = preg_replace("/(д)иавол/ui", "$1іавол", $t);
		$t = preg_replace("/(з)авет/ui", "$1авѣт", $t);
		$t = preg_replace("/(в)ерн/ui", "$1ѣрн", $t);
		$t = preg_replace("/(в)ет(е?)р/ui", "$1ѣт$2р", $t);
		$t = preg_replace("/(п)овер/ui", "$1овѣр", $t);
		$t = preg_replace("/(в)месте/ui", "$1мѣстѣ", $t);
		$t = preg_replace("/\b(м)есто\b/ui", "$1ѣсто", $t);
		$t = preg_replace("/(м)ест/ui", "$1ѣст", $t);
		$t = preg_replace("/(м)ещ/ui", "$1ѣщ", $t);
		$t = preg_replace("/\b(д)оме\b/ui", "$1омѣ", $t);	
		$t = preg_replace("/(ц)ве([тлс])/ui", "$1вѣ$2", $t);
		$t = preg_replace("/(с)емен/ui", "$1ѣмен", $t);
		$t = preg_replace("/(ж)елез/ui", "$1елѣз", $t);	
		$t = preg_replace("/(д)ел/ui", "$1ѣл", $t);
		$t = preg_replace("/(д)[еѣ]ле/ui", "$1ѣлѣ", $t);
		$t = preg_replace("/(с)евер/ui", "$1ѣвер", $t);
		$t = preg_replace("/(п)римет/ui", "$1римѣт", $t);
		$t = preg_replace("/(?<![Кк]о|х)([Лл])ес/u", "$1ѣс", $t);
		$t = preg_replace("/([Сс])е([яю])/u", "$1ѣ$2", $t);
		$t = preg_replace("/(м)едвед/ui", "$1едвѣд", $t);
		$t = preg_replace("/(р)ез/ui", "$1ѣз", $t);
		$t = preg_replace("/(д)ет(с?к|е)/ui", "$1ѣт$2", $t);
		$t = preg_replace("/(д)ев(к|уш)/ui", "$1ѣв$2", $t);
		$t = preg_replace("/Спасе/u", "Спасѣ", $t);
		$t = preg_replace("/\b(?<!к)(л)ет/ui", "$1ѣт", $t);
		$t = preg_replace("/(с)тен/ui", "$1тѣн", $t);
		$t = preg_replace("/(п)ривет/ui", "$1ривѣт", $t);
		$t = preg_replace("/(с)леп/ui", "$1лѣп", $t);
		$t = preg_replace("/(с)ле([дж])/ui", "$1лѣ$2", $t);
		$t = preg_replace("/(с)пел/ui", "$1пѣл", $t);
		$t = preg_replace("/(б)есед/ui", "$1есѣд", $t);
		$t = preg_replace("/(о)днихъ/ui", "$1днѣхъ", $t);
		$t = preg_replace("/\b([Нн])[еѣ]тъ?\b/u", "$1ѣтъ", $t);
		$t = preg_replace("/\b(в)ек/ui", "$1ѣк", $t);
		$t = preg_replace("/\b(м)ер([аыуе])\b/ui", "$1ѣр$2", $t);
		$t = preg_replace("/(у)бедит/ui", "$1бѣдит", $t);
		$t = preg_replace("/(л)ев(о|ш|ы)/ui", "$1ѣв$2", $t);
		$t = preg_replace("/(с)пев/ui", "$1пѣв", $t);
		$t = preg_replace("/(с)иден/ui", "$1идѣн", $t);
		$t = preg_replace("/(р)еки/ui", "$1ѣки", $t);
		$t = preg_replace("/(р)ечн/ui", "$1ѣчн", $t);
		$t = preg_replace("/(с)ъед/ui", "$1ъѣд", $t);
		//$t = preg_replace("/\bест([ъь])/u", "ѣст$1", $t);	$t = preg_replace("/\bЕст([ъь])/u", "Ѣст$1", $t);
		$t = preg_replace("/\bестъ\b/u", "ѣстъ", $t);	$t = preg_replace("/\bЕстъ\b/u", "Ѣстъ", $t);
		$t = preg_replace("/\bед([уеаояиюъ])/u", "ѣд$1", $t);	$t = preg_replace("/\bЕд([уеаояиюъ])/u", "Ѣд$1", $t);
		$t = preg_replace("/\bешь/u", "ѣшь", $t);	$t = preg_replace("/\bЕшь/u", "Ѣшь", $t);
		$t = preg_replace("/езд/u", "ѣзд", $t);	$t = preg_replace("/Езд/u", "Ѣзд", $t);
		$t = preg_replace("/(м)ена/ui", "$1ѣна", $t);
		$t = preg_replace("/(с)ме([хш])/ui", "$1мѣ$2", $t);
		$t = preg_replace("/(с)не([жг])/ui", "$1нѣ$2", $t);
		$t = preg_replace("/(с)веж/ui", "$1вѣж", $t);
		$t = preg_replace("/(б)лед/ui", "$1лѣд", $t);
		$t = preg_replace("/(?<!колы)(б)ел/ui", "$1ѣл", $t);
		$t = preg_replace("/(г)нев/ui", "$1нѣв", $t);
		$t = preg_replace("/(о)твет/ui", "$1твѣт", $t);		


		echo (htmlspecialchars($t));
		*/
	} 
?></pre>
	<br><br>
	<form method="post" action="<?=$_SERVER['PHP_SELF']?>">Конвертер современной орфографии в дореформенную.<br><br>
		<textarea name="text" rows="15" cols="130"></textarea>
		<br><br> <input type=submit value="Конвертить">
	</form>
Ниже общие правила конвертации.<br>
Также есть словарь исключений, в который, однако, добавляются только самые популярные слова. Ибо данный скрипт никак не претендет на полноту, и тем более не словарь всего на свете. Скрипт даёт результат сразу, для последующей ручной выверки. Если нужен более точный конвертер, воспользуйтесь <a href="http://slavenica.com">slavenica.com</a>.
<ul>
	<li>После согласных ставится «ъ». За исключением ряда слов, которые могут быть <i>сокращениями</i> («и т.д.» и т. п.).</li>
	<li>«И» перед гласными меняется на славянскую «і».</li>
	<li>Окончания «ого» → «аго».</li>
	<li>Окончание «е» после согласных → «ѣ». В списке исключенией присутствуют некоторые слова, имеющие окончание «е» в своей исходной форме именительного падежа. Например, «две» (имен. пад. «два») → «двѣ», но «четыре» (также в имен. пад.) так и кончается на «е».</li>
	<li>В некоторых словах «е» меняется на «ѣ». Но список ограничен, и может быть неточен. Ибо в ДО многие слова могли писаться через обе буквы, многие имеют омонимы, писавшиеся иначе. И формы всех слов имеют сложнуют морфологию (приставки, суффиксы, чередующие согласные и гласные, диалекты), предусмотреть все варианты едва ли возможно даже в сложнейших огромных коммерческих словарях.</li>
</ul>
</body>
</html>