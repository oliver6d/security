from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone

from .models import *

# def view(request):
#     question_list = Question.objects.order_by('-text')[:5]
#     context = {'question_list': question_list}
#     return render(request, 'polls/detail.html', context)

def index(request):
	questions = Question.objects.order_by('-text')[:5]

	user_id = request.get_host()
	user,created = User.objects.get_or_create(host=user_id)

	#upvotes = Votable.objects.filter(vote__user = user, vote__vote = 1)
	#downvotes = Votable.objects.filter(vote__user = user, vote__vote = -1)
	data =  {
		'question_list': questions, 
		'upvote_question': Question.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_question': Question.objects.filter(vote__user = user, vote__vote = -1),
		'upvote_category': Category.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_category': Category.objects.filter(vote__user = user, vote__vote = -1),
		'upvote_comment': Comment.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_comment': Comment.objects.filter(vote__user = user, vote__vote = -1),
	}
	return render(request, 'polls/index.html', data)

def detail(request):
	questions = Question.objects.order_by('-text')[:5]
	html = loader.render_to_string(
		'polls/detail.html',
		{'question_list': questions}
	)
	output_data = {
		'detail_html': html,
	}
	return JsonResponse(output_data)



def vote(request):
	user_id = request.get_host()
	votable_id = request.POST.get('id')
	value = request.POST.get('value')

	user,created = User.objects.get_or_create(host=user_id)
	votable = get_object_or_404(Votable, pk=votable_id)

	v, created = Vote.objects.get_or_create(votable=votable, user=user)
	v.vote = value
	v.save()

	data = {
		'id': v.votable.pk,
		'value': v.vote,
	}
	return JsonResponse(data)


def comment(request):
	user_id = request.get_host()
	category_id = request.POST.get('id')
	comment = request.POST.get('comment')

	user, created = User.objects.get_or_create(pk=user_id)
	category = get_object_or_404(Category, pk=category_id)

	c = Comment(text=comment, 
		commentQuestion = category.categoryQuestion,
		commentCategory = category,
		commentUser = user)
	c.save()

	return detail(request)


def question(request):
	user_id = request.get_host()
	question = request.POST.get('question')

	user,created = User.objects.get_or_create(pk=user_id)

	q = Question(text=question, questionUser = user)
	q.save()
	Category(categoryQuestion=q, text="Memorable").save()
	Category(categoryQuestion=q, text="Relevant").save()
	Category(categoryQuestion=q, text="Secret").save()
	Category(categoryQuestion=q, text="Unique").save()

	return detail(request)
