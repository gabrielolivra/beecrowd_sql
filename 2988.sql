SELECT 
    DISTINCT te.name, 
    COUNT(ma.team_1 + ma.team_2) AS matches,
    SUM(
        CASE
            WHEN (ma.team_1_goals > ma.team_2_goals AND te.id = ma.team_1)
                 OR (ma.team_2_goals > ma.team_1_goals AND te.id = ma.team_2) THEN 1 
            ELSE 0 
        END
    ) AS victories,
    SUM(
        CASE
            WHEN (ma.team_1_goals < ma.team_2_goals AND te.id = ma.team_1)
                 OR (ma.team_2_goals < ma.team_1_goals AND te.id = ma.team_2) THEN 1 
            ELSE 0 
        END
    ) AS defeats,
    SUM(
        CASE
            WHEN (ma.team_1_goals = ma.team_2_goals AND te.id = ma.team_1)
                 OR (ma.team_2_goals = ma.team_1_goals AND te.id = ma.team_2) THEN 1 
            ELSE 0 
        END
    ) AS draws,
    SUM(
        CASE
            WHEN (ma.team_1_goals > ma.team_2_goals AND te.id = ma.team_1)
                 OR (ma.team_2_goals > ma.team_1_goals AND te.id = ma.team_2) THEN 1 
            ELSE 0 
        END
    ) * 3 +
    SUM(
        CASE
            WHEN (ma.team_1_goals = ma.team_2_goals AND te.id = ma.team_1)
                 OR (ma.team_2_goals = ma.team_1_goals AND te.id = ma.team_2) THEN 1 
            ELSE 0 
        END
    ) * 1 AS score
FROM 
    teams te
INNER JOIN 
    matches ma ON te.id = ma.team_1 OR te.id = ma.team_2
GROUP BY 
    te.name
ORDER BY score desc

