from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title:  # prevent empty tasks
            Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'add_task.html')