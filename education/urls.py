from django.urls import path
from .views import *


urlpatterns = [
    path('introduction', introduction, name='introduction'),
    path('sniper_education', sniper_education, name='sniper_education'),
    path('all_courses_ch1', all_courses_ch1, name='all_courses_ch1'),
    path('lesson_detail/<int:lesson_id>', lesson_detail, name='lesson_detail'),
    path('quiz-detail/<int:quiz_id>', quiz_detail,name='quiz-detail'),
    path('quiz-detail/check-quiz', check_quiz, name='check-quiz'),

]