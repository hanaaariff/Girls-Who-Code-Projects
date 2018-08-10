var ourLoc;
var view;
var map;

// Step 3: We should initalize our variables!
function init() {
	// Initalize things here
	ourLoc = ol.proj.fromLonLat([-122.036367,32.409302]);

	view = new ol.View({
		center: ourLoc,
		zoom: 6 // Students can play around with the starting zoom.
	});

	map = new ol.Map({
		target: 'map', // The "Target" is our <div> name.
		layers: [
		  new ol.layer.Tile({
		    source: new ol.source.OSM() // Explain: this is a required variable.
		  })
		],
		loadTilesWhileAnimating: true,
		view: view
	});
}

function panHome(){
  view.animate({
    center: ourLoc,
    duration: 2000
  });
}

function makeCountryRequest(){
  var countryName = document.getElementById("country-name").value;

  if (countryName === ""){
    alert("You didn't enter a country name!");
    return;
  }

  var query = "https://restcountries.eu/rest/v2/name/" + countryName + "?fullText=true";

  query = query.replace(/ /g, "%20");

  countryRequest = new XMLHttpRequest();
	// changes the call from synchronous to an asynchronous
  countryRequest.open('GET', query, true);

	countryRequest.onload=processCountryRequest

  countryRequest.send();
}

  // alert("Ready State " + countryRequest.readyState);
  // alert("Status " + countryRequest.status);
  // alert("Response " + countryRequest.responseText);
function processCountryRequest(){
	if (countryRequest.readyState != 4){
		return;
	}
  if (countryRequest.status != 200 || countryRequest.responseText === ""){
    alert("We were unable to find your requested country!");
    return;
  }

  var countryInformation = JSON.parse(countryRequest.responseText);

  var lat = countryInformation[0].latlng[0];
  var lon = countryInformation[0].latlng[1];

  // window.console.log(countryName + ": lon " + lon + "& lat " + lat);

  var location = ol.proj.fromLonLat([lon,lat]);
  view.animate({
    center: location,
    duration: 2000
  })
}

// all the countries Karen and I have visited collectively
function us(){
	var us = ol.proj.fromLonLat([-122.036367,32.409302]);
	view.animate({
    center: us,
    duration: 2000
  });
}

function canada(){
	var canada = ol.proj.fromLonLat([-105.750596,55.585901]);
	view.animate({
    center: canada,
    duration: 2000
  });
}

function england(){
	var england = ol.proj.fromLonLat([-0.734771,52.871685]);
	view.animate({
    center: england,
    duration: 2000
  });
}

function taiwan(){
	var taiwan = ol.proj.fromLonLat([120.930229,23.777978]);
	view.animate({
		center: taiwan,
		duration: 2000
	});
}

function india(){
	var india = ol.proj.fromLonLat([78.476681,22.199166]);
	view.animate({
    center: india,
    duration: 2000
  });
}

function singapore(){
	var singapore = ol.proj.fromLonLat([103.808053,1.351616]);
	view.animate({
    center: singapore,
    duration: 2000
  });
}

function malaysia(){
	var malaysia = ol.proj.fromLonLat([101.992306,3.950791]);
	view.animate({
    center: malaysia,
    duration: 2000
  });
}

// function sleep(milliseconds) {
//   var start = new Date().getTime();
//   for (var i = 0; i < 1e7; i++) {
//     if ((new Date().getTime() - start) > milliseconds){
//       break;
//     }
//   }
// }

function worldTrip(){
	us();
	// sleep(2000);
	canada();
	// sleep(2000);
	england();
	// sleep(2000);
	taiwan();
	// sleep(2000);
	india();
	// sleep(2000);
	singapore();
	// sleep(2000);
	malaysia();
}

window.onload = init;
