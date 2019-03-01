$(document).ready(function () {

});
function doSomething(){
	console.log("update graph");
	var graph_type = $("#graph_type").val();
	if(graph_type!="-1"){
		var state1 = $("#state1").val();
		var state2 = $("#state2").val();
		var year = $("#year").val();
		var category = $("#category").val();
		if (state1!="-1"&&state2!="-1") {
			// compare two graphs
			showTwoGraphs();
		} else if (state1!="-1") {
			showOneGraph();
			// get state1 graph
			if (graph_type=="Scatter"&&year!="-1") {
				var url = "graphs/" + state1 + "_" + year + "_" + graph_type + ".html";
				$("#category").val("-1");
				setGraphURL("#graph_window", url);
			} else if(graph_type=="Line") {
				var url = "graphs/" + state1 + "_" + graph_type + "_" + category + ".html";
				$("#year").val("-1");
				setGraphURL("#graph_window", url);
			} else if (graph_type=="Pie"&&year!="-1") {
				var url = "graphs/" + state1 + "_" + year + "_" + graph_type + "_" + category + ".html";
				setGraphURL("#graph_window", url);
			} else {

			}
		} else {
			showOneGraph();
			// get state2 graph
			if (graph_type=="Scatter") {
				var url = "graphs/" + state2 + "_" + year + "_" + graph_type + ".html";
				$("#category").val("-1");
				setGraphURL("#graph_window", url);
			} else if(graph_type=="Line") {
				var url = "graphs/" + state2 + "_" + graph_type + "_" + category + ".html";
				$("#year").val("-1");
				setGraphURL("#graph_window", url);
			} else if (graph_type=="Pie") {
				var url = "graphs/" + state2 + "_" + year + "_" + graph_type + "_" + category + ".html";
				setGraphURL("#graph_window", url);
			} else {

			}
		}
	}
	
}
function setGraphURL(selector, url){
    // document.getElementById('graph_window').src = url;
    $(""+selector).attr("src", url);
}
function showTwoGraphs(){

}
function showOneGraph(){
	
}