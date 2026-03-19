from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista'),
    path('criar/', views.criar_tarefa, name='criar'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir'),
]