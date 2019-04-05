from django.shortcuts import render
from django.http import HttpResponse
from.models import Quiz

# Create your views here.
def index(request):
    ques = Quiz.objects.all()
    return render(request, 'index.html', {'ques': ques})


def result(request):
    score = 0
    ques = Quiz.objects.all()
    for i in ques:
        userans = request.POST.get(i.question)
        if userans == i.answer:
            score += 1
    return HttpResponse('Your Score is ' + str(score) + '/' + str(len(ques)))

