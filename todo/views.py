# todo/views.py
from django.shortcuts import render, redirect
from .models import Task

# View to display all tasks and add new tasks
def task_list(request):
    if request.method == 'POST':
        # Logic to add a new task
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')

    tasks = Task.objects.all().order_by('-created_at') # Get all tasks, newest first
    context = {'tasks': tasks}
    return render(request, 'todo/task_list.html', context)

# View to update a task (mark as complete/incomplete)
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed # Toggle the completed status
    task.save()
    return redirect('task_list')

# View to delete a task
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')