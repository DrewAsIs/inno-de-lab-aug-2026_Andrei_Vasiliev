CREATE ROLE hr_user WITH
    LOGIN
    PASSWORD 'hr_user';

GRANT SELECT
ON TABLE Employees 
TO hr_user;

GRANT INSERT, UPDATE
ON TABLE Employees
TO hr_user;

GRANT USAGE
ON SEQUENCE employees_employeeid_seq
TO hr_user;