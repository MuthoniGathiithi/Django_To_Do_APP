from django.shortcuts import render,redirect
from .models import Task

#show task 
def show_tasks(request):
    Task=Task.objects.all()

    return render(request,"add_task.html", {'tasks': Task})


def add_tasks(request):
    if request.method == "POST"
    title =request.POST.get("title")
    Task.objects.create(title=title)
# Create your views here.
