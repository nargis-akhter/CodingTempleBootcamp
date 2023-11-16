#the hire_date is before '1990-01-01' and the hire_date is after '2000-01-01'

SELECT 
    *
FROM
    employees
WHERE
    hire_date BETWEEN '1990-01-01' AND '2000-01-01';
    

    