import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Profile



@login_required
def dashboard(request):
  notice = Profile.objects.filter(user=request.user)
  context = {'notice': notice }
  return render(request, 'dashboard/dashboard.html', context)
