from .models import Profile, Notice, Payment, Submitted_files
from django.contrib.admin.models import LogEntry
from django.contrib import admin
from . import models


admin.site.site_header= " Crop "
admin.site.site_title= " Crop "



class NoticeAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_on')
class Submitted_filesAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_on')
class PaymentAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'image_tag','descriptions','created_on')
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'image_tag','national_code','phone','address')



admin.site.register(models.Notice,NoticeAdmin)
admin.site.register(models.Submitted_files,Submitted_filesAdmin)
admin.site.register(models.Payment,PaymentAdmin)
admin.site.register(models.Profile,ProfileAdmin)

admin.site.register(LogEntry)
