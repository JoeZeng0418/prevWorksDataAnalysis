
$(document).ready(function () {
	appendSeletionList();
});
function appendSeletionList(){
	var states = [
		"All U.S.",
		"Alabama",
		"Alaska",
		"Arizona",
		"Arkansas",
		"California",
		"Connecticut",
		"Delaware",
		"District of Columbia",
		"Georgia",
		"Hawaii",
		"Illinois",
		"Indiana",
		"Iowa",
		"Kansas",
		"Kentucky",
		"Louisiana",
		"Maine",
		"Maryland",
		"Massachusetts",
		"Michigan",
		"Minnesota",
		"Missouri",
		"Montana",
		"Nebraska",
		"Nevada",
		"New Jersey",
		"New Mexico",
		"New York",
		"North Carolina",
		"Ohio",
		"Oregon",
		"Pennsylvania",
		"Puerto Rico",
		"South Carolina",
		"Tennessee",
		"Texas",
		"Utah",
		"Vermont",
		"Virginia",
		"Virgin Islands",
		"Washington",
		"West Virginia",
		"Wisconsin",
		"Wyoming",
		"Guam",
	];
	var years = ["2011","2012","2013","2014","2015","2016","2017"];
	var graph_types = ["Line","Pie"];
	var categories = ["Age", "Event or exposure", "Industry sector", "Musculoskeletal disorders","Nature of injury illness","Number of days away from work","Occupation","Secondary source of injury illness","Sex","Source of injury illness"];
	for (var i = 0; i < states.length; ++i) {
		$("#state1").append($("<option></option>").attr("value",states[i].replace(/\s/g, "_")).text(states[i])); 
		$("#state2").append($("<option></option>").attr("value",states[i].replace(/\s/g, "_")).text(states[i])); 
	}
	for (var i = years.length-1; i >= 0; --i) {
		$("#year").append($("<option></option>").attr("value",years[i]).text(years[i])); 
	}
	for (var i = 0; i < graph_types.length; ++i) {
		$("#graph_type").append($("<option></option>").attr("value",graph_types[i]).text(graph_types[i]+" Chart")); 
	}
	for (var i = 0; i < categories.length; ++i) {
		$("#category").append($("<option></option>").attr("value",categories[i].replace(/\s/g, "_")).text(categories[i])); 
	}
}

