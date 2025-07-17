from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def show_tasks(request):
    tasks = Task.objects.all()
    return render(request, "add_task.html", {'tasks': tasks})

def add_tasks(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect('show_tasks')
    return render(request, 'add_task.html')

def remove_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("show_tasks")
    return render(request, "confirm_delete.html", {'task': task})

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.completed = True
        task.save()
        return redirect('show_tasks')
    return render(request, "confirm_update.html", {'task': task})