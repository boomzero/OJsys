from django.shortcuts import render
from django.http import HttpResponse
from .models import News
import markdown


def index(request):
    latest_news_list = News.objects.order_by("id")[:30]
    for news in latest_news_list:
        news.text = markdown.markdown(news.text)
    context = {"latest_news_list": latest_news_list}
    return render(request, "mainpage/index.html", context)