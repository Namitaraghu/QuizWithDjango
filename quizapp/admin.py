from django.contrib import admin
from . models import Quiz

class QuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice1', 'choice2', 'choice3', 'answer')


admin.site.register(Quiz,QuizAdmin)