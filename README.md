# Sistema de Análise de Evasão Escolar

> Um sistema de console para gerenciar e analisar dados sobre a evasão escolar no ensino médio, desenvolvido para a disciplina de Banco de Dados.

---

### 📋 Índice

- ✨ Funcionalidades
- 📂 Estrutura do Projeto
- 📦 Pré-requisitos
- 🚀 Começando
  - 1. Configuração do Banco de Dados PostgreSQL
  - 2. Configuração do Ambiente Python
  - 3. Criação das Tabelas
- ▶️ Executando o Projeto
  - 1. Ajuste da Conexão
  - 2. Povoando o Banco com Dados Fictícios
  - 3. Iniciando a Aplicação

---

## ✨ Funcionalidades

- **Gerenciamento (CRUD)** completo para:
  - 🏫 Escolas
  - 🎓 Alunos
  - 🏃 Registros de Evasão
- **Geração de Relatórios** em console:
  - Evasão detalhada por aluno e escola.
  - Total de evasões agrupadas por motivo.
- **Povoamento de Banco de Dados** com dados fictícios para testes e demonstração.

## 📂 Estrutura do Projeto

```
projeto_evasao/
├── conexion/
│   └── db_connection.py      # Gerencia a conexão com o PostgreSQL
├── controller/
│   ├── controller_aluno.py   # Lógica de negócio para Aluno
│   ├── controller_escola.py  # Lógica de negócio para Escola
│   └── controller_evasao.py  # Lógica de negócio para Evasão
├── model/
│   ├── aluno.py              # Modelo de dados do Aluno
│   ├── escola.py             # Modelo de dados da Escola
│   └── evasao.py             # Modelo de dados da Evasão
├── reports/
│   └── relatorios.py         # Lógica para geração de relatórios
├── utils/
│   ├── config.py             # Funções de utilidade (menus, limpar tela)
│   └── splash_screen.py      # Tela inicial da aplicação
├── principal.py              # Ponto de entrada da aplicação
├── popular_banco.py          # Script para gerar dados fictícios
└── schema.sql                # Script SQL para criar a estrutura do banco
```

## 📦 Pré-requisitos

- **Python 3.x**
- **PostgreSQL**
- Bibliotecas Python: `psycopg2-binary`, `Faker`

## 🚀 Começando

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Configuração do Banco de Dados PostgreSQL

1.  **Instale o PostgreSQL** (exemplo para Debian/Ubuntu):
    ```bash
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    ```

2.  **Acesse o psql** como superusuário:
    ```bash
    sudo -u postgres psql
    ```

3.  **Crie o usuário e o banco de dados**. Substitua `consulta` e `teste123` se desejar.
    ```sql
    -- Crie um novo usuário (role) com senha
    CREATE ROLE consulta WITH LOGIN PASSWORD 'teste123';

    -- Crie o banco de dados
    CREATE DATABASE evasao;

    -- Dê todos os privilégios ao usuário no novo banco
    GRANT ALL PRIVILEGES ON DATABASE evasao TO consulta;
    ```

4.  **Ajuste o método de autenticação**:
    - Encontre o caminho do arquivo `pg_hba.conf`:
      ```sql
      SHOW hba_file;
      ```
    - Saia do psql com `\q`.
    - Edite o arquivo (use o caminho retornado pelo comando anterior):
      ```bash
      sudo nano /etc/postgresql/16/main/pg_hba.conf
      ```
    - Altere a linha `local all all peer` para `local all all md5`.
    - Salve o arquivo e reinicie o serviço do PostgreSQL:
      ```bash
      sudo systemctl reload postgresql
      ```

### 2. Configuração do Ambiente Python

1.  **Crie e ative um ambiente virtual** na raiz do projeto:
    ```bash
    # Cria a pasta .venv
    python3 -m venv .venv
    
    # Ativa o ambiente
    source .venv/bin/activate
    ```
    *(Seu terminal deve agora exibir `(.venv)` no início do prompt)*

2.  **Instale as dependências** com o `pip`:
    ```bash
    pip install psycopg2-binary Faker
    ```

### 3. Criação das Tabelas

Execute o script `schema.sql` para criar as tabelas no banco de dados. Você precisará digitar a senha do usuário `consulta`.

```bash
psql -U consulta -d evasao -f schema.sql
```

## ▶️ Executando o Projeto

### 1. Ajuste da Conexão

Verifique se as credenciais de conexão nos arquivos `principal.py` e `popular_banco.py` correspondem às que você configurou.

**Exemplo (`principal.py`, linha 20):**
```python
db = DBConnection(db_name="evasao", user="consulta", password="teste123")
```

### 2. Povoando o Banco com Dados Fictícios

Para ter dados para testar e visualizar os relatórios, execute o script de povoamento:

```bash
python3 popular_banco.py
```

### 3. Iniciando a Aplicação

Finalmente, execute o script principal para iniciar o sistema:

```bash
python3 principal.py
```

O sistema será iniciado, exibindo a tela de splash e o menu principal.