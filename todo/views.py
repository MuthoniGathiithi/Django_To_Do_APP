from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import date, timedelta
from django.contrib import messages

def show_tasks(request):
    selected_date = request.GET.get('date')
    if selected_date:
        selected_date_obj = date.fromisoformat(selected_date)
    else:
        selected_date_obj = date.today()

    # Get tasks for 3 consecutive days starting from selected_date_obj
    end_date = selected_date_obj + timedelta(days=2)
    consecutive_tasks = Task.objects.filter(date__range=[selected_date_obj, end_date]).order_by('date')

    return render(
        request,
        "add_task.html",
        {
            'tasks': Task.objects.filter(date=selected_date_obj),
            'selected_date': selected_date_obj,
            'today': date.today(),
            'consecutive_tasks': consecutive_tasks
        }
    )

def add_tasks(request):
    if request.method == "POST":
        title = request.POST.get("title")
        task_date = request.POST.get("date")
        if title and task_date:
            Task.objects.create(title=title, date=task_date)
            messages.success(request, "Task added successfully!")
            return redirect(f"/?date={task_date}")
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