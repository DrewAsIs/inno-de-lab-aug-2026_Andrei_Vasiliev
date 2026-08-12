SELECT 
	item,
	COUNT(order_id) AS orders_count,
	AVG(amount) AS avg_amount
FROM 
	Orders
GROUP BY 
	item