UPDATE Employees
SET Salary = Salary * 1.10
WHERE Department = 'HR';

UPDATE Employees
SET Department = 'Senior IT'
WHERE Salary > 70000.00;


DELETE FROM Employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM EmployeeProjects ep
    WHERE ep.EmployeeID = e.EmployeeID
);

BEGIN;
INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
VALUES ('Cloud Migration', 120000.00, '2023-11-01', '2024-05-01');

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT EmployeeID, ProjectID, 120
FROM Employees, Projects
WHERE Employees.FirstName = 'Bob'
  AND Employees.LastName = 'Johnson'
  AND Projects.ProjectName = 'Cloud Migration';

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT EmployeeID, ProjectID, 100
FROM Employees, Projects
WHERE Employees.FirstName = 'Diana'
  AND Employees.LastName = 'Prince'
  AND Projects.ProjectName = 'Cloud Migration';
COMMIT;