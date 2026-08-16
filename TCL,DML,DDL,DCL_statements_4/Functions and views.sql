CREATE OR REPLACE FUNCTION CalculateAnnualBonus(
    p_employee_id INT, -- never used but required by task
    p_salary DECIMAL(10, 2)
)
RETURNS DECIMAL(10, 2)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN p_salary * 0.10;
END;
$$;

SELECT
    EmployeeID,
    FirstName,
    LastName,
    Salary,
    CalculateAnnualBonus(EmployeeID, Salary) AS annualbonus
FROM Employees;

CREATE OR REPLACE VIEW IT_Department_View as --changed the view to reflect the data changes in task 4.2
SELECT
    EmployeeID,
    FirstName,
    LastName,
    Salary
FROM Employees
WHERE Department = 'Senior IT';

SELECT *
FROM IT_Department_View;
