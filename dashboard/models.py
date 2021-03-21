from django.db import models
from django.contrib.auth.models import User




class Notice(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title





class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image=models.ImageField(upload_to='image/profile', default='image/Default.png' ,null=True, blank=True,verbose_name = "تصویر")
  signature=models.ImageField(upload_to='image/signature',null=True, blank=True)

  def __str__(self):
    return "User : " + str(self.user)
