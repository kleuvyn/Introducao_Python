# Passo 1: Instalar o Django

Certifique-se de ter o Python instalado em seu sistema. Em seguida, você pode instalar o Django usando o pip, o gerenciador de pacotes do Python:

pip install django

# Passo 2: Criar um Novo Projeto Django

'''Abra um terminal e navegue até o diretório onde deseja criar o seu projeto Django. Em seguida, execute o seguinte comando para criar um novo projeto:'''

django-admin startproject nome_do_projeto

# Substitua "nome_do_projeto" pelo nome desejado para o seu projeto.
# Passo 3: Criar um Aplicativo Django

'''Navegue até o diretório do seu projeto Django e execute o seguinte comando para criar um novo aplicativo:'''

python manage.py startapp nome_do_aplicativo

# Substitua "nome_do_aplicativo" pelo nome desejado para o seu aplicativo.
# Passo 4: Definir Modelos de Dados

''' o arquivo models.py dentro do diretório do seu aplicativo e defina os modelos de dados usando classes Python. '''

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Passo 5: Registrar o Aplicativo

''' o arquivo settings.py dentro do diretório do seu projeto e adicione o nome do seu aplicativo à lista INSTALLED_APPS:'''

INSTALLED_APPS = [
    # outros aplicativos
    'nome_do_aplicativo',
]

# Passo 6: Executar as Migrações do Banco de Dados

'''Execute o seguinte comando para criar as tabelas do banco de dados com base nos seus modelos de dados:'''

python manage.py makemigrations
python manage.py migrate

# Passo 7: Criar Visualizações

'''Crie visualizações para manipular solicitações HTTP.abra o arquivo views.py dentro do diretório do seu aplicativo e defina suas visualizações. Por exemplo:
'''

from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

# Passo 8: Definir URLs

'''Crie um arquivo urls.py dentro do diretório do seu aplicativo e defina as URLs para suas visualizações.'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# Passo 9: Criar Templates HTML

'''Crie arquivos de template HTML para renderizar suas páginas. Coloque-os dentro do diretório templates do seu aplicativo.'''
# Passo 10: Iniciar o Servidor de Desenvolvimento

# Execute o seguinte comando para iniciar o servidor de desenvolvimento do Django:

python manage.py runserver

# Acesse o seu aplicativo web em um navegador visitando http://localhost:8000.