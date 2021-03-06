import datetime

from django.utils import timezone
from django.db import models


class Votable(models.Model):
	text = models.CharField(max_length=200, default='')
	def upvotes(self):
		return self.vote_set.filter(vote=1).count()
	def downvotes(self):
		return self.vote_set.filter(vote=-1).count()
	def votes(self):
		return self.vote_set.count()
	def __str__(self):
		return self.text

class Word(models.Model):
	wordText = models.CharField(max_length=12, unique=True)

class Language(models.Model):
	languageText = models.CharField(max_length=20, default='')
	def __str__(self):	return str(self.languageText)
	class Meta: ordering = ('languageText',)

class Country(models.Model):
	countryText = models.CharField(max_length=30, default='')
	def __str__(self):	return str(self.countryText)
	class Meta: ordering = ('countryText',)

class Other(models.Model):
	otherText = models.CharField(max_length=30, default='')
	def __str__(self):	return str(self.otherText)
	class Meta: ordering = ('otherText',)


class Profile(models.Model):
	userNum = models.IntegerField(unique=True)
	userVotes = models.ManyToManyField(Votable, through='Vote')
	created = models.DateTimeField(null=True)

	userAge = models.IntegerField(default=0, null=True)
	userGender = models.CharField(max_length=3, default='')
	userEducation = models.CharField(max_length=3, default='')
	userIncome = models.CharField(max_length=3, default='')

	userLanguage = models.ManyToManyField(Language)
	userCountry = models.ManyToManyField(Country)
	userOther = models.ManyToManyField(Other)
	

class Question(Votable):
	questionUser = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)

class Comment(Votable):
	commentQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
	commentUser = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
	#automatically vote

class Vote(models.Model):
	votable = models.ForeignKey(Votable, on_delete=models.CASCADE)
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	vote = models.IntegerField(default=0)
	def __str__(self):
		return str(self.votable)

