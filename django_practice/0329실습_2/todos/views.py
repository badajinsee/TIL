from django.shortcuts import render
from .models import Todo

# Create your views here.

def index(request):
    todo = Todo.objects.all()

    context = {
        'todo':todo,
    }

    return render(request,'todos/index.html',context)


def detail(request, todo_pk) :
    todos = Todo.objects.get(pk=todo_pk)
    
    context = {
        'todos':todos,
    }

    return render(request,'todos/detail.html',context)


def new(request):
    return render(request,'todos/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')

    todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    todo.save()
    return render(request,'todos/create.html')