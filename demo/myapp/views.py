from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.

def home(request):
    return render(request, "home.html")

def todos(request):
    items = Todo.objects.all()
    return render(request, "todos.html", {"todos":items}) 
# here we are going to return a render, we are going to render a request, todos.html, and a python dicationary that contains variable with a key value pair that we want to view inside of {% for todo in todos %}, so pass todos.