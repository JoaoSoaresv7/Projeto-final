<<<<<<< HEAD
# Descrição do projeto

Projeto de sistema completo de pedidos para uma pizzaria em formato web.  
Possui duas interfaces principais:  
- Página do cliente para realizar pedidos.
- Página do funcionário para visualizar e processar pedidos.

## Instruções de instalação
```bash

1. Clone o repositório (Da branch 'frontend'):
git clone https://github.com/JoaoSoaresv7/Projeto-final.git
cd Projeto-final

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. instale as dependências:
pip install -r requirements.txt

4. Aplique as migrações:
python manage.py makemigrations
python manage.py migrate

5. Inicie o servidor de desenvolvimento:
python manage.py runserver

6. Acesse no navegador:
Página do cliente: http://127.0.0.1:8000/cliente/fazer/
Página do funcionário (fila de pedidos): http://127.0.0.1:8000/cliente/fila/

Estrutura do Projeto:

cliente/ — App responsável pelos pedidos dos clientes
funcionario/ — App para o controle dos pedidos pela equipe da pizzaria
filapizza/ — Configuração geral do projeto Django
```

## Tecnologias utilizadas
**Geral:**
- Django
- Visual Studio Code
- Git
- GitHub

**BackEnd:**
- Python
- OpenCage API

**FrontEnd:**
- JavaScript
- HTML
- CSS
- Figma
- Google Fonts
- Miro
- Django ORM
- Hashing Django
- Django Templates

**Banco de dados:**
- SQLite Studio
- Biblioteca SQL

  ## 📁 Estrutura dos Arquivos
```
PROJETO-FINAL/
├── cliente/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── funcionario/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── fila_pizza/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home_pizzaria/
├── pedidos_shared/
│   ├── __init__.py
│   └── logica.py
├── venv/
├── db.sqlite3
├── manage.py
└── README.md
```

## Integrantes do grupo
- Ariel Shalom
- Gabriel Lima
- Gabriel Vicente
- João Vitor Soares
- Julia Rosa Cosme
- Luca Zago Couto
- Matheus Ramos da Silva
- Rafael Ramos
=======
# Descrição do projeto

Projeto de sistema completo de pedidos para uma pizzaria em formato web.  
Possui duas interfaces principais:  
- Página do cliente para realizar pedidos.
- Página do funcionário para visualizar e processar pedidos.

## Instruções de instalação
```bash

1. Clone o repositório (Da branch 'frontend'):
git clone https://github.com/JoaoSoaresv7/Projeto-final.git
cd Projeto-final

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. instale as dependências:
pip install -r requirements.txt

4. Aplique as migrações:
python manage.py makemigrations
python manage.py migrate

5. Inicie o servidor de desenvolvimento:
python manage.py runserver

6. Acesse no navegador:
Página do cliente: http://127.0.0.1:8000/cliente/fazer/
Página do funcionário (fila de pedidos): http://127.0.0.1:8000/cliente/fila/

Estrutura do Projeto:

cliente/ — App responsável pelos pedidos dos clientes
funcionario/ — App para o controle dos pedidos pela equipe da pizzaria
filapizza/ — Configuração geral do projeto Django
```

## Tecnologias utilizadas
**Geral:**
- Django
- Visual Studio Code
- Git
- GitHub

**BackEnd:**
- Python
- OpenCage API

**FrontEnd:**
- JavaScript
- HTML
- CSS
- Figma
- Google Fonts
- Miro
- Django ORM
- Hashing Django
- Django Templates

**Banco de dados:**
- SQLite Studio
- Biblioteca SQL

  ## 📁 Estrutura dos Arquivos
```
PROJETO-FINAL/
├── cliente/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── funcionario/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── fila_pizza/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home_pizzaria/
├── pedidos_shared/
│   ├── __init__.py
│   └── logica.py
├── venv/
├── db.sqlite3
├── manage.py
└── README.md
```

## Integrantes do grupo
- Ariel Shalom
- Gabriel Lima
- Gabriel Vicente
- João Vitor Soares
- Julia Rosa Cosme
- Luca Zago Couto
- Matheus Ramos da Silva
- Rafael Ramos
>>>>>>> 81e4968abde002e858a3addca30aac4f09a89e45
