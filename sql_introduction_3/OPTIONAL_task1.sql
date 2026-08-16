SELECT 
	CONCAT_WS(' ', c.first_name, c.last_name) AS full_name,
	c.country,
	COUNT(o.order_id) AS total_orders,
	SUM(o.amount) AS total_amount
FROM 
	Customers c
INNER JOIN 
	orders o
ON 
	c.customer_id=o.customer_id
WHERE EXISTS (
    SELECT 1
    FROM shippings AS s
    WHERE s.customer = c.customer_id
      AND s.status = 'Delivered'
)
GROUP BY 
	c.customer_id,
	c.country
HAVING
	COUNT(o.order_id)>=2;
	