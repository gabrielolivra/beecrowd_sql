SELECT c.name, ROUND(((s.math * 2) + (s.specific * 3) + (s.project_plan * 5)) / 10, 2) AS avg 
FROM score s
INNER JOIN candidate c ON c.id = s.candidate_id
ORDER BY avg DESC;