# Sistema de Análise de Evasão Escolar

Este projeto é um sistema de console para gerenciar e analisar dados sobre a evasão escolar no ensino médio público, desenvolvido para a disciplina de Banco de Dados.

## Requisitos

- Python 3.x
- PostgreSQL
- Biblioteca Python: `psycopg2-binary`

## Configuração do Ambiente (Linux)

### 1. Instalação do PostgreSQL

Abra o terminal e execute os seguintes comandos:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### 2. Configuração do Banco de Dados

1.  **Acesse o PostgreSQL:**
    ```bash
    sudo -u postgres psql
    ```

2.  **Crie um novo usuário (role).** Substitua `seu_usuario` e `sua_senha` por suas credenciais.
    ```sql
    CREATE ROLE seu_usuario WITH LOGIN PASSWORD 'sua_senha';
    ```

3.  **Crie o banco de dados.**
    ```sql
    CREATE DATABASE seu_banco;
    ```

4.  **Dê todas as permissões ao seu novo usuário no banco de dados criado.**
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE seu_banco TO seu_usuario;
    ```

5.  **Saia do psql:**
    ```sql
    \q
    ```

### 3. Instalação das Dependências Python

Certifique-se de ter o `pip` instalado. Em seguida, instale a biblioteca necessária:

```bash
pip install psycopg2-binary
```

### 4. Execução do Script de Criação de Tabelas

Execute o script `schema.sql` para criar as tabelas no seu banco de dados.

```bash
psql -U seu_usuario -d seu_banco -f schema.sql
```
Você precisará digitar a senha que criou anteriormente.

## Execução do Projeto

1.  **Configure a Conexão**

    Abra o arquivo `principal.py` e altere os detalhes da conexão na linha 20 para corresponder ao seu banco de dados, usuário e senha:

    ```python
    db = DBConnection(db_name="seu_banco", user="seu_usuario", password="sua_senha")
    ```

2.  **Execute o Programa**

    Navegue até o diretório raiz do projeto (`projeto_evasao/`) e execute o script principal:

    ```bash
    python3 principal.py
    ```

O sistema será iniciado, exibindo a tela de splash com as informações e o menu principal.