var slideIndex = 0;
var slidecount = 5;
w_width = screen.width
var allslidecount = 15;
var sliders = document.getElementsByClassName("slider"); 
var width_str = getComputedStyle(document.getElementsByClassName("img_slide")[0]).width;
var width = parseInt(width_str.slice(0, width_str.length-2));
var column = document.getElementsByClassName("column_wraper");
var prevScrollpos = window.pageYOffset;
todate(1);



function chapter_header(n) {
	let a = document.getElementsByClassName("triangle")[0];
	let column = document.getElementsByClassName("chapters_wraper");
	if (n == 0) {
		a.style.left = "32px";
		column[0].style.display = "none";
		column[1].style.display = "flex";
	}
	else{
		a.style.left = "202px";
		column[0].style.display = "flex";
		column[1].style.display = "none";
	}
}