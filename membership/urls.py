from django.urls import path
from .views import *


urlpatterns = [

    path('all_memberships', all_memberships, name='all_memberships'),
    path('monthly_checkout', monthly_checkout, name='monthly_checkout'),
    path('bronze_checkout', bronze_checkout, name='bronze_checkout'),
    path('silver_checkout', silver_checkout, name='silver_checkout'),
    path('gold_checkout', gold_checkout, name='gold_checkout'),
    path('lifetime_checkout', lifetime_checkout, name='lifetime_checkout'),
    path('signal_checkout', signalonly_checkout, name='signal_checkout'),
    path('save_selected_package', save_selected_package, name='save_selected_package'),
    ]