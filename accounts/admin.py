from django.contrib import admin
from .models import DiscordModel

class DiscordAdmin(admin.ModelAdmin):
    list_display = ('user', 'discord_id')


admin.site.register(DiscordModel, DiscordAdmin)