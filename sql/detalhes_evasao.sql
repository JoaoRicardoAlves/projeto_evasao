-- sql/detalhes_evasao.sql
SELECT
    a.nome_aluno,
    e.nome_escola,
    ev.data_evasao,
    ev.motivo,
    ev.ano_letivo
FROM evasao ev
JOIN aluno a ON ev.id_aluno = a.id_aluno
JOIN escola e ON a.id_escola = e.id_escola
ORDER BY e.nome_escola, a.nome_aluno;