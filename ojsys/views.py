from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Dataset, Submission
from django.urls import reverse
from django.http import Http404
import requests
import markdown
import os
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'ojsys/login.html', {'form': form})

def index(request):
    latest_question_list = Question.objects.all()
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
    #check auth status
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("ojsys:login", args=()))
    question = get_object_or_404(Question, pk=question_id)
    try:
        code = request.POST["code"]
        lang = request.POST["lang"]
    except KeyError:
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
            question=question, code=code, lang=lang, user=request.user, status="Pending"
        )
        question.submissionCnt += 1
        try:
            dataSets = Dataset.objects.filter(question=question)
        except Exception:
            sub.status = "Accepted"
            sub.score = 0
            question.acceptedCnt += 1
            sub.save()
            question.save()
            return HttpResponseRedirect(reverse("ojsys:submitindex", args=()))
        if lang == "cpp":
            for dataSet in dataSets:
                # judge by sending api call to  https://www.runoob.com/try/compile2.php
                response = requests.post(
                    "https://www.runoob.com/try/compile2.php",
                    data={
                        "code": code,
                        "fileext": lang,
                        "input": dataSet.dataset_in,
                        "language": 7,
                    },
                )
                print(response.text)
        #for now
        sub.status = "Accepted"
        sub.score = 0
        question.acceptedCnt += 1
        question.save()
        sub.save()
        return HttpResponseRedirect(reverse("ojsys:submitindex", args=()))


def submissions(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    latest_submission_list = Submission.objects.filter(question=question_id).order_by(
        "-id"
    )[:]
    context = {"latest_submission_list": latest_submission_list, "question": question}
    return render(request, "ojsys/submissions.html", context)


def submitindex(request):
    latest_submission_list = Submission.objects.order_by("-id")[:]
    context = {"latest_submission_list": latest_submission_list}
    return render(request, "ojsys/submitindex.html", context)
