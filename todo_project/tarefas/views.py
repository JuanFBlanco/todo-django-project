from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm


def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})


def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = TarefaForm()

    return render(request, 'tarefas/criar.html', {'form': form})


def excluir_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('lista')