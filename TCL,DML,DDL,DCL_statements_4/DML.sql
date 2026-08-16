INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES
    ('Kazimir', 'Piastowski', 'Marketing', 55000.00),
    ('Ivan', 'Ivanov', 'Finance', 63000.00);

SELECT *
FROM Employees;

SELECT FirstName, LastName
FROM Employees
WHERE Department = 'IT';

UPDATE Employees
SET Salary = 65000.00
WHERE FirstName = 'Alice'
  AND LastName = 'Smith';

DELETE FROM Employees
WHERE FirstName = 'Eve'
  AND LastName = 'Davis';

SELECT *
FROM Employees;