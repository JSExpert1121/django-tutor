from django.shortcuts import render
from .models import Question
# Create your views here.


def homeview(request):
    '''
    landing page
    '''
    print(request.headers)

    questions = Question.objects.all()
    context = {
        "text": 'This is from context',
        'questions': questions
    }

    return render(request, 'personal/home.html', context)
