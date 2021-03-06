/*
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
*/

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
function like(button, id) {
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
            var y = document.getElementById("Yc"+data.id);
            y.innerText="🖤";
            y.className="unselected";
            if(data.value == 1)
                y.innerText = "❤";
                y.className = "selected";

        }
      });
    return; 
};


function addcomment(button, id) {
    var box = document.getElementById("comment"+id);
    var text = box.value;
    if (text.length < 5) return;

    $.ajax({
        type:"POST",
        url: 'comment/',
        data: {
            'comment': text,
            'question_id': id,
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


function deleteComment(button, id) {
    $.ajax({
        type:"POST",
        url: 'delete/',
        data: {
            'comment_id': id,
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
