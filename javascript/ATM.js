var images=new Array('../image/header2.jpg','../image/header1.jpg','../image/header3.jpg');
var nextimage=0;
doSlideshow();

$(".About").hide();
$(".Help").hide();
$(".Predict_Div").hide();
$(".Top").hide();
$(".Result").hide();
$(".Error").hide();
$(".Prediction").hide();
$(".Description").hide();
$(".Loading").hide();

function PredictATM(){

	var check=CheckInput();
	if(check){

		var predict_tndt=parseInt(document.getElementById("Predict_TNDT").value);
		var predict_tcdt=parseInt(document.getElementById("Predict_TCDT").value);
		var predict_dsl=document.getElementById("Predict_DSL").value;
		var str=predict_dsl.replace(":"," ");
		var time=str.split(" ");
		var hour=parseInt(time[0]);
		var minute=parseInt(time[1]);
		data='tndt=' + predict_tndt + '&tcdt=' + predict_tcdt + '&hour=' + hour + '&minute=' + minute;
 		Ajax(data);

	}
		
	else{
		
		document.getElementsByClassName("Error")[0].innerHTML="Wrong input data! Please go to the help section for more information about the expected input.";
		$(".Loading").hide();
		$(".Prediction").hide();
		$(".Description").hide();
		$(".Error").show();
		$(".Result").show();
		$('html, body').animate({
       		scrollTop: $(".Error").offset().top
    		}, 500);
		
	}

}

function Ajax(data){
	$(".Prediction").hide();
	$(".Description").hide();
	$(".Error").hide();
	
	$(".Loading").show();
	$(".Result").show();

	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
  		if (xhttp.readyState == 4 && xhttp.status == 200) {
   		 	 Response(xhttp.responseXML);
  		}
	};
	
	xhttp.open("GET", "../cgi-bin/predict.py?" + data , true);
	xhttp.send();
}

function Response(xml){
	xmlDoc = xml	

	x = xmlDoc.getElementsByTagName("message");
	if(x.length!=0){
		txt = x[0].childNodes[0].nodeValue;
		document.getElementsByClassName("Error")[0].innerHTML=txt;
		$(".Loading").hide();
		$(".Prediction").hide();
		$(".Description").hide();
		$(".Error").show();
		$('html, body').animate({
       		scrollTop: $(".Error").offset().top
    		}, 500);
	}
	else{
		x = xmlDoc.getElementsByTagName("date");
		var dates=new Array(x.length);
		var classes=new Array(x.length);;
		y = xmlDoc.getElementsByTagName("class");

		for(i=0;i<x.length;i++){
			dates[i] = x[i].childNodes[0].nodeValue;
			classes[i] = y[i].childNodes[0].nodeValue;
		}
		document.getElementById("Date1").innerHTML=dates[0];
		document.getElementById("Date2").innerHTML=dates[1];
		document.getElementById("Date3").innerHTML=dates[2];
		document.getElementById("Date4").innerHTML=dates[3];
		document.getElementById("Date5").innerHTML=dates[4];
		document.getElementById("Date6").innerHTML=dates[5];
		document.getElementById("Date7").innerHTML=dates[6];
		
		document.getElementById("PN1").innerHTML=classes[0];
		document.getElementById("PN2").innerHTML=classes[1];
		document.getElementById("PN3").innerHTML=classes[2];
		document.getElementById("PN4").innerHTML=classes[3];
		document.getElementById("PN5").innerHTML=classes[4];
		document.getElementById("PN6").innerHTML=classes[5];
		document.getElementById("PN7").innerHTML=classes[6];
		$(".Loading").hide();
		$(".Error").hide();		
		$(".Prediction").show();
		$(".Description").show();
		$('html, body').animate({
       		scrollTop: $(".Prediction").offset().top
    		}, 500);
		
		
	}
	

}

function CheckInput(){

var check=true;
var predict_tndt=document.getElementById("Predict_TNDT").value;
var predict_tcdt=document.getElementById("Predict_TCDT").value;
var predict_dsl=document.getElementById("Predict_DSL").value;


if ( !predict_tndt.match('^[0-9]+$') ) {
	check=false;
	return check;
}
if ( !predict_tcdt.match('^[0-9]+$') ) {
	check=false;
	return check;
	
}
if ( !predict_dsl.match('^[0-9][0-9][:][0-9][0-9]$') ) {
	check=false;
	return check;
}

if(!(parseInt(predict_tndt)>5 && (parseInt(predict_tndt)<2000))){
	check=false;
	return check;
}

if(!(parseInt(predict_tcdt)>1 && (parseInt(predict_tcdt)<3000))){
	check=false;
	return check;
}


var str=predict_dsl.replace(":"," ");
var time=str.split(" ");
var hour=parseInt(time[0]);
var minute=parseInt(time[1]);

if(!(hour>=0 && hour<=5)){

	check=false;
	return check;	

}

if(!(minute>=0 && minute<=59)){

	check=false;
	return check;	

}

	
return check;

}


function About(){
	
	$(".Help").hide();
	$(".Loading").hide();
	$(".Result").hide();
	$(".Error").hide();
	$(".Prediction").hide();
	$(".Predict_Div").hide();
	$(".Description").hide();	
	$(".About").show();
	$(".Top").show();
	$('html, body').animate({
        scrollTop: $(".About").offset().top
    	}, 500);
	
}


function Help(){

	$(".About").hide();
	$(".Predict_Div").hide();
	$(".Loading").hide();
	$(".Result").hide();
	$(".Error").hide();
	$(".Prediction").hide();
	$(".Description").hide();	
	$(".Help").show();
	$(".Top").show();
	$('html, body').animate({
        scrollTop: $(".Help").offset().top
    	}, 500);

}


function Predict(){

	$(".About").hide();
	$(".Loading").hide();
	$(".Help").hide();	
	$(".Result").hide();
	$(".Error").hide();
	$(".Description").hide();
	$(".Prediction").hide();
	$(".Predict_Div").show();
	$(".Top").show();
	$('html, body').animate({
        scrollTop: $(".Predict_Div").offset().top
    	}, 500);
		
}

function Top(){
	
	$('html, body').animate({
        scrollTop: $(".Header").offset().top
    	}, 500);

}

function Redirect(){

	window.open("https://github.com/SaeedNajafi/ATM_Predictor");

}

function doSlideshow(){
    if(nextimage>=images.length){nextimage=0;}
    $('.Image')
    .css('background-image','url("'+images[nextimage++]+'")')
    .fadeIn(15000,function(){
        setTimeout(doSlideshow,15000);
    });
}
