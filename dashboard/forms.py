from django import forms
from django.contrib.auth.models import User
from .models import Profile, Payment
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm





#------------------------------------------------------------------------------
class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payment
		fields = ['descriptions', 'photo']



#------------------------------------------------------------------------------
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
        'father_name',
        'identity_number',
        'national_code',
		'phone',
        'address',
        'bank_name',
        'account_holder',
        'cardـnumber',
        'user_photo',
        'signature',
        'personalـphoto']



#------------------------------------------------------------------------------
class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']







#------------------------------- Forms End -----------------------------------
