from django import template
from blog.models import Question
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    latestQuestionList = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latestQuestionList' : latestQuestionList
    }
    return render(request, 'blog/index.html',context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def result(request, question_id):
    return HttpResponse("You're looking at the results of question %s." %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting at question %s." %question_id)
