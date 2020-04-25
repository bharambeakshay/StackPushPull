from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'
		exclude = ['user']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=False,help_text='Optional.')
    last_name = forms.CharField(max_length=30,required=False,help_text='Optional.')
    email = forms.EmailField(max_length=254,required=False,help_text='Optional.')

    class Meta:
        model = User
		# fields = '__all__'
        fields = ('username','first_name','last_name','email','password1','password2')
