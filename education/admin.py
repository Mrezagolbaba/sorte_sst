from django.contrib import admin
from .models import Quiz, CourseModel, LessonModel

class QuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_answer')


class LessonAdmin(admin.TabularInline):
    model = LessonModel
    

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'chapter')
    list_filter = ('chapter',)
    list_display_links = ('id', 'title', 'chapter')
    inlines = [LessonAdmin ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(CourseModel, CourseAdmin)