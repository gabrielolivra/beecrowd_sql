 select c.name, o.id from orders o
 inner join customers c on c.id = o.id_customers
 where o.orders_date between '2016-01-01' and '2016-06-30'