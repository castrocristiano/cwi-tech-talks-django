from django.shortcuts import render
from .models import Tarefa


def home(request):
    return render(request, 'home.html')


def tarefas(request):
    tarefas = Tarefa.objects.all()
    context = {
        'tarefas': tarefas
    }
    return render(request, 'tarefas.html', context)
