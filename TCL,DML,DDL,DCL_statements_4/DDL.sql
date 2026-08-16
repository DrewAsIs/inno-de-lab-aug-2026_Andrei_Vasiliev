CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);

ALTER TABLE Employees
ADD COLUMN Email VARCHAR(100);

--did that since the names happened to be unique
UPDATE Employees 
SET Email = LOWER(FirstName || '.' || LastName || '@example.com');

ALTER TABLE Employees
ADD CONSTRAINT employees_email_unique UNIQUE (Email);

ALTER TABLE Departments
RENAME COLUMN Location TO OfficeLocation;