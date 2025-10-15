# Sistema de Análise de Evasão Escolar

Este projeto é um sistema de console para gerenciar e analisar dados sobre a evasão escolar no ensino médio público, desenvolvido para a disciplina de Banco de Dados.

## Requisitos

- Python 3.x
- PostgreSQL
- Bibliotecas Python: `psycopg2-binary`, `Faker`

## Configuração do Ambiente

### 1. Instalação do PostgreSQL

Para sistemas baseados em Debian/Ubuntu, abra o terminal e execute os seguintes comandos:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### 2. Configuração do Banco de Dados

1.  **Acesse o PostgreSQL:**
    ```bash
    sudo -u postgres psql
    ```

2.  **Crie um novo usuário (role).** Substitua `consulta` e `teste123` por suas credenciais desejadas.
    ```sql
    CREATE ROLE consulta WITH LOGIN PASSWORD 'teste123';
    ```

3.  **Crie o banco de dados.**
    ```sql
    CREATE DATABASE seu_banco;
    ```

4.  **Dê todas as permissões ao seu novo usuário no banco de dados criado.** Substitua `seu_banco` e `seu_usuario` se tiver usado nomes diferentes.
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
pip install psycopg2-binary Faker
```

### 4. Execução do Script de Criação de Tabelas

Execute o script `schema.sql` para criar as tabelas no seu banco de dados. Se estiver usando Docker, o comando é:

```bash
# Para Docker
docker-compose exec -T postgres psql -U consulta -d evasao < schema.sql

# Para instalação manual
# psql -U seu_usuario -d seu_banco -f schema.sql
```
Você precisará digitar a senha que criou anteriormente.

## Execução do Projeto

1.  **Configure a Conexão**

    Abra o arquivo `principal.py` e altere os detalhes da conexão na linha 20 para corresponder ao seu banco de dados, usuário e senha:

    ```python
    db = DBConnection(db_name="seu_banco", user="seu_usuario", password="sua_senha")
    ```



2.  **Popule o Banco de Dados**
Navegue até o diretório raiz do projeto (`projeto_evasao/`) e execute python3 popular_banco.py

Para que o banco tenha dados para exibição
Lembrando "São dados ficticios para testes e demonstração"

3.  **Execute o Programa**

    Navegue até o diretório raiz do projeto (`projeto_evasao/`) e execute o script principal:

    ```bash
    python3 principal.py
    ```

O sistema será iniciado, exibindo a tela de splash com as informações e o menu principal.