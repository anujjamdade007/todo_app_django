from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def addtask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request , pk):
    task = get_object_or_404(Task , pk=pk)
    task.task_complete= True
    task.save()
    
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.task_complete= False
    task.save()

    return redirect('home')

def update_task(request , pk):
    update_task = get_object_or_404(Task , pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        Task.objects.update()
        update_task.task = new_task
        update_task.save()
        return redirect('home')
    else:
        context = {
            'update_task':update_task
        }
        
        return render(request, 'update_task.html', context)
    

def delete_task(request , pk):
    delete_task = get_object_or_404(Task , pk=pk)
    delete_task.delete()
    return redirect('home')

    
