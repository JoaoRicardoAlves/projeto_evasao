# Sistema de Análise de Evasão Escolar

> Sistema de console para gerenciar e analisar dados sobre a evasão escolar no ensino médio. O projeto utiliza Python, PostgreSQL e Docker para facilitar a configuração e execução.

---

### 📋 Índice

- ✨ Funcionalidades
- 📂 Estrutura do Projeto
- 📦 Pré-requisitos
- 🚀 Executando com Docker (Recomendado)
  - 1. Configuração do Ambiente
  - 2. Iniciando a Aplicação
- 🔧 Configuração Manual (Alternativa)
  - 1. Instalação do PostgreSQL
  - 2. Criação do Banco e Usuário
  - 3. Criação das Tabelas

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
- **Inicialização simplificada** com Docker Compose, que automatiza a criação e configuração do banco de dados.

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
├── schema.sql                # Script SQL para criar a estrutura do banco
├── docker-compose.yml        # Arquivo de configuração do Docker
└── start_docker_db.py        # Script auxiliar para iniciar o container Docker
```

## 📦 Pré-requisitos

- **Python 3.x**
- **Docker** e **Docker Compose**
- Bibliotecas Python: `psycopg2-binary`, `Faker`

---

## 🚀 Executando com Docker (Recomendado)

A maneira mais fácil de executar o projeto é usando Docker. Ele cuidará de criar, configurar e iniciar o banco de dados PostgreSQL automaticamente.

### 1. Configuração do Ambiente

1.  **Crie e ative um ambiente virtual** na raiz do projeto:
    ```bash
    # Cria a pasta .venv
    python3 -m venv .venv
    
    # Ativa o ambiente (Linux/macOS)
    source .venv/bin/activate

    # Ativa o ambiente (Windows)
    # .\.venv\Scripts\activate
    ```
    *(Seu terminal deve agora exibir `(.venv)` no início do prompt)*

2.  **Instale as dependências** com o `pip`:
    ```bash
    pip install psycopg2-binary Faker
    ```

### 2. Iniciando a Aplicação

Execute o script principal. Ele irá:
1.  Iniciar o container Docker com o banco de dados (se ainda não estiver rodando).
2.  Verificar se o banco está vazio e, se estiver, populá-lo com dados fictícios.
3.  Iniciar o menu principal do sistema.

```bash
python3 principal.py
```

Pronto! O sistema estará em execução.

---

## 🔧 Configuração Manual (Alternativa)

Se você não quiser usar Docker, pode configurar um servidor PostgreSQL localmente.

### 1. Instalação do PostgreSQL

Instale o PostgreSQL em seu sistema operacional. Para sistemas baseados em Debian (como Ubuntu), você pode usar:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### 2. Criação do Banco e Usuário

Acesse o `psql` e execute os seguintes comandos para criar o usuário e o banco de dados.

```bash
# Acesse como superusuário
sudo -u postgres psql

-- Crie um novo usuário (role) com senha
CREATE ROLE consulta WITH LOGIN PASSWORD 'teste123';

-- Crie o banco de dados
CREATE DATABASE evasao;

-- Dê todos os privilégios ao usuário no novo banco
GRANT ALL PRIVILEGES ON DATABASE evasao TO consulta;

-- Saia do psql
\q
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