from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.

def home(request):
    return render(request, "home.html")

def todos(request):
    items = Todo.objects.all()
    return render(request, "todos.html", {"todos":items}) 