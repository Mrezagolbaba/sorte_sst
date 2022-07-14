from django.urls import path
from . import views


urlpatterns = [
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('discord', views.discord, name='discord'),
    path('discord_save', views.discord_save, name='discord_save'),
    path('bookings', views.bookings, name='bookings'),
    path('bought_package', views.bought_package, name='bought_package'),
]