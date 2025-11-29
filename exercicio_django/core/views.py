from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Tarefa
from .forms import TarefaForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    tasks = Tarefa.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = TarefaForm(request.user, request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  
            task.save()
            return redirect('home')
    else:
        form = TarefaForm(request.user)

    return render(request, 'core/home.html', {'tasks': tasks, 'form': form})

@login_required
@require_POST
def complete_task(request, task_id):
    task = get_object_or_404(Tarefa, id=task_id, user=request.user)
    task.status = 'concluida'
    task.save()
    return redirect('home')

@login_required
@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Tarefa, id=task_id, user=request.user)
    task.delete()
    return redirect('home')