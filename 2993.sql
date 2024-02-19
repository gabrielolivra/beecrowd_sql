SELECT amount as most_frequent_value

FROM (
    SELECT amount, COUNT(*) AS frequencia
    FROM value_table
    GROUP BY amount
    ORDER BY frequencia DESC
    LIMIT 1
) AS moda;