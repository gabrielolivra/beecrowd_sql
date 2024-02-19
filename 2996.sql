select packages.year, u1.name as sender, u2.name as receiver from packages 
inner join users u1 on packages.id_user_sender = u1.id 
inner join users u2 on packages.id_user_receiver = u2.id
where (packages.year = '2015' or packages.color = 'blue')
and u2.address != 'Taiwan' order by packages.year desc