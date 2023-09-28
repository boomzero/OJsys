from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
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
    except (KeyError, code.DoesNotExist):
        return render(
            request,
            "ojsys/submitpage.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))