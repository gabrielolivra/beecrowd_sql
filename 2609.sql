select cat.name, sum(prod.amount) from products prod
inner join categories cat on cat.id = prod.id_categories
group by cat.name