SELECT temperature, COUNT(mark) as number_of_records
FROM records r1
WHERE mark IN (SELECT mark FROM records r2 WHERE r1.mark = r2.mark)
GROUP BY temperature, mark
order by mark asc