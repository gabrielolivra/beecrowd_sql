select empregados.cpf, empregados.enome, departamentos.dnome from empregados empregados
inner join departamentos departamentos ON departamentos.dnumero = empregados.dnumero
where empregados.cpf not in (SELECT cpf_emp from trabalha)
order by empregados.cpf