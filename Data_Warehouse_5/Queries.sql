--which properties made the most money
SELECT
    p.PropertyID,
    p.Address,
    COUNT(f.RentalFactKey) AS RentalCount,
    SUM(f.PaidAmount) AS TotalPaid
FROM FactRental f
JOIN DimProperty p
    ON f.PropertyKey = p.PropertyKey
GROUP BY
    p.PropertyID,
    p.Address
ORDER BY TotalPaid DESC;

--which clients have spent the most money
SELECT
    c.ClientID,
    c.FirstName,
    c.LastName,
    COUNT(f.RentalFactKey) AS RentalCount,
    SUM(f.PaidAmount) AS TotalPaid
FROM FactRental f
JOIN DimClient c
    ON f.ClientKey = c.ClientKey
GROUP BY
    c.ClientID,
    c.FirstName,
    c.LastName
ORDER BY TotalPaid DESC;

--which properties stay rented the longest
SELECT
    p.PropertyID,
    p.Address,
    COUNT(f.RentalFactKey) AS RentalCount,
    SUM(f.RentalDays) AS TotalRentalDays,
    ROUND(AVG(f.RentalDays)) AS AverageRentalDays
FROM FactRental f
JOIN DimProperty p
    ON f.PropertyKey = p.PropertyKey
GROUP BY
    p.PropertyID,
    p.Address
ORDER BY AverageRentalDays DESC;

--select contracts whose current market rent differs from their perceived market price
SELECT
    c.FirstName,
    c.LastName,
    p.Address,
    f.RentalCost AS ContractRent,
    p.MonthlyRent AS CurrentRent,
    p.MonthlyRent - f.RentalCost AS RentDifference,
    d.FullDate AS CheckOutDate
FROM FactRental f
JOIN DimClient c
    ON f.ClientKey = c.ClientKey
JOIN DimProperty p
    ON f.PropertyKey = p.PropertyKey
LEFT JOIN DimDate d
    ON f.CheckOutDateKey = d.DateKey
WHERE
    (f.CheckOutDateKey IS NULL OR d.FullDate > CURRENT_DATE)
    AND f.RentalCost <> p.MonthlyRent
ORDER BY
    RentDifference DESC;