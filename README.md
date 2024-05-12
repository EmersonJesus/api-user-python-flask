# API de Gerenciamento de Usuários

Esta é uma API simples para gerenciamento de usuários, com funcionalidades básicas como criar, atualizar, visualizar e excluir usuários, além de autenticação.

## Rotas Disponíveis

### Autenticação de Usuário

- **POST /auth**
  - Endpoint para autenticar um usuário.
  - Parâmetros:
    - `username`: Nome de usuário.
    - `password`: Senha do usuário.
  - Resposta:
    - `message`: Mensagem de sucesso ou falha.
    - `token`: Token de autenticação JWT válido por um determinado período de tempo.

### Gerenciamento de Usuários

- **POST /users**
  - Cria um novo usuário.
  - Parâmetros:
    - `username`: Nome de usuário.
    - `password`: Senha do usuário.
    - `email`: Endereço de e-mail do usuário (opcional).
  - Resposta:
    - `message`: Mensagem de sucesso ou falha.

- **PUT /users/<id>**
  - Atualiza um usuário existente.
  - Parâmetros:
    - `id`: ID do usuário a ser atualizado.
    - `username`: Novo nome de usuário.
    - `password`: Nova senha do usuário.
    - `email`: Novo endereço de e-mail do usuário (opcional).
  - Resposta:
    - `message`: Mensagem de sucesso ou falha.

- **GET /users**
  - Retorna todos os usuários cadastrados.
  - Resposta:
    - Lista de usuários.

- **GET /users/<id>**
  - Retorna um usuário específico com o ID fornecido.
  - Parâmetros:
    - `id`: ID do usuário a ser recuperado.
  - Resposta:
    - Dados do usuário.

- **DELETE /users/<id>**
  - Exclui um usuário existente.
  - Parâmetros:
    - `id`: ID do usuário a ser excluído.
  - Resposta:
    - `message`: Mensagem de sucesso ou falha.

## Autenticação JWT

Esta API utiliza autenticação JWT (JSON Web Token) para proteger as rotas que exigem autenticação. Ao fazer login com sucesso, um token JWT é gerado e deve ser incluído no cabeçalho das solicitações subsequentes para rotas protegidas.

Para incluir o token JWT no cabeçalho da solicitação: Authorization: Bearer <token>

## Exemplo de Uso

Aqui está um exemplo de uso básico da API:

1. Faça uma solicitação POST para `/auth` com as credenciais do usuário para obter um token JWT.
2. Use o token JWT recebido para acessar outras rotas protegidas, incluindo operações CRUD de usuário.

## Dependências

Esta API depende das seguintes bibliotecas Python:

- Flask: Framework web para Python.
- Flask-RESTful: Extensão do Flask para criação de APIs RESTful.
- Flask-JWT-Extended: Extensão do Flask para autenticação JWT.
- MySQLdb: Conector MySQL para Python.

Para instalar as dependências, você pode usar o arquivo `requirements.txt` incluído neste projeto: `pip install -r requirements.txt`


## Configuração

Antes de executar a aplicação, é necessário configurar o banco de dados MySQL e as credenciais de acesso no arquivo `config.ini`. Certifique-se de que o MySQL esteja em execução e acessível antes de iniciar a aplicação.

## Executando a Aplicação

Para iniciar a aplicação, execute o seguinte comando: `python run.py`

Isso iniciará o servidor Flask na porta padrão (5000) localmente. Você pode acessar a API em `http://localhost:5000`.
