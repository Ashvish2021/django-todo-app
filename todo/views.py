from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks=Task.objects.all()

    if request.method == 'POST':
        title=request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request,'todo/task_list.html',{'tasks':tasks})
def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')
def completed_task(request,id):
    task=Task.objects.get(id=id)
    task.completed=True
    task.save()
    return redirect('task_list')
def edit_task(request,id):
    task=Task.objects.get(id=id)
    if request.method == 'POST':
        task.title=request.POST.get('title')
        task.save()
        return redirect('task_list')
    return render(request, 'todo/edit_task.html', {'task':task})        


# Create your views here.
