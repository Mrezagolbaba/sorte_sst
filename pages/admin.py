from django.contrib import admin
from .models import NewsletterModel

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')

admin.site.register(NewsletterModel, NewsletterAdmin)
