SELECT name, CAST(substring( payday, 9,2) as numeric(10, 2)) as day FROM loan;


SELECT name, CAST(EXTRACT(DAY FROM PAYDAY) AS INTEGER) AS day FROM loan;
