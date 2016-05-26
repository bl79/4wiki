



<script>
var object = {
	x : 100,
	y : 20,
	string : 'hello',
	g : {
		a: 50,
		b: 'string',
	}
};

/*

	var object2 = Object.create(object);

	object2.title = 'new title';
	object2.description = 'text';
	object2.x = 'var x';

	for (var var_name in object2) {
		document.write(var_name + ' => ' + object2[var_name] + '<br>');
	}

	document.write(object.x);
*/

	var object = {
		x : 100,
		y : 20,

		get test(){
			return this.x + this.y;
		},

		set test(b) {
			this.x = b;
			return this.x + this.y;
		},

		my_method : function () {
			alert(this.x + 'test' + this.y);
		}
	}

//object.my_method();


//	object.test = 1000;
//	document.write(object.test);

/*	for (var i = 1; i<4; i++){
		document.write(object['x' +i]);
	}*/

//function User (name, famiy) {
//	this.name = name;
//	this.family = famiy;
//}
//var Vasya = new User("Вася", "Иванов");
//var Sergey = new User("Сергей", "Сидоров");
//document.write(Sergey.name + " " + Sergey.family);
//document.write(Vasya.name + " " + Vasya.family);

//	jj = window.confirm('uu');
//

function Car (data) {

	function getparam(data){
		s = data.split('|');
		this.color = s[0];
		this.type = s[1];
	}
	function showcar () {
		document.write('цвет: ' + this.color + '\nтип кузова: ' + this.type + '\n');
	}

	getparam(data);
	showcar();
}
//	var data = ;
	var Vasya = new Car(window.prompt("цвет|тип кузова"));







</script>