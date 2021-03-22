from django import forms
from django.contrib.auth.models import User
from .models import Profile



class createUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bank_name', 'identity_number', 'address']
#The labels attribute is optional. It is used to define the labels of the form fields created
        labels = {
                "bank_name": _("bank_name Name     "),
                "identity_number": _("identity_number Address"),
                "address": _("Street Address"),
                }
