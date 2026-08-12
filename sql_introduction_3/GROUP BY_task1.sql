SELECT 
	country, 
	COUNT(customer_id) AS customers_count
FROM 
	Customers 
GROUP BY 
	country;