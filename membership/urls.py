from django.urls import path

from education.views import quiz_detail
from .views import *


urlpatterns = [

    path('all_memberships', all_memberships, name='all_memberships'),
    path('monthly_checkout', monthly_checkout, name='monthly_checkout'),
    path('bronze_checkout', bronze_checkout, name='bronze_checkout'),
    path('silver_checkout', silver_checkout, name='silver_checkout'),
    path('gold_checkout', gold_checkout, name='gold_checkout'),
    path('lifetime_checkout', lifetime_checkout, name='lifetime_checkout'),
    path('signal_checkout', signalonly_checkout, name='signal_checkout'),
    path('tradeideas', trade_idea, name='tradeideas'),
    path('save_selected_package', save_selected_package, name='save_selected_package'),
    path('oneonone_reservation', oneonone_reservation, name='oneonone_reservation'),
    path('reservation-detail/<int:session_id>', oneonone_reservation_detail, name='reservationdetail'),
    path('reserved/<int:session_id>', oneonone_make_reservation, name='reserved'),
    path('expiration_check', ten_days_left_members, name='expiration_check'),
    path('membership_newsletter', membership_newsletter, name='membership_newsletter'),
    ]