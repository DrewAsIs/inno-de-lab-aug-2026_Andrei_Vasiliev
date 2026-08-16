SELECT 
	s.status,
	c.first_name,
	c.last_name
FROM 
	Customers AS c 
INNER JOIN Shippings AS s
ON c.customer_id = s.customer;