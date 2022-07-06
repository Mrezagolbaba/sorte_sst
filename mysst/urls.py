from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('education/', include('education.urls')),
    path('store/', include('store.urls')),
    path('memberships/', include('membership.urls')),
]
