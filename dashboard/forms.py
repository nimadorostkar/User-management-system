from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile




class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['address']
        #fields = '__all__'


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
