-- sql/evasoes_por_motivo.sql
SELECT
    motivo,
    COUNT(id_evasao) AS total_evasoes
FROM evasao
GROUP BY motivo
ORDER BY total_evasoes DESC;