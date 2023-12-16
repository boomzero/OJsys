from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "ojsys"
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path("", views.index, name="index"),
    path("problemset/", views.index, name="index"),
    path("submissions/", views.submitindex, name="submitindex"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/submitpage/", views.submitpage, name="submitpage"),
    path("<int:question_id>/submissions/", views.submissions, name="submissions"),
    path("<int:question_id>/submit/", views.submit, name="submit"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
