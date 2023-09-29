from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.http import Http404
import markdown


def index(request):
    latest_question_list = Question.objects.order_by("id")[:10]
    context = {"latest_question_list": latest_question_list}
    return render(request, "ojsys/problemset/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        md = markdown.markdown(question.text)
    except Question.DoesNotExist:
        raise Http404("problem does not exist")
    context = {"question": question, "md": md}
    return render(request, "ojsys/problemset/detail.html", context)


def submitpage(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("problem does not exist")
    context = {"question": question}
    return render(request, "ojsys/problemset/submitpage.html", context)


def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        code = request.POST["code"]
        lang = request.POST["lang"]
    except ():
        return render(
            request,
            "ojsys/submitpage.html",
            {
                "question": question,
                "error_message": "You didn't submit any code",
            },
        )
    else:
        # Temporarily redirect back
        return HttpResponseRedirect(reverse("ojsys:detail", args=(question.id,)))