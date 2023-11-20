SELECT 
    *
FROM
    departments
LIMIT 10;

#create new duplicate table
CREATE TABLE departments_dup (
    dept_no CHAR(4) NOT NULL,
    dept_name VARCHAR(40) NOT NULL
);

#verify empty table
SELECT 
    *
FROM
    departments_dup;

#select everything from departments table into departments_dup table
INSERT INTO departments_dup
(
dept_no,
dept_name
)
SELECT * FROM departments;

#check 
SELECT 
    *
FROM
    departments_dup
ORDER BY dept_no