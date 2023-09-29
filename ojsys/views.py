from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Dataset, Submission
from django.urls import reverse
from django.http import Http404
import markdown
from django.contrib.auth import authenticate


def index(request):
    latest_question_list = Question.objects.order_by("id")[:10]
    context = {"latest_question_list": latest_question_list}
    return render(request, "ojsys/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        md = markdown.markdown(question.text)
    except Question.DoesNotExist:
        raise Http404("problem does not exist")
    context = {"question": question, "md": md}
    return render(request, "ojsys/detail.html", context)


def submitpage(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("problem does not exist")
    context = {"question": question}
    return render(request, "ojsys/submitpage.html", context)


def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        code = request.POST["code"]
        lang = request.POST["lang"]
    except (KeyError):
        return render(
            request,
            "ojsys/submitpage.html",
            {
                "question": question,
                "error_message": "You didn't submit any code",
            },
        )
    else:
        sub = Submission(
            question=question, code=code, lang=lang, user = "admin" #for now
        )
        try:
            dataSets= Dataset.objects.get(Dataset, question=question_id)
        except(Exception):
            sub.status="Accepted"
            sub.score=0
            sub.save()
            return HttpResponseRedirect(reverse("ojsys:submitindex", args=()))
        
        return HttpResponseRedirect(reverse("ojsys:submitindex", args=()))

def submissions(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    latest_submission_list = Submission.objects.filter(question=question_id).order_by("-id")[:]
    context = {"latest_submission_list": latest_submission_list, "question": question}
    return render(request, "ojsys/submissions.html", context)
def submitindex(request):
    latest_submission_list = Submission.objects.order_by("-id")[:]
    context = {"latest_submission_list": latest_submission_list}
    return render(request, "ojsys/submitindex.html", context)
