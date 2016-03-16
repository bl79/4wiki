<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title>Наиболее посещаемые страницы</title>
	<style type="text/css">
		A {text-decoration: none;}/* Убирает подчеркивание для ссылок */
		A:hover {text-decoration: underline;} /* Подчеркивание при наведении на ссылку */
	</style>
</head>
<body>
	<form method="post" action="<?=$_SERVER['PHP_SELF']?>"><h2>Наиболее посещаемые страницы</h2>
		сайт: <input type="text" name="site" value="ru.wikisource.org"><br>
		год: <input type="number" name="year" value="2016">
		месяц: <input type="text" name="month" value="03">
		день: <input type="text" name="day" value="01"> (с ведущими нулями)
		<br><input type=submit value="Отправить">
	</form>

<?php
if (isset($_POST["site"], $_POST["year"], $_POST["month"], $_POST["day"])) {
	$site = $_POST["site"];
	$y = $_POST["year"];
	$m = $_POST["month"];
	$d = $_POST["day"];

	$url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/'.$site.'/all-access/'.$y.'/'.$m.'/'.$d;
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_TIMEOUT, 300);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$json = (json_decode(curl_exec($ch)));
	curl_close($ch);

	echo $y.'/'.$m.'/'.$d;
	echo '<table><tr bgcolor="silver"><td>Позиция</td><td>Заголовок</td><td>Просмотров</td></tr>';
	foreach ($json->items[0]->articles as $n) {
		$article = '<a href="https://'.$site.'/wiki/'.$n->article.'" >'. str_replace("_"," ",$n->article) .'</a>';
		echo "<tr><td>$n->rank</td><td>$article</td><td>$n->views</td></tr>";
	}
	echo '</table>';
}
?>

<br /><br />
<p><small>© <a href="https://meta.wikimedia.org/wiki/User:Vladis13">Vladis13</a>, 16.03.2016. Информация с проекта <a href="https://wikimedia.org/api/rest_v1/?doc#!/Pageviews_data/get_metrics_pageviews_top_project_access_year_month_day">Wikimedia REST API</a>.</small></p>
</body>
</html>