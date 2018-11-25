function load() {
    $.ajax({
      type: 'posts_html',
      url: '/detail/',
      data: {
        'csrfmiddlewaretoken': window.CSRF_TOKEN // from index.html
      },
	success: function(data) {
        // append html to the posts div
        $('#detail').replaceWith(data.detail_html);
      }
  });
};

function aboutUser(input) {
    var text = document.getElementById("age").value;
    var text = document.getElementById("gender").value;
    var text = document.getElementById("education").value;
    var text = document.getElementById("income").value;
    var text = document.getElementById("language").value;
    var text = document.getElementById("nationality").value;
    var text = document.getElementById("other").value;

    $.ajax({
        type:"POST",
        url: 'question/',
        data: {
            'question': text,
            'csrfmiddlewaretoken': window.CSRF_TOKEN
        },
        dataType: 'json',
        success: function (data) {
            $('#detail').replaceWith(data.detail_html);
        }
      });
    return; 
};

function toggle(button, id) {
	$.ajax({
		type:"POST",
        url: 'vote/',
        data: {
        	'value': button.value,
        	'id': id,
        	'csrfmiddlewaretoken': window.CSRF_TOKEN
        },
        dataType: 'json',
        success: function (data) {
        	var y = document.getElementById("Y"+data.id);
        	y.className="unselected";
        	var n = document.getElementById("N"+data.id);
        	n.className="unselected";
        	if(data.value == -1)
	        	n.className = "selected";
	       	if(data.value == 1)
	        	y.className = "selected";
        }
      });
	return;	
};

function comment(button, id) {
	var text = document.getElementById("comment"+id).value;
    if (text.length < 5) return;

	$.ajax({
		type:"POST",
        url: 'comment/',
        data: {
        	'comment': text,
        	'id': id,
        	'csrfmiddlewaretoken': window.CSRF_TOKEN
        },
        dataType: 'json',
        success: function (data) {
            $('#detail').replaceWith(data.detail_html);
            box.value = "";
        }
      });
	return;	
};


function question(button) {
    var box = document.getElementById("addQuestion");
	var text = box.value;
    if (text.length < 5) return;

	$.ajax({
		type:"POST",
        url: 'question/',
        data: {
        	'question': text,
        	'csrfmiddlewaretoken': window.CSRF_TOKEN
        },
        dataType: 'json',
        success: function (data) {
            $('#detail').replaceWith(data.detail_html);
            box.value = "";
        }
      });
	return;	
};
