# tasks.ulrs.py
from django.urls import path
from . import views

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('', views.taskList, name='task-list'),
    path('newtask/', views.newTask, name='new-task'),
    path('edittask/<int:id>', views.editTask, name='edit-task'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]
