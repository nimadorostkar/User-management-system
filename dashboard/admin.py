from django.contrib import admin
from .models import Profile, Notice, Payment


admin.site.register(Notice)
admin.site.register(Payment)
admin.site.register(Profile)
