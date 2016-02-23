<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title></title>
</head>
<body>
<?php
//	if (isset($_POST["text"])) {
//		$t = $_POST["text"];/
//
		//require 'tsd-vars.php';
		
		$f ='AWBfile.txt';
		$t = file_get_contents($f); 
		
		$t = 'jjjjjjjjjjjjjjjjjjjjjj'  . $t;
		
		//showarray($t);

		file_put_contents($f, $t);
?>