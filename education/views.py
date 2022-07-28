from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import CourseModel, LessonModel, Quiz
from membership.models import SelectedPackage
from django.contrib import messages
from datetime import date



def sniper_education(request):
    user = request.user
    same_user = []
    check_for_same_user_1 = True
    check_for_same_user_2 = False
    check_for_expired = SelectedPackage.objects.all().filter(user=user, status='Active')
    if check_for_expired:
        today = date.today()
        for member in check_for_expired:
            expire_date = getattr(member, 'end_date').date()
            if today > expire_date:
                same_user.append(member)
                check_for_same_user_1 = False
                member.status = 'Expired'
                member.save()
                messages.info(request, 'Your account has been expired!')
                
                # return  render(request, 'membership/all_memberships.html')
            if today < expire_date:
                check_for_same_user_2 = True
                same_user.append(member)

        if check_for_same_user_1 or check_for_same_user_2:
            return render(request, 'education/sniper_education.html')
        else:
            return render(request,'membership/all_memberships.html')
    else:
         return render(request,'membership/all_memberships.html')



def introduction(request):
    courses = CourseModel.objects.all().filter(chapter=1)
    lessons = LessonModel.objects.all().filter(chapter=1)
    count = LessonModel.objects.all().filter(chapter=1).count()
    context = {
        'courses': courses,
        'lessons' : lessons,
        'count': count,
    }
    return render(request, 'education/introduction.html', context)


def forexfoundamentals(request):
    courses = CourseModel.objects.all().filter(chapter=2)
    lessons = LessonModel.objects.all().filter(chapter=2)
    count = LessonModel.objects.all().filter(chapter=2).count()
    context = {
        'courses': courses,
        'lessons' : lessons,
        'count': count,
    }

    return render(request,'education/forexfoundamentals.html', context)



def Characteristicsofcandlesticks(request):
    courses = CourseModel.objects.all().filter(chapter=3)
    lessons = LessonModel.objects.all().filter(chapter=3)
    count = LessonModel.objects.all().filter(chapter=3).count()
    context = {
    
        'lessons' : lessons,
        'courses': courses,
        'count': count
    }

    return render(request,'education/Characteristicsofcandlesticks.html', context)


def sr(request):
    courses = CourseModel.objects.all().filter(chapter=4)
    lessons = LessonModel.objects.all().filter(chapter=4)
    count = LessonModel.objects.all().filter(chapter=4).count()
    context = {
        'courses': courses,
        'lessons' : lessons,
        'count': count,
    }

    return render(request,'education/sr.html', context)

def technical_indicators(request):
    courses = CourseModel.objects.all().filter(chapter=5)
    lessons = LessonModel.objects.all().filter(chapter=5)
    count = LessonModel.objects.all().filter(chapter=5).count()
    context = {
        'courses': courses,
        'lessons' : lessons,
        'count': count,
    }

    return render(request,'education/technical_indicators.html', context)


def sniper_strategies(request):
    courses = CourseModel.objects.all().filter(chapter=6)
    lessons = LessonModel.objects.all().filter(chapter=6)
    count = LessonModel.objects.all().filter(chapter=6).count()
    context = {
        'courses': courses,
        'lessons' : lessons,
        'count': count,
    }

    return render(request,'education/sniper_strategies.html', context)


def all_courses_ch1(request):
    courses = CourseModel.objects.all().filter(chapter=1)
    lessons = LessonModel.objects.all().filter(chapter=1)
    context = {
        'courses': courses,
        'lessons' : lessons,
    }
    return render(request, 'education/all_courses_chapter1.html', context)


def all_courses_ch2(request):
    quiz_passed_check = Quiz.objects.all().filter(chapter=1)
    check = None
    for quiz in quiz_passed_check:
        check = quiz.passed
    
    if check:
        courses = CourseModel.objects.all().filter(chapter=2)
        lessons = LessonModel.objects.all().filter(chapter=2)
        context = {
            'courses': courses,
            'lessons' : lessons,
        }
        return render(request, 'education/all_courses_chapter2.html', context)
    else:
        messages.info(request, 'You did not passed the quiz of Introduction of Forex.')
        return redirect('sniper_education')

