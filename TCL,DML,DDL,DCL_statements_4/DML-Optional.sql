SELECT p.ProjectName 
FROM Projects p
JOIN EmployeeProjects ep
    ON p.ProjectID = ep.ProjectID
JOIN Employees e
    ON ep.EmployeeID = e.EmployeeID
WHERE e.FirstName = 'Bob'
  AND e.LastName = 'Johnson'
  AND ep.HoursWorked > 150;

SELECT ProjectID, ProjectName, Budget
FROM Projects; --check before the update

UPDATE Projects p
SET Budget = Budget * 1.10
WHERE EXISTS (
    SELECT 1
    FROM EmployeeProjects ep
    JOIN Employees e
        ON ep.EmployeeID = e.EmployeeID
    WHERE ep.ProjectID = p.ProjectID
      AND e.Department = 'IT'
);

SELECT ProjectID, ProjectName, Budget
FROM Projects; --check after the update

SELECT ProjectID, ProjectName, StartDate, EndDate
FROM Projects;

UPDATE Projects
SET EndDate = StartDate + INTERVAL '1 year'
WHERE EndDate IS NULL;

SELECT ProjectID, ProjectName, StartDate, EndDate
FROM Projects;

BEGIN;
WITH new_employee AS (
    INSERT INTO Employees (FirstName, LastName, Department, Salary, Email)
    VALUES ('Karl', 'Marx', 'IT', 55000.00,'Karl.Marx@example.com')
    RETURNING EmployeeID
)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT
    new_employee.EmployeeID,
    p.ProjectID,
    80
FROM new_employee
JOIN Projects p
    ON p.ProjectName = 'Website Redesign';
COMMIT;

SELECT
    e.EmployeeID,
    e.FirstName,
    e.LastName,
    p.ProjectName,
    ep.HoursWorked
FROM Employees e
JOIN EmployeeProjects ep
    ON e.EmployeeID = ep.EmployeeID
JOIN Projects p
    ON ep.ProjectID = p.ProjectID
WHERE e.FirstName = 'Karl'
  AND e.LastName = 'Marx';
