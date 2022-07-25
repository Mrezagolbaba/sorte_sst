from django.http import HttpResponse
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
    return render(request, 'education/introduction.html')

def all_courses_ch1(request):
    courses = CourseModel.objects.all().filter(chapter=1)
    lessons = LessonModel.objects.all().filter(chapter=1)
    context = {
        'courses': courses,
        'lessons' : lessons,
    }
    return render(request, 'education/all_courses_chapter1.html', context)


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
        correct = quiz[:5]
        answer1 = request.POST['answer1']
        answer2 = request.POST['answer2']
        answer3 = request.POST['answer3']
        answer4 = request.POST['answer4'] 
        
        print(answer1)
        print(answer2)
        print(answer3)
        print(answer4)
    
    return redirect('sniper_education')