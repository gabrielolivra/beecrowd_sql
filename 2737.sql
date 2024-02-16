SELECT name, customers_number AS customers_number FROM lawyers WHERE customers_number =  (SELECT MAX(customers_number) FROM lawyers)
UNION all
SELECT name,  customers_number AS customers_number FROM lawyers  WHERE customers_number =  (SELECT MIN(customers_number) FROM lawyers)
UNION all
SELECT 'Average' AS name, cast(AVG(customers_number) as int) AS customers_number
FROM lawyers;