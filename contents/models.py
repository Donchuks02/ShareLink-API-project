from django.db import models
from django.conf import settings

# Create your models here.

class Content(models.Model):
  body = models.TextField()
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return self.body

