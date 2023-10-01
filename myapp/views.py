from django.shortcuts import render
from .models import TodoItem


# Create your views here.
def home(request):
    return render(request, "home.html")


def article_list(request):
    items = TodoItem.objects.all().order_by("date")
    return render(request, "todo/todo_list.html", {"todo_items": items})
