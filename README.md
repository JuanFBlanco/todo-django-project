# Sistema de Lista de Tarefas

## Aluno
Juan Blanco

## Descrição do Sistema

Este projeto consiste em um sistema simples de gerenciamento de tarefas desenvolvido utilizando Python e Django.  
O sistema permite que usuários criem, visualizem e removam tarefas, facilitando a organização de atividades do dia a dia.

As tarefas são armazenadas em um banco de dados SQLite e cada tarefa está associada a um usuário, permitindo um relacionamento entre as informações.

O objetivo do projeto é aplicar conceitos fundamentais de programação em Python, incluindo Programação Orientada a Objetos, manipulação de banco de dados e desenvolvimento de aplicações web com Django.

---

## Funcionalidades Principais

- Criar novas tarefas
- Visualizar lista de tarefas
- Excluir tarefas
- Relacionar tarefas a usuários
- Interface web simples para gerenciamento das tarefas

---

## Tecnologias Utilizadas

- Python
- Django
- SQLite
- HTML
- Git
- GitHub

---

## Como Executar o Projeto

### 1 - Clonar o repositório

```bash
git clone https://github.com/JuanFBlanco/todo-django-project.git
```

### 2 - Acessar pasta do projeto
```bash
cd todo-django-project
```

### 3 - Criar o ambiente virtual
```bash
python -m venv venv
```

### 4 - Ativar o ambiente virtual
Windows:
```bash
venv\Scripts\activate
```
### 5 - Instalar as dependências
```bash
pip install django
```

### 6 - Executar as migrações do banco de dados
```bash
python manage.py migrate
```

### 7 - Executar o servidor
```bash
python manage.py runserver
```

### 8 - Abrir no navegador
```
http://127.0.0.1:8000
```
