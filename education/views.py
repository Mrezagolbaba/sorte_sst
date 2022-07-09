from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import CourseModel, LessonModel


def sniper_education(request):
    return render(request, 'education/sniper_education.html')


def introduction(request):
    return render(request, 'education/introduction.html')

def all_courses(request):
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
    return render(request, 'education/.html', context)


def lesson_detail(request, lesson_id):
    main_lesson = get_object_or_404(LessonModel, id=lesson_id)
    context = {

    }