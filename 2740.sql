SELECT CONCAT('Podium: ',team) AS name FROM LEAGUE where position in (select position from league order by position asc limit 3)
UNION ALL
SELECT CONCAT('Demoted: ', team) AS name FROM LEAGUE where position in (select position from league order by position DESC limit 2)