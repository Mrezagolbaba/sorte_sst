from django.urls import path
from .views import *


urlpatterns = [
    path('introduction', introduction, name='introduction'),
    path('sniper_education', sniper_education, name='sniper_education'),
    path('all_courses', all_courses, name='all_courses'),

]