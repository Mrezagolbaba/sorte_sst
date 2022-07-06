from django.urls import path
from .views import *


urlpatterns = [
    path('store_homepage', store_homepage, name='store_homepage'),
]