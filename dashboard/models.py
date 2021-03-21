from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  text = models.TextField(max_length=600,null=True, blank=True)


  def __str__(self):
    return "User : " + str(self.user)
