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

class Language(models.Model):
	languageText = models.CharField(max_length=20, default='')
	def __str__(self):	return str(self.languageText)

class Country(models.Model):
	countryText = models.CharField(max_length=30, default='')
	def __str__(self):	return str(self.countryText)

class Other(models.Model):
	otherText = models.CharField(max_length=30, default='')
	def __str__(self):	return str(self.otherText)


class User(models.Model):
	userNum = models.IntegerField(unique=True)
	userVotes = models.ManyToManyField(Votable, through='Vote')

	userAge = models.IntegerField(default=0)
	userGender = models.CharField(max_length=3, default='')
	userEducation = models.CharField(max_length=3, default='')
	userIncome = models.CharField(max_length=3, default='')

	userLanguage = models.ManyToManyField(Language)
	userCountry = models.ManyToManyField(Country)
	userOther = models.ManyToManyField(Other)
	

class Question(Votable):
	questionUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Category(Votable):
	categoryQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
	class Meta:
		ordering = ['text']

class Comment(Votable):
	commentQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
	commentCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
	commentUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	#automatically vote

class Vote(models.Model):
	votable = models.ForeignKey(Votable, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	vote = models.IntegerField(default=0)
	def __str__(self):
		return str(self.votable)

