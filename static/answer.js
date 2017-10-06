window.onload = function(){
	var hira = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん".split("");

	var A = "ＴＥＣＨＣＨＡＮＩＳＣＵＴＥ".split("");
	var B = "ＫＯＵＤＡＩＳＡＩＡＰＵＲＩ".split("");
	var C = "てつくちやんはとてもかわいい".split("");
	var D = A.map(function(_, i){
		return hira[(hira.length + hira.indexOf(C[i]) + B[i].charCodeAt(0) - A[i].charCodeAt(0)) % hira.length];
	});

	var data = [
		A.map(c => "<td>○</td>").join(""),
		A.map(c => "<td>↓</td>").join(""),
		B.map(c => "<td>" + c + "</td>").join(""),
		B.map(c => "<td>　</td>").join(""),
		C.map(c => "<td>" + c + "</td>").join(""),
		C.map(c => "<td>↓</td>").join(""),
		D.map(c => "<td>" + c + "</td>").join(""),
	].map(r => "<tr>" + r + "</tr>").join("");

	document.querySelector("table").innerHTML = data;
	document.querySelector("main").style.opacity = 1;
};
