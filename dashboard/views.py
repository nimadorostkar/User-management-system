import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Profile



def get_alphavantage_key():
  alphavantage_keys = [
    settings.ALPHAVANTAGE_KEY1,
    settings.ALPHAVANTAGE_KEY2,
    settings.ALPHAVANTAGE_KEY3,
    settings.ALPHAVANTAGE_KEY4,
    settings.ALPHAVANTAGE_KEY5,
    settings.ALPHAVANTAGE_KEY6,
    settings.ALPHAVANTAGE_KEY7,
  ]
  return random.choice(alphavantage_keys)

@login_required
def dashboard(request):
  name = Profile.objects.filter(user=request.user)
  portfolio = Profile.objects.get(user=request.user)
  context = {
    'name': name
  }

  return render(request, 'dashboard/dashboard.html', context)
