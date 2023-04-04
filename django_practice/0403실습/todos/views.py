from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):
    todos = Todo.objects.all()

    context = {
        'todos':todos,
    }
    return render(request,'todos/index.html',context)


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo':todo,
    }
    return render(request,'todos/detail.html',context)


def create(request):
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            priority = form.cleaned_data['priority']
            deadline = form.cleaned_data['deadline']
            Todo.objects.create(
                title=title,
                content=content,
                priority=priority,
                deadline=deadline
            )
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {'form': form}
    return render(request, 'todos/create.html', context)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')
