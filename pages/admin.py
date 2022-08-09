from django.contrib import admin
from .models import NewsletterModel, ContactModel


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'number', 'email')
    # list_editable = ('is_published',)
    list_filter = ('date',)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')

admin.site.register(NewsletterModel, NewsletterAdmin)
admin.site.register(ContactModel, ContactModelAdmin)