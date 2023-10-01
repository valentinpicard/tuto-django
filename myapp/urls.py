from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todo", views.article_list, name="todo_list"),
]
