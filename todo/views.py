from django.shortcuts import render,redirect
from .models import Task

#show task 
def show_tasks(request):
    Task=Task.objects.all()

    return render(request,"add_task.html", {'tasks': tasks})

# Create your views here.
