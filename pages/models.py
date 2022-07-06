from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

auth_user = settings.AUTH_USER_MODEL if getattr(
    settings, "AUTH_USER_MODEL") else User



class NewsletterModel(models.Model):
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)

    def __str__(self) -> str:
        return self.email