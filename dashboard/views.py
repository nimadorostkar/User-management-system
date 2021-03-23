import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Profile, Notice, Payment
from . import models
from django.db import transaction
from .forms import ProfileForm, UserForm
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django import forms





@login_required
@transaction.atomic
def dashboard(request):
  profile = models.Profile.objects.filter(user=request.user)
  notices = models.Notice.objects.filter(user=request.user).order_by('-created_on')
  payment = models.Payment.objects.filter(user=request.user).order_by('-created_on')

  if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            context = {'profile': profile,'notices': notices,'payment': payment,'user_form': user_form,'profile_form': profile_form }
            return render(request, 'dashboard/dashboard.html', context)
        else:
            messages.error(request, _('Please correct the error below.'))
  else:
      user_form = UserForm(instance=request.user)
      profile_form = ProfileForm(instance=request.user.profile)

  context = {
  'profile': profile,
  'notices': notices,
  'payment': payment,
  'user_form': user_form,
  'profile_form': profile_form }
  return render(request, 'dashboard/dashboard.html', context)







"""
    References:
      https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
      https://prog.world/one-to-one-relationship-linking-a-user-model-to-a-custom-profile-model-in-django/
      https://dennis-sourcecode.herokuapp.com/30/
      https://stackoverflow.com/questions/53165222/updating-userprofile-onetoone-model-to-django-user-model
"""



#-------------------------- end views ------------------------