def all_courses_ch3(request):
    quiz_passed_check = Quiz.objects.all().filter(chapter=2)
    check = None
    for quiz in quiz_passed_check:
        check = quiz.passed
    
    if check:
        courses = CourseModel.objects.all().filter(chapter=3)
        lessons = LessonModel.objects.all().filter(chapter=3)
        context = {
            'courses': courses,
            'lessons' : lessons,
        }
        return render(request, 'education/all_courses_chapter3.html', context)

    else:
        messages.info(request, 'You did not passed the quiz of Forex Fundamentals.')
        return redirect('sniper_education')

def all_courses_ch4(request):
    quiz_passed_check = Quiz.objects.all().filter(chapter=3)
    check = None
    for quiz in quiz_passed_check:
        check = quiz.passed
    
    if check:
        courses = CourseModel.objects.all().filter(chapter=4)
        lessons = LessonModel.objects.all().filter(chapter=4)
        context = {
            'courses': courses,
            'lessons' : lessons,
        }
        return render(request, 'education/all_courses_chapter4.html', context)
    else:
        messages.info(request, 'You did not passed the quiz of Technical Characteristics of candlesticks.')
        return redirect('sniper_education')  

def all_courses_ch5(request):
    quiz_passed_check = Quiz.objects.all().filter(chapter=4)
    check = None
    for quiz in quiz_passed_check:
        check = quiz.passed
    
    if check:
        courses = CourseModel.objects.all().filter(chapter=5)
        lessons = LessonModel.objects.all().filter(chapter=5)
        context = {
            'courses': courses,
            'lessons' : lessons,
        }
        return render(request, 'education/all_courses_chapter5.html', context)
    else:
        messages.info(request, 'You did not passed the quiz of Technical Support and Resistance.')
        return redirect('sniper_education')  


def all_courses_ch6(request):
    quiz_passed_check = Quiz.objects.all().filter(chapter=5)
    check = None
    for quiz in quiz_passed_check:
        check = quiz.passed
    
    if check:
        courses = CourseModel.objects.all().filter(chapter=6)
        lessons = LessonModel.objects.all().filter(chapter=6)
        context = {
            'courses': courses,
            'lessons' : lessons,
        }
        return render(request, 'education/all_courses_chapter5.html', context)
    else:
        messages.info(request, 'You did not passed the quiz of Technical Indicators.')
        return redirect('sniper_education')  


def course_detail(request, course_id):
    main_course = get_object_or_404(CourseModel, id=course_id)
    context = {
        'main_course': main_course
    }
    return render(request, 'education/lesson-template.html', context)


def lesson_detail(request, lesson_id):
    main_lesson = get_object_or_404(LessonModel, id=lesson_id)
    context = {
        'main_lesson': main_lesson

    }
    return render(request, 'education/lesson-template.html', context)

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    context = {
        'quiz' : quiz
    }
    return render(request, 'education/quiz.html', context)

def check_quiz(request):
    if request.method == "POST":

        question = request.POST['question']
        quiz = Quiz.objects.all().filter(question=question)
        correct = request.POST['correct'] 
        user_answer = request.POST['final']
        correct = str(correct)
        user_answer = str(user_answer)
        correct = correct.replace(" ", "")
        user_answer = user_answer.replace(" ", "")

        if correct == user_answer:
            messages.info(request, 'Congratulations! You have passed the course! keep going...')
            for q in quiz:
                q.user = request.user
                q.passed = True
                q.save()
            
            return render(request,'education/sniper_education.html')
        else:
            messages.info(request, 'You did not passed the course! keep going try one more time.')
            return render(request,'education/sniper_education.html')
    else:
        return redirect('sniper_education')

    