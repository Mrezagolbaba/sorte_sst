from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

auth_user = settings.AUTH_USER_MODEL if getattr(
    settings, "AUTH_USER_MODEL") else User



class NewsletterModel(models.Model):
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)

    def __str__(self) -> str:
        return self.email

class ContactModel(models.Model):
    full_name = models.CharField(max_length=150, default='')
    email = models.EmailField(max_length=255)
    number = models.CharField(max_length=15)
    message = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.full_name
