select mov.id, mov.name from movies mov 
inner join prices pri on pri.id = mov.id_prices
where pri.value < '2.00'