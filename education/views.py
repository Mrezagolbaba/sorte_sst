from multiprocessing import context
from django.shortcuts import render
from .models import CourseModel


def sniper_education(request):
    return render(request, 'education/sniper_education.html')


def introduction(request):
    return render(request, 'education/introduction.html')

def all_courses(request):
    courses = CourseModel.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'education/all_courses.html', context)