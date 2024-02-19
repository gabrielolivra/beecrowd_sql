SELECT city_name, population FROM cities  WHERE population = ( SELECT population FROM cities ORDER BY population DESC LIMIT 1 OFFSET 1)
UNION all 
SELECT city_name, population FROM cities 
WHERE population = ( SELECT population FROM cities ORDER BY population asc LIMIT 1 OFFSET 1) 