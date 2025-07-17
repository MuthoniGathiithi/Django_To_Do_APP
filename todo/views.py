from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import date

def show_tasks(request):
    selected_date = request.GET.get('date')
    if selected_date:
        tasks = Task.objects.filter(date=selected_date)
    else:
        tasks = Task.objects.filter(date=date.today())
    return render(
        request,
        "add_task.html",
        {
            'tasks': tasks,
            'selected_date': selected_date,
            'today': date.today().isoformat()  # Add this line
        }
    )

def add_tasks(request):
    if request.method == "POST":
        title = request.POST.get("title")
        task_date = request.POST.get("date")
        if title and task_date:
            Task.objects.create(title=title, date=task_date)
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