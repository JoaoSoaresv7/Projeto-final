# Descrição do projeto

Projeto de sistema completo de pedidos para uma pizzaria em formato web.  
Possui duas interfaces principais:  
- Página do cliente para realizar pedidos.
- Página do funcionário para visualizar e processar pedidos.

## Instruções de instalação

1. **Clone o repositório:**

```bash
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

