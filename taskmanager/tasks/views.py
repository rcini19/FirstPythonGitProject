from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Task

def task_list(request):
    tasks = Task.objects.order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

@require_http_methods(["POST"])
def add_task(request):
    title = request.POST.get('title', '').strip()
    if title:
        Task.objects.create(title=title)
    return redirect('task_list')

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title', task.title).strip()
        task.description = request.POST.get('description', task.description)
        task.save()
        return redirect('task_list')
    return render(request, 'edit_task.html', {'task': task})

