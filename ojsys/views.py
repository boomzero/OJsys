from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "ojsys/problemset/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        title=question.title
    except Question.DoesNotExist:
        raise Http404("problem does not exist")
    context={"question": question, "title": title}
    return render(request, "ojsys/problemset/detail.html", context)

def submitpage(request, question_id):
    response = "You're looking at the submissions of question %s."
    return HttpResponse(response % question_id)


def submit(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)