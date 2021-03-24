from .models import Profile, Notice, Payment, Submitted_files
from django.contrib import admin



admin.site.register(Notice)
admin.site.register(Submitted_files)
admin.site.register(Payment)
admin.site.register(Profile)
