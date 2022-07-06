from django.contrib import admin
from .models import Packages, SelectedPackage

class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'saving', 'tax')

class SelectedPackageAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'start_date', 'end_date')
    list_filter = ('title', 'start_date', 'end_date')


admin.site.register(Packages, PackageAdmin)
admin.site.register(SelectedPackage, SelectedPackageAdmin)