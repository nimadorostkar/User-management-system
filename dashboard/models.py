from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver





#------------------------------------------------------------------------------
class Notice(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    class Meta:
        verbose_name = "اعلان"
        verbose_name_plural = " اعلانات "

    def __str__(self):
        return self.title




#------------------------------------------------------------------------------
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_photo=models.ImageField(upload_to='user_uploads/user_photo',default='user_uploads/user_photo/default.png',null=True, blank=True,verbose_name = "تصویر")
  father_name = models.CharField(max_length=50,null=True, blank=True,verbose_name = " نام پدر  ")
  signature=models.ImageField(upload_to='user_uploads/signature',default='user_uploads/signature/default.png',null=True, blank=True,verbose_name = "امضاء")
  personalـphoto=models.ImageField(upload_to='user_uploads/personalـphoto',default='user_uploads/personalـphoto/default.png',null=True, blank=True,verbose_name = "عکس پرسنلی ۳*۴")
  identity_number = models.CharField(max_length=50,unique=True,null=True, blank=True,verbose_name = "شماره شناسنامه")
  national_code = models.CharField(max_length=50,unique=True,null=True, blank=True,verbose_name = " کد ملی ")
  address = models.CharField(max_length=250,null=True, blank=True,verbose_name = " آدرس  ")
  bank_name = models.CharField(max_length=50,null=True, blank=True,verbose_name = " نام بانک")
  cardـnumber = models.CharField(max_length=16,null=True, blank=True,verbose_name = " شماره کارت بانک  ")
  account_holder = models.CharField(max_length=150,null=True, blank=True,verbose_name = " نام صاحب حساب ")

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()


  class Meta:
      verbose_name = "پروفایل"
      verbose_name_plural = " پروفایل ها "

  def __str__(self):
    return "پروفایل : " + str(self.user)








#------------------------------- Models End -----------------------------------
