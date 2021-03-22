import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Profile, Notice
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

  if request.method == 'POST':
      user_form = UserForm(request.POST, instance=request.user)
      profile_form = ProfileForm(request.POST, instance=request.user.profile)
      if user_form.is_valid() and profile_form.is_valid():
          user_form.save()
          profile_form.save()
          messages.success(request, _('Your profile was successfully updated!'))
          return redirect('settings:dashboard')
      else:
          messages.error(request, _('Please correct the error below.'))
  else:
      user_form = UserForm(instance=request.user)
      profile_form = ProfileForm(instance=request.user.profile)

  context = {
  'profile': profile,
  'notices': notices,
  'user_form': user_form,
  'profile_form': profile_form }
  return render(request, 'dashboard/dashboard.html', context)



    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.UserProfile.user)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            #user.username = user.email
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/account/profile')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)
        user_form = EditProfileForm(instance=request.user)





#-------------------------- end views ------------------------
