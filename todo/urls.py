from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_tasks, name='show_tasks'),  # Home page shows all tasks
    path('add/', views.add_tasks, name='add_tasks'),  # Form to add a new task
    path('remove/<int:task_id>/', views.remove_task, name='remove_task'),  # Remove a specific task
    path('update/<int:task_id>/', views.update_task, name='update_task'),  # Mark a task as completed
]