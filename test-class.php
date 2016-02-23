<?php
class MyClass {
	public $var1 = 'value 1';
	public $var2 = 'value 2';
	public $var3 = 'value 3';

	protected $protected = 'protected';
	private   $private   = 'private';

}

$class = new MyClass();

foreach($class as $key => $value) {
	print "$key => $value\n";
}