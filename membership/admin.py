from django.contrib import admin
from .models import LiveSession, Packages, SelectedPackage, Reservation, Tradeidea


class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'saving', 'tax')

class SelectedPackageAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'start_date', 'end_date')
    list_filter = ('title', 'status' , 'start_date', 'end_date')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'reserved_start_date', 'reserved_end_date')


class LiveSessionAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in LiveSession._meta.get_fields()]
      list_display = ['reservation']

class TradeideaAdmin(admin.ModelAdmin):
    list_display = ('pair', 'chart', 'status', 'date_sent')




admin.site.register(LiveSession, LiveSessionAdmin)
admin.site.register(Packages, PackageAdmin)
admin.site.register(SelectedPackage, SelectedPackageAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Tradeidea, TradeideaAdmin)