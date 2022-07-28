from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _


auth_user = settings.AUTH_USER_MODEL if getattr(settings, "AUTH_USER_MODEL") else User

class DiscordModel(models.Model):
    user = models.ForeignKey(auth_user, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(default='amir.cpu@gmail.com')
    discord_id = models.CharField(max_length=100)

    def __str__(self):
        return self.discord_id
