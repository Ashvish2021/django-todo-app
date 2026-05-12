from django.urls import path
from . import views
urlpatterns = [
    path('tasks/', views.task_list,name='task_list'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('complete/<int:id>/', views.completed_task,name='completed_task'),
    path('edit/<int:id>/', views.edit_task,name='edit_task'),

]
