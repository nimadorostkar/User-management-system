from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'bank_name', 'cardـnumber', 'account_holder')
        #The labels attribute is optional. It is used to define the labels of the form fields created
        labels = {
                "address": _("address     "),
                "bank_name": _("bank_name"),
                "cardـnumber": _("cardـnumberrr"),
                "account_holder": _("account holder"),
                }
