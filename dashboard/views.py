import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Profile, Notice
from . import models
from django.db import transaction
from .forms import ProfileForm, CreateUserForm





@login_required
def dashboard(request):
  profile = models.Profile.objects.filter(user=request.user)
  notices = models.Notice.objects.filter(user=request.user).order_by('-created_on')
  context = {'profile': profile, 'notices':notices }
  return render(request, 'dashboard/dashboard.html', context)




@login_required
def updateProfile(request, pk):

	profile = Profile.objects.get(id=pk)
	form = ProfileForm(instance=profile)

	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'dashboard/dashboard.html', context)
