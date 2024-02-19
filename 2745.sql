  select name, CASE
  when salary > 3000 then ROUND(salary * 0.10, 2) else 0 END as tax from people
  where salary > 3000