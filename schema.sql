-- schema.sql

-- Drop tables if they exist to ensure a clean setup
DROP TABLE IF EXISTS evasao;
DROP TABLE IF EXISTS aluno;
DROP TABLE IF EXISTS escola;

-- Tabela para armazenar as escolas
CREATE TABLE escola (
    id_escola SERIAL PRIMARY KEY,
    nome_escola VARCHAR(255) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    regiao VARCHAR(50) NOT NULL
);

-- Tabela para armazenar os alunos, com referência à escola
CREATE TABLE aluno (
    id_aluno SERIAL PRIMARY KEY,
    nome_aluno VARCHAR(255) NOT NULL,
    data_nascimento DATE,
    id_escola INT,
    CONSTRAINT fk_escola
        FOREIGN KEY(id_escola) 
        REFERENCES escola(id_escola)
);

-- Tabela para registrar os eventos de evasão
CREATE TABLE evasao (
    id_evasao SERIAL PRIMARY KEY,
    data_evasao DATE NOT NULL,
    motivo VARCHAR(255) NOT NULL,
    ano_letivo INT NOT NULL,
    id_aluno INT UNIQUE, -- Um aluno só pode ter um registro de evasão
    CONSTRAINT fk_aluno
        FOREIGN KEY(id_aluno) 
        REFERENCES aluno(id_aluno)
);