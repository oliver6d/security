from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone
import random

from polls.forms import *
from polls.models import *

def test(request):
	return render(request, 'test.html')

def example(request, id):
	return render(request, 'example.html', {'id':id})


def detail(request, id):
	user = Profile.objects.get(userNum = id)

	questions = Question.objects.order_by('-votes')
	context =  {
		'question_list': questions, 
		'upvote_question': Question.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_question': Question.objects.filter(vote__user = user, vote__vote = -1),
		'upvote_comment': Comment.objects.filter(vote__user = user, vote__vote = 1),
		'my_comment': Comment.objects.filter(commentUser = user),
	}
	html = loader.render_to_string(
		'detail.html',
		context
	)
	output_data = {
		'detail_html': html,
	}
	return JsonResponse(output_data)


def index(request, id):
	try:
		user = Profile.objects.get(userNum = id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	questions = Question.objects.order_by('-text')

	context =  {
		'user_num':id,
		'question_list': questions, 
		'upvote_question': Question.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_question': Question.objects.filter(vote__user = user, vote__vote = -1),
		'upvote_comment': Comment.objects.filter(vote__user = user, vote__vote = 1),
		'my_comment': Comment.objects.filter(commentUser = user),
	}
	return render(request, 'index.html', context)



def comment(request, id):
	try:
		user = Profile.objects.get(userNum = id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	comment = request.POST.get('comment')
	if(len(comment) < 3):
		return

	question_id = request.POST.get('id')
	question = get_object_or_404(Question, pk=question_id)

	c = Comment(text=comment, 
		commentQuestion = question,
		commentUser = user)
	c.save()

	return detail(request, id)

def delete(request, id):
	try:
		user = Profile.objects.get(userNum = id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	comment_id = request.POST.get('comment')
	try:
		c = Comment.objects.get(pk = comment_id)
		c.delete()
	except:
		pass

	return detail(request, id)


def question(request, id):
	try:
		user = Profile.objects.get(userNum = id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	question = request.POST.get('question')
	if(len(question) < 5):
		return

	q = Question(text=question, questionUser = user)
	q.save()

	return detail(request, id)


def vote(request, id):
	try:
		user = Profile.objects.get(userNum = id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	votable_id = request.POST.get('id')
	value = int(request.POST.get('value'))
	votable = get_object_or_404(Votable, pk=votable_id)

	v, created = Vote.objects.get_or_create(votable=votable, user=user)

	if (not created) and (v.vote == value):
		v.vote = 0
	else:
		v.vote = value
	v.save()

	data = {
		'id': votable_id,
		'value': v.vote,
	}
	return JsonResponse(data)


def login(request):

	# load page, return empty form
	if request.method == 'GET':
		context = {
			'form': ProfileForm(),
		}
		return render(request, 'login.html', context)

	# submits load user, return filled form
	else:
		try:
			user_id = request.POST.get('userInt')
			user = Profile.objects.get(userNum = user_id)
			context = {
				'form': ProfileForm(instance=user),
			}
			return render(request, 'logedin.html', context)
		except:
			# This will clear profile info
			context = {
				'form': ProfileForm(),
				'error': "Profile not found",
			}
			return render(request, 'login.html', context)


def form(request):
	form = ProfileForm(request.POST)
	# update existing profile
	try:
		id = form['userNum'].value()
		user = Profile.objects.get(userNum = id)
	# create new profile
	except:
		created = False
		while (not created):
			id = random.getrandbits(20)
			user, created = Profile.objects.get_or_create(userNum = id)

	form = ProfileForm(request.POST, instance=user)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.userNum = id
		instance.save()
	#TODO: check cleaning, add errors

	return HttpResponseRedirect('/polls/example/'+str(id)+'/')