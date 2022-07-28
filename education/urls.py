from django.urls import path
from .views import *


urlpatterns = [
    path('introduction', introduction, name='introduction'),
    path('forexfoundamentals', forexfoundamentals, name='forexfoundamentals'),
    path('sniper_education', sniper_education, name='sniper_education'),
    path('Characteristicsofcandlesticks', Characteristicsofcandlesticks, name='Characteristicsofcandlesticks'),
    path('sr', sr, name='sr'),
    path('technical_indicators', technical_indicators, name='technical_indicators'),
    path('sniper_strategies', sniper_strategies, name='sniper_strategies'),
    path('all_courses_ch1', all_courses_ch1, name='all_courses_ch1'),
    path('all_courses_ch2', all_courses_ch2, name='all_courses_ch2'),
    path('all_courses_ch3', all_courses_ch3, name='all_courses_ch3'),
    path('all_courses_ch4', all_courses_ch4, name='all_courses_ch4'),
    path('all_courses_ch5', all_courses_ch5, name='all_courses_ch5'),
    path('all_courses_ch6', all_courses_ch6, name='all_courses_ch6'),
    path('lesson_detail/<int:lesson_id>', lesson_detail, name='lesson_detail'),
    path('quiz-detail/<int:quiz_id>', quiz_detail,name='quiz-detail'),
    path('quiz-detail/check-quiz', check_quiz, name='check-quiz'),

]


