# Cadastro CNPJ - Projeto Django

Este é um projeto de cadastro de CNPJ desenvolvido em Django.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados em seu sistema:

- Python (versão 3.x)
- Pip (gerenciador de pacotes do Python)
- Ambiente virtual (opcional, mas recomendado)

## Como Rodar o Projeto

### Passo 1: Clonar o Repositório

Clone este repositório para o seu sistema local:

  - git clone https://github.com/Pedro26fer/cadastro_cnpj.git
  - cd cadastro_cnpj
    
### Passo 2: Configurar Ambiente Virtual (Opcional, mas Recomendado)
Crie e ative um ambiente virtual para isolar as dependências do projeto:


- python -m venv venv
- source venv/bin/activate   
No Windows: 
- venv\Scripts\activate

### Passo 3: Instalar Dependências
Instale as dependências do projeto:

- pip install -r requirements.txt

### Passo 4: Configurar Banco de Dados
Execute as migrações para configurar o banco de dados:

- python manage.py migrate

### Passo 5: Iniciar o Servidor
Inicie o servidor de desenvolvimento:

- python manage.py runserver

O projeto estará disponível em http://127.0.0.1:8000/

Passo 6: Acessar a Aplicação
Acesse a aplicação em seu navegador:

### Página inicial: http://127.0.0.1:8000/
### API de cadastro: http://127.0.0.1:8000/api/enterprises/
### Interface API: http://127.0.0.1:8000/swagger

### Notas Adicionais
Certifique-se de ter o Python instalado e acessível via linha de comando.
Se preferir, você pode usar um ambiente virtual para isolar as dependências deste projeto.
Certifique-se de ajustar configurações de banco de dados ou outras conforme necessário.

