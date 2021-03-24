from .models import Profile, Notice, Payment, Submitted_files
from django.contrib import admin

from django.contrib.admin.models import LogEntry
admin.site.register(LogEntry)


admin.site.site_header= "  پنل مدیریت BOM "
admin.site.site_title= "Tavankar"



admin.site.register(Notice)
admin.site.register(Submitted_files)
admin.site.register(Payment)
admin.site.register(Profile)
