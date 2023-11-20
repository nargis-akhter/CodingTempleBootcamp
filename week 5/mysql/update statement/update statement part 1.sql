#update statement is used to update the values of existing records in a table

USE employees;

SELECT * from employees where emp_no = 999901;

UPDATE employees
SET
	first_name = 'Stella',
    last_name = 'Parkinson',
    birth_date = '1990-12-31',
    gender = 'F'
WHERE emp_no = 999901;

SELECT 
    *
FROM
    employees
ORDER BY emp_no DESC
LIMIT 10;