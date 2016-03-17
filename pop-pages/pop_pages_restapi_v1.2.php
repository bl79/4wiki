<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title>Наиболее посещаемые страницы</title>

	<style type="text/css">
		A {text-decoration: none;} /* Убирает подчеркивание для ссылок */
		A:hover {text-decoration: underline;} /* Подчеркивание при наведении на ссылку */
	</style>

	<!-- виджет календарь -->
	<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
	<script src="//code.jquery.com/jquery-1.10.2.js"></script>
	<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
	<script src="datepicker-ru.js"></script>
	<link rel="stylesheet" href="/resources/demos/style.css">
	<script>
		$.datepicker.setDefaults($.datepicker.regional['ru']);
		$(function () {
			$('#datepicker').datepicker($.extend({
				dateFormat: "yy/mm/dd", 			// в datepicker-ru.js dateFormat отключён
				minDate: new Date(2015, 8 - 1, 1),	// до августа 2015 статистики нет
				maxDate: "-1", 						// за сегодня статистики ещё нет
				numberOfMonths: 3,
				changeYear: true,
				changeMonth: true,
				// showOn: "button", buttonImage: "calendar.gif", buttonImageOnly: true, buttonText: "Select date"
			}));
			/* var c = document.querySelector('#PerMonth');
			c.onclick = function() {
				if ('#PerMonth'.checked) {
					alert('чекбокс включён');
				} else {
					alert('чекбокс выключён');
				}
			} */
			$('#datepickerPerMonth').datepicker($.extend({
				dateFormat: "yy/mm/'all-days'", 	// в datepicker-ru.js dateFormat отключён
				minDate: new Date(2015, 8 - 1, 1),	// до августа 2015 статистики нет
				maxDate: "-1m", 					// статистика есть только за закончившиеся месяцы
				numberOfMonths: 3,
				changeYear: true,
				changeMonth: true,
			}));
		});
	</script>
</head>
<body>

	<form method="post" action="<?=$_SERVER['PHP_SELF']?>"><h2>Наиболее посещаемые страницы</h2>
		<p>Top-1000, за период от авг. 2015 до пред. месяца или дня.</p>
		Сайт: <input type="text" name="site" value="ru.wikisource.org">
		За месяц: <input type="text" id="datepickerPerMonth" name="datePerMonth"  placeholder="гггг/мм/all-days">
		или за день: <input type="text" id="datepicker" name="date" placeholder="гггг/мм/дд">
		<!-- <label><input type="checkbox" id="PerMonth" name="PerMonth" checked>PerMonth</label> -->
		<input type=submit value="Отправить">
	</form>

<?php
if (!empty($_POST["datePerMonth"])) $_POST["date"] = $_POST["datePerMonth"];

echo $_POST["date"];
if (!empty($_POST["site"]) and !empty($_POST["date"])) {
	$site = $_POST["site"];
	$date = $_POST["date"];
	$url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/'.$site.'/all-access/'.$date;

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	$json = (json_decode(curl_exec($ch)));
	curl_close($ch);

	if (!$json) echo '<p>Ошибка: Нет ответа сервера.</p>';

	// таблица
	echo '<table><tr bgcolor="silver"><td>Позиция</td><td>Заголовок</td><td>Просмотров</td></tr>';
	foreach ($json->items[0]->articles as $n) {
		$article = '<a href="https://'.$site.'/wiki/'.$n->article.'" >'. str_replace("_"," ",$n->article) .'</a>';
		echo "<tr><td>$n->rank</td><td>$article</td><td>$n->views</td></tr>";
	}
	echo '</table>';
}
?>

<br /><br />
<p><small>© <a href="https://meta.wikimedia.org/wiki/User:Vladis13">Vladis13</a>, 16.03.2016. Информация с проекта <a href="https://wikimedia.org/api/rest_v1/?doc#!/Pageviews_data/get_metrics_pageviews_top_project_access_year_month_day">Wikimedia REST API (beta)</a>.</small></p>
</body>
</html>