from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from collections import Counter



@login_required
def task_list(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task = Task.objects.get(id=task_id, user=request.user)
        if 'mark_ongoing' in request.POST:
            task.status = 'in_progress'
            task.save()
        elif 'mark_completed' in request.POST:
            task.status = 'completed'
            task.save()
        elif 'delete' in request.POST:
            task.delete()
        return redirect('task-list')
    tasks = Task.objects.filter(user=request.user)
    status_counts = Counter(tasks.values_list('status', flat=True))
    return render(request, 'tasks/task_list.html',
                  {'tasks_pending': tasks.filter(status='pending'),
                   "tasks_in_progress": tasks.filter(status='in_progress'),
                   "tasks_completed": tasks.filter(status='completed'),
                   "chart_data":{
                       'pending': status_counts.get('pending', 0),
                       'in_progress': status_counts.get('in_progress', 0),
                       'completed': status_counts.get('completed', 0),
                   }
                   })




@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})


