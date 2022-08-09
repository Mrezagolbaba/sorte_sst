from django.urls import path
from .views import *


urlpatterns = [
    path('store_homepage', store_homepage, name='store_homepage'),
    path('store_newsletter', store_newsletter, name='store_newsletter'),
]