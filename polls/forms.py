from django import forms
from polls.models import *
	
INCOMES = (
    ("-", "Select Income"),
    ("LOW", "< 30,000"),
    ("MID", "< 80,000"),
    ("HIG", "> 80,000"),
    )

GENDERS = (
    ("-", "Select Gender"),
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
    )

EDUCATIONS = (
    ("-", "Select Education"),
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
	    widget=forms.SelectMultiple(attrs={'placeholder': 'Language(s)'}),
    	)
    userCountry = forms.ModelMultipleChoiceField(
    	required=False,
    	queryset=Country.objects.all(),
	    widget=forms.SelectMultiple(attrs={'placeholder': 'Country(s)'}),
    	)
    userOther = forms.ModelMultipleChoiceField(
    	required=False,
    	queryset=Other.objects.all(),
	    widget=forms.SelectMultiple(attrs={'placeholder': 'Ethnicity, Faith, Disability, etc'}),
    	)

    #Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
     #                                    choices=OPTIONS)


    def clean_user_language(self):
        cleaned = self.cleaned_data['user_language']
        
        # Error: some individual values weren't valid...
        raise forms.ValidationError('some message')

    class Meta:
        model = Profile
        fields = ('userNum', 'userAge', 'userGender', 'userEducation', 'userIncome', 'userLanguage', 'userCountry', 'userOther')
