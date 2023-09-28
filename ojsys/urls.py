from django.urls import path

from . import views

app_name = "ojsys"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/submitpage/", views.submitpage, name="submitpage"),
    path("<int:question_id>/submitions/", views.submitpage, name="submitions"),
    path("<int:question_id>/submit/", views.submit, name="submit"),
]
