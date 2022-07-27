from django.urls import path
from .views import *


urlpatterns = [
    path('introduction', introduction, name='introduction'),
    path('forexfoundamentals', forexfoundamentals, name='forexfoundamentals'),
    path('sniper_education', sniper_education, name='sniper_education'),
    path('Characteristicsofcandlesticks', Characteristicsofcandlesticks, name='Characteristicsofcandlesticks'),
    path('all_courses_ch1', all_courses_ch1, name='all_courses_ch1'),
    path('all_courses_ch2', all_courses_ch2, name='all_courses_ch2'),
    path('all_courses_ch3', all_courses_ch3, name='all_courses_ch3'),
    path('lesson_detail/<int:lesson_id>', lesson_detail, name='lesson_detail'),
    path('quiz-detail/<int:quiz_id>', quiz_detail,name='quiz-detail'),
    path('quiz-detail/check-quiz', check_quiz, name='check-quiz'),

]