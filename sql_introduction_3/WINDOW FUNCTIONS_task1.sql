SELECT 
	o.order_id,
	c.customer_id,
	o.item,
	o.amount,
	SUM(o.amount) OVER(PARTITION BY c.customer_id) AS total_by_customer
FROM 
	Customers AS c
INNER JOIN 
	Orders AS o
ON 
	c.customer_id=o.customer_id
ORDER BY 
	o.order_id;