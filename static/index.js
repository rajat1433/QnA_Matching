(function() {
	var PNUM = 16
  var question_id = 0;
  var context_questions;// Context in the form field.
	var context_title;// Titles in the drop down Menu.
	window.onload = function(){
		load()
	}

	function clearField(){
		var qadiv = document.getElementById("qa");
		qadiv.innerHTML = "";
		displayQuestion();
	}

	function load(){
		sendAjax("/select", {}, handleQuestion);
	}
	function loadDropdown(){
		var dropdown = document.getElementById("selectQuest");
		for(var i=0; i<PNUM; i++){
			var opt = document.createElement("option");
			opt.value = parseInt(i);
			opt.innerHTML = context_title[i];// titles come here
			dropdown.appendChild(opt);
		}
		question_id = 0;
		_loadQuestion();
		dropdown.onchange = loadQuestion;
	}

	function displayQuestion(){
		var form= document.createElement("div");
		form.id = "current";

		// button to submit
		var button = document.createElement("button");
		button.type = "button";
		button.classList.add("btn");
		button.classList.add("btn-sm");
		button.classList.add("btn-default");
		button.innerHTML="submit";
		button.id = "submit";
		// button to clear
		var clear = document.createElement("button");
		clear.type = "button";
		clear.classList.add("btn");
		clear.classList.add("btn-sm");
		clear.classList.add("btn-default");
		clear.innerHTML="clear";
		clear.id = "clear";
		// loading
		var loading = document.createElement("div");
		loading.id = "loading";
		loading.style.display = "none";
		var img = document.createElement("img");
		img.src = "../static/styles/images/loading_img.gif";
		img.alt = "icon";
		loading.appendChild(img);
		loading.innerHTML = loading.innerHTML + "loading";
		// appendChild

		form.appendChild(button);
		form.appendChild(clear);
		form.appendChild(loading);
		var qadiv = document.getElementById("qa");
		qadiv.append(form);
		button.onclick = loadAnswer;
		clear.onclick = clearField;
	}

	function displayAnswer(answer){
	  var div = document.createElement("div");
		var label = document.createElement("h4");
		var span = document.createElement("span");
		span.classList.add("label");
		span.classList.add("label-primary");
		span.innerHTML="Answer";
		var input = document.createElement("textarea");
		input.style = "resize:none";
		input.readOnly = true;
		input.classList.add("form-control");
		input.innerHTML = answer;
		input.rows = 15;
		div.appendChild(label);
		label.appendChild(span);
		div.appendChild(input);

		var qadiv = document.getElementById("qa");
		qadiv.append(div);
    }

    function loadAnswer(){
		document.getElementById("loading").style.display = "block";
		var data = {
			qid : $("#qid").val(),
		};
		sendAjax("/submit", data, handleAnswer);
	}

    function handleAnswer(answer){
		var curr = document.getElementById("current");
		curr.removeChild(document.getElementById("submit"));
		curr.removeChild(document.getElementById("clear"));
		curr.removeChild(document.getElementById("loading"));
		displayAnswer(answer);

		var clear = document.createElement("button");
		clear.type = "button";
		clear.classList.add("btn");
		clear.classList.add("btn-sm");
		clear.classList.add("btn-default");
		clear.innerHTML="Ask New Question";
		clear.id = "clear";
		clear.onclick = clearField;
		curr.appendChild(clear);	
	}

	function loadQuestion(){
		question_id = this.value;
		_loadQuestion();
	}

	function _loadQuestion(){
		clearField();
		document.getElementById("qid").value = context_questions[question_id];
	}

	function handleQuestion(data){
		context_title = data.context_title;
		context_questions = data.context_questions;
		loadDropdown();
	}

  function sendAjax(url, data, handle){
		$.getJSON(url, data, function(response){
			handle(response.result);
		});
	}

})();
