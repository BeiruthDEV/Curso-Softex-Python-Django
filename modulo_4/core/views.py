
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Tarefa
from .forms import TarefaForm

def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm() 
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em') # Ordena pelas mais novas
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'Models', 'Forms'],
        'tarefas': todas_as_tarefas,
        'form': form, 
    }
    return render(request, 'home.html', context)


def login(request):
    return HttpResponse("<input>Login</input>")
