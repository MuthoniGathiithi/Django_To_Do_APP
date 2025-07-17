from django.shortcuts import render,redirect
from .models import Task

#show task 
def show_tasks(request):
    Task=Task.objects.all()

    return render(request,"add_task.html", {'tasks': Task})


def add_tasks(request):
    if request.method == "POST":
     title =request.POST.get("title")
    if title:  # only add if title is not empty
            Task.objects.create(title=title)
    return redirect('show_tasks')  # make sure this matches your URL name
    return render(request, 'add_task.html')
# Create your views here.

def remove_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    return redirect ("show tasks")

