from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/",views.detail, name="detail"),
    path("<int:question_id>/submitpage/", views.submitpage, name="submitpage"),
    path("<int:question_id>/submit/", views.submit, name="submit"),
]