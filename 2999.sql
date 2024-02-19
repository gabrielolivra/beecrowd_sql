SELECT 
    empregado.nome,  
    ROUND(SUM(DISTINCT COALESCE(vencimento.valor, 0)) - SUM(DISTINCT COALESCE(desconto.valor, 0)), 2) AS salario
FROM 
    empregado empregado
INNER JOIN 
    emp_venc ON emp_venc.matr = empregado.matr
INNER JOIN 
    vencimento ON vencimento.cod_venc = emp_venc.cod_venc
LEFT JOIN 
    emp_desc ON emp_desc.matr = empregado.matr
LEFT JOIN 
    desconto ON desconto.cod_desc = emp_desc.cod_desc                           
GROUP BY 
    empregado.nome, empregado.lotacao_div
HAVING 
SUM(COALESCE(vencimento.valor, 0) - COALESCE(desconto.valor, 0)) > 8000
ORDER BY 
    empregado.lotacao_div asc