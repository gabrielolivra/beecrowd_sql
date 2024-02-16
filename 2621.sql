SELECT prod.name 
FROM products prod 
INNER JOIN providers prov ON prov.id = prod.id_providers
where prod.amount >= 10 and prod.amount <= 20 and prov.name iLIKE '%P%'