function updateGraph(){
	console.log("update graph");
	$("#merge_button button").text("Merge");
	var graph_type = $("#graph_type").val();
	if(graph_type!="-1"){
		var state1 = $("#state1").val();
		var state2 = $("#state2").val();
		var year = $("#year").val();
		var category = $("#category").val();
		if (state1!="-1"&&state2!="-1") {
			// compare two graphs
			// get state1 graph
			console.log("comparing graphs");
			if (graph_type=="Scatter"&&year!="-1") {
				console.log("2 scatter graphs");
				var title = "Scatter plot for " + state1 + " at " + year;
				setGraphTitle("#graph_title1", title);
				var url = "graphs/" + state1 + "_" + year + "_" + graph_type + ".html";
				$("#category").val("-1");
				setGraphURL("#graph_window1", url);
			} else if(graph_type=="Line"&&category!="-1") {
				console.log("2 line graphs");
				var title = "Line plot (rates) for " + state1 + " for years from 2011 to 2017 in "+ category;
				setGraphTitle("#graph_title1", title);
				var url = "graphs/" + state1 + "_" + graph_type + "_" + category + ".html";
				$("#year").val("-1");
				setGraphURL("#graph_window1", url);
			} else if (graph_type=="Pie"&&category!="-1"&&year!="-1") {
				console.log("2 pie graphs");
				var title = "Pie Chart (cases) for " + state1 + " at " + year + " in " + category;
				setGraphTitle("#graph_title1", title);
				var url = "graphs/" + state1 + "_" + year + "_" + graph_type + "_" + category + ".html";
				setGraphURL("#graph_window1", url);
			} else {
				var title = "";
				setGraphTitle("#graph_title1", title);
				setGraphURL("#graph_window1", "graphs/blank.html");
			}
			// get state2 graph
			if (graph_type=="Scatter"&&year!="-1") {
				var title = "Scatter plot for " + state2 + " at " + year;
				setGraphTitle("#graph_title2", title);
				var url = "graphs/" + state2 + "_" + year + "_" + graph_type + ".html";
				$("#category").val("-1");
				setGraphURL("#graph_window2", url);
			} else if(graph_type=="Line"&&category!="-1") {
				var title = "Line plot (rates) for " + state2 + " for years from 2011 to 2017 in " + category;
				setGraphTitle("#graph_title2", title);
				var url = "graphs/" + state2 + "_" + graph_type + "_" + category + ".html";
				$("#year").val("-1");
				setGraphURL("#graph_window2", url);
			} else if (graph_type=="Pie"&&category!="-1"&&year!="-1") {
				var title = "Pie Chart (cases) for " + state2 + " at " + year + " in " + category;
				setGraphTitle("#graph_title2", title);
				var url = "graphs/" + state2 + "_" + year + "_" + graph_type + "_" + category + ".html";
				setGraphURL("#graph_window2", url);
			} else {
				var title = "";
				setGraphTitle("#graph_title2", title);
				setGraphURL("#graph_window2", "graphs/blank.html");
			}
			showTwoGraphs();
		} else if (state1!="-1") {
			showOneGraph();
			// get state1 graph
			if (graph_type=="Scatter"&&year!="-1") {
				var title = "Scatter plot for " + state1 + " at " + year;
				setGraphTitle("#graph_title", title);
				var url = "graphs/" + state1 + "_" + year + "_" + graph_type + ".html";
				$("#category").val("-1");
				setGraphURL("#graph_window", url);
			} else if(graph_type=="Line"&&category!="-1") {
				var title = "Line plot (rates) for " + state1 + " for years from 2011 to 2017 in " + category;
				setGraphTitle("#graph_title", title);
				var url = "graphs/" + state1 + "_" + graph_type + "_" + category + ".html";
				$("#year").val("-1");
				setGraphURL("#graph_window", url);
			} else if (graph_type=="Pie"&&category!="-1"&&year!="-1") {
				var title = "Pie Chart (cases) for " + state1 + " at " + year + " in " + category;
				setGraphTitle("#graph_title", title);
				var url = "graphs/" + state1 + "_" + year + "_" + graph_type + "_" + category + ".html";
				setGraphURL("#graph_window", url);
			} else {
				var title = "";
				setGraphTitle("#graph_title", title);
				setGraphURL("#graph_window", "graphs/blank.html");
			}
		} else if(state2!="-1") {
			showOneGraph();
			// get state2 graph
			if (graph_type=="Scatter"&&year!="-1") {
				var title = "Scatter plot for " + state2 + " at " + year;
				setGraphTitle("#graph_title", title);
				var url = "graphs/" + state2 + "_" + year + "_" + graph_type + ".html";
				$("#category").val("-1");
				setGraphURL("#graph_window", url);
			} else if(graph_type=="Line"&&category!="-1") {
				var title = "Line plot (rates) for " + state2 + " for years from 2011 to 2017 in " + category;
				setGraphTitle("#graph_title", title);
				var url = "graphs/" + state2 + "_" + graph_type + "_" + category + ".html";
				$("#year").val("-1");
				setGraphURL("#graph_window", url);
			} else if (graph_type=="Pie"&&category!="-1"&&year!="-1") {
				var title = "Pie Chart (cases) for " + state2 + " at " + year + " in " + category;
				setGraphTitle("#graph_title", title);
				var url = "graphs/" + state2 + "_" + year + "_" + graph_type + "_" + category + ".html";
				setGraphURL("#graph_window", url);
			} else {
				setGraphURL("#graph_window", "graphs/blank.html");
			}
		} else {

		}
	}
	
}
function setGraphURL(selector, url){
	setTimeout(function (){
	  	console.log("set: "+selector+" to "+url);
    	$(""+selector).attr("src", url);
	}, 500);
}
function showTwoGraphs(){
	console.log("show two graphs");
	$("#window").fadeOut(function() {
		$("#window1").fadeIn();
		$("#window2").fadeIn();
	});
}
function showOneGraph(){
	console.log("show one graphs");
	$("#window1").fadeOut("fast");
	$("#window2").fadeOut("fast", function() {
		$("#window").fadeIn();
	});
}
function setGraphTitle(selector, title){
	$(""+selector).text(title);
}
function mergeGraphs(){
	console.log("merge wo graphs");
	var buttonText = $("#merge_button button").text();
	if (buttonText=="Split") {
		updateGraph();
		$("#merge_button button").text("Merge");
	} else {
		var graph_type = $("#graph_type").val();
		if(graph_type!="-1"){
			var state1 = $("#state1").val();
			var state2 = $("#state2").val();
			var year = $("#year").val();
			var category = $("#category").val();
			if (state1!="-1"&&state2!="-1"&&graph_type=="Line"&&year=="-1"&&category!="-1") {
				var title = "Line plot (rates) to compare " + state1 + " and " + state2 + " for years from 2011 to 2017 in "+ category;
				setGraphTitle("#graph_title", title);
				// call ajax to run python script
				var url = "";
				$.ajax({
			        url: "http://localhost:5000/getGraph?state1="+state1+"&state2="+state2+"&category="+category,
			        type: 'GET',
			        // dataType: 'json', // added data type
			        success: function(res) {
			            console.log(res);
			            var url = res;
			            showOneGraph();
			            $("#merge_button button").text("Split");
						setGraphURL("#graph_window", url);
						
						
			        },
			        error: function(xhr, status, error) {
				  		// var err = eval("(" + xhr.responseText + ")");
				  		console.log(error);
				  		alert(error);
					}
			    });
				
			}
		}
	}
}








