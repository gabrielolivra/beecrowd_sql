SELECT DISTINCT
    departamento.nome as Departamento,
    empregado.nome As Empregado,  
    SUM(DISTINCT COALESCE(vencimento.valor, 0)) as "Salario Bruto",
    SUM(DISTINCT COALESCE(desconto.valor, 0)) as "Total Desconto",
    SUM(DISTINCT COALESCE(vencimento.valor, 0)) - SUM(DISTINCT COALESCE(desconto.valor, 0)) AS "Salario Liquido"
FROM 
    empregado
LEFT JOIN 
    emp_venc ON emp_venc.matr = empregado.matr
LEFT JOIN 
    vencimento ON vencimento.cod_venc = emp_venc.cod_venc
LEFT JOIN 
    emp_desc ON emp_desc.matr = empregado.matr
LEFT JOIN 
    desconto ON desconto.cod_desc = emp_desc.cod_desc
INNER JOIN 
    departamento ON departamento.cod_dep = empregado.lotacao
INNER JOIN 
    divisao On divisao.cod_dep = departamento.cod_dep
GROUP BY 
    divisao, departamento, empregado
ORDER BY 
    "Salario Liquido" DESC;
