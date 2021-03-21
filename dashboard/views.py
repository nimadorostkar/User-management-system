import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Profile, Notice



@login_required
def dashboard(request):
  profile = Profile.objects.filter(user=request.user)
  notices = Notice.objects.order_by('-created_on')
  context = {'profile': profile }
  return render(request, 'dashboard/dashboard.html', context)
