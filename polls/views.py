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



def detail(request, id):
	user = Profile.objects.get(userNum = id)

	questions = Question.objects.order_by('-text')
	context =  {
		'question_list': questions, 
		'upvote_question': Question.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_question': Question.objects.filter(vote__user = user, vote__vote = -1),
		'upvote_category': Category.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_category': Category.objects.filter(vote__user = user, vote__vote = -1),
		'upvote_comment': Comment.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_comment': Comment.objects.filter(vote__user = user, vote__vote = -1),
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
		'question_list': questions, 
		'upvote_question': Question.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_question': Question.objects.filter(vote__user = user, vote__vote = -1),
		'upvote_category': Category.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_category': Category.objects.filter(vote__user = user, vote__vote = -1),
		'upvote_comment': Comment.objects.filter(vote__user = user, vote__vote = 1),
		'downvote_comment': Comment.objects.filter(vote__user = user, vote__vote = -1),
	}
	return render(request, 'index.html', context)


def comment(request, id):
	try:
		user = Profile.objects.get(userNum = id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	comment = request.POST.get('comment')
	if(len(comment) < 5):
		return

	category_id = request.POST.get('id')
	category = get_object_or_404(Category, pk=category_id)

	c = Comment(text=comment, 
		commentQuestion = category.categoryQuestion,
		commentCategory = category,
		commentUser = user)
	c.save()

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
	Category(categoryQuestion=q, text="Secret").save()
	Category(categoryQuestion=q, text="Unique").save()
	Category(categoryQuestion=q, text="Relevant").save()
	Category(categoryQuestion=q, text="Reproducible").save()

	return detail(request, id)


def vote(request, id):
	try:
		user = Profile.objects.get(userNum = id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')

	votable_id = request.POST.get('id')
	value = request.POST.get('value')
	votable = get_object_or_404(Votable, pk=votable_id)

	v, created = Vote.objects.get_or_create(votable=votable, user=user)
	v.vote = value
	v.save()

	data = {
		'id': v.votable.pk,
		'value': v.vote,
	}
	return JsonResponse(data)


def login(request):

	if request.method == 'GET':
		return render(request, 'login.html')

	# Get User
	# try:
	# 	users_id = request.POST.get('userInt')
	# 	user = User.objects.get(userNum = users_id)
	# # Create User
	# except:
	users_id = random.getrandbits(30)
	#TODO: check that this user does not already exist
	#TODO: don't create user unles form is submitted
	user = Profile.objects.create(userNum = users_id)

	return HttpResponseRedirect('form/'+str(users_id)+'/')

	#TODO: every time refresh, creates a new user and resubmits post

def form(request, id):
	try:
		user = Profile.objects.get(userNum = id)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')
	
	if request.method == 'GET':
		context = {
			'form': ProfileForm(instance=user),
		}
		return render(request, 'form.html', context)

	# Create a form instance and populate it with data from the request (binding):
	form = ProfileForm(request.POST, instance=user)
	if form.is_valid():
		form.save()
	
	# try:
	# 	user = Profile.objects.get(userNum = request.POST.get('userNum'))
	# except ObjectDoesNotExist:
	# 	return HttpResponseRedirect('/')

	#TODO: check fields, save user or update user

	return HttpResponseRedirect('/polls/poll/'+str(id)+'/')
	# maybe dont save user until submit right here
	#return render(request, 'form.html', context)