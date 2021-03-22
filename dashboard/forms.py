from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm





class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['address', 'father_name', 'bank_name' ]
        #fields = '__all__'


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']
