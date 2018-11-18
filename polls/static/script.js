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
    var text = document.getElementById("addQuestion").value;

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
        }
      });
	return;	
};


function question(button) {
	var text = document.getElementById("addQuestion").value;

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
