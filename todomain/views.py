from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(task_complete=False).order_by('-modified_at')
    completed_task = Task.objects.filter(task_complete=True).order_by('-modified_at')
    print(completed_task)
    context = {
        'tasks':tasks,
        'completed_task':completed_task
        
        
    }
    return render(request , 'home.html', context)