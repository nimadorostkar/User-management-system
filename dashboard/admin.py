from .models import Profile, Notice, Payment, Submitted_files
from django.contrib import admin
from django.contrib.admin.models import LogEntry


admin.site.site_header= " Crop "
admin.site.site_title= " Crop "



class NoticeAdmin(admin.ModelAdmin):
	list_display = ('name',)
class Submitted_filesAdmin(admin.ModelAdmin):
	list_display = ('name','description')
class PaymentAdmin(admin.ModelAdmin):
	list_display = ('name','image_tag','description')
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('rate','product')


admin.site.register(models.Notice,NoticeAdmin)
admin.site.register(models.Submitted_files,Submitted_filesAdmin)
admin.site.register(models.Payment,PaymentAdmin)
admin.site.register(models.Profile,ProfileAdmin)



admin.site.register(LogEntry)
