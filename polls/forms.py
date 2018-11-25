from django import forms
from polls.models import *
	
INCOMES = (
    ("LOW", "Low"),
    ("MID", "Middle"),
    ("HIG", "High"),
    )

GENDERS = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
    )

EDUCATIONS = (
    ("pri", "Primary"),
    ("sec", "Secondary"),
    ("add", "Post Secondary"),
    ("deg", "4 year degree"),
    )

class ProfileForm(forms.ModelForm):
    userNum = forms.IntegerField(required=True,
    	widget=forms.HiddenInput(),
    	)
    userAge = forms.IntegerField(required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Age', 'class':'cpyElement fstElement'}))
    userGender = forms.CharField(
        max_length=3, required=False,
        widget=forms.Select(choices=GENDERS, attrs={'placeholder': 'Gender'} ),
    )
    userEducation = forms.CharField(
        max_length=3, required=False,
        widget=forms.Select(choices=EDUCATIONS, attrs={'placeholder': 'Education'} ),
    )
    userIncome = forms.CharField(
        max_length=3, required=False,
        widget=forms.Select(choices=INCOMES, attrs={'placeholder': 'Income'} ),
    )

    userLanguage = forms.ModelMultipleChoiceField(
    	required=False,
    	queryset=Language.objects.all(),
	    widget=forms.SelectMultiple(attrs={'placeholder': 'Language'}),
    	)
    userCountry = forms.ModelMultipleChoiceField(
    	required=False,
    	queryset=Country.objects.all(),
	    widget=forms.SelectMultiple(attrs={'placeholder': 'Country'}),
    	)
    userOther = forms.ModelMultipleChoiceField(
    	required=False,
    	queryset=Other.objects.all(),
	    widget=forms.SelectMultiple(attrs={'placeholder': 'Ethnicity, Disability, Religion, etc'}),
    	)

    #Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
     #                                    choices=OPTIONS)


    class Meta:
        model = Profile
        fields = ('userNum', 'userAge', 'userGender', 'userEducation', 'userIncome', 'userLanguage', 'userCountry', 'userOther')
