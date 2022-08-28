from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'when', 'status', )
    list_filter = ('title', 'when', 'status', )


admin.site.register(Event, EventAdmin)