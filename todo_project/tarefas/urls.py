from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista'),
    path('criar/', views.criar_tarefa, name='criar'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir'),
]