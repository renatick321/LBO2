var sliders = document.getElementsByClassName("slider"); 
var width_str = getComputedStyle(document.getElementsByClassName("img_slide")[0]).width;
var width = parseInt(width_str.slice(0, width_str.length-2));

w_width = screen.width;
var column = document.getElementsByClassName("column_wraper");
var prevScrollpos = window.pageYOffset;

window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementsByClassName("header")[0].style.top = "0";
  } else {
    document.getElementsByClassName("header")[0].style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}

	function next(n) {
		var slides = sliders[n].getElementsByClassName("slide");
		let matrix = getComputedStyle(slides[0]).transform;
		let a = parseInt(matrix.split(/\(|,\s|\)/).slice(1,7)[4]);
		if (a == -(width + 60) * allslidecount) {a = (width + 60) * slidecount}
		a -= (width + 60) * slidecount
		if (a < -(width + 60) * allslidecount) {
			a = -(width + 60) * allslidecount
		}
		for (var i = 0; i < slides.length; i++) {
			slides[i].style.transform = 'translateX(' + a + 'px)';
		}
	}

	function back(n) {
		var slides = sliders[n].getElementsByClassName("slide");
		let matrix = getComputedStyle(slides[0]).transform;
		let a = parseInt(matrix.split(/\(|,\s|\)/).slice(1,7)[4]);
		if (a == 0) {a = -(width + 60) * allslidecount - (width + 60) * slidecount}
		a += (width + 60) * slidecount
		if (a > 0) {
			a = 0
		}
		for (var i = 0; i < slides.length; i++) {
			slides[i].style.transform = 'translateX(' + a + 'px)';
		}
	}