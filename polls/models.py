import datetime

from django.utils import timezone
from django.db import models

class Votable(models.Model):
	text = models.CharField(max_length=200, default='')
	def upvotes(self):
		return self.vote_set.filter(vote=1).count()
	def downvotes(self):
		return self.vote_set.filter(vote=-1).count()
	def __str__(self):
		return self.text

class User(models.Model):
	host = models.CharField(max_length=40, primary_key=True)
	ethnicity = models.CharField(max_length=200, default='')
	userVotes = models.ManyToManyField(Votable, through='Vote')
	def __str__(self):
		return str(self.host)

class Question(Votable):
	questionUser = models.ForeignKey(User, on_delete=models.CASCADE)
	

class Category(Votable):
	categoryQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
	class Meta:
		ordering = ['text']

class Comment(Votable):
	commentQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
	commentCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
	commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
	#automatically vote

class Vote(models.Model):
	votable = models.ForeignKey(Votable, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	VOTES = (
		( 1, 'upVote'),
		( 0, 'noVote'),
		(-1, 'downVote'),
	)
	vote = models.IntegerField(choices=VOTES, default=0)
	def __str__(self):
		return str(self.votable)