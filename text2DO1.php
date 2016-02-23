<?php
// конвертит текст в ДО
require 'tsd-vars.php';

	$t = "    ";

	$t = addslashes($t);
	$t = oformlenie($t);
	$t = stripslashes($t);

	//echo $t;
	echo toDO($t);
}