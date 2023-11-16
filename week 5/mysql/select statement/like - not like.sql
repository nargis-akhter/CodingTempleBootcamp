# % - matches sequence of characters
# _  - matches single character

#executes all names starting with Mar
SELECT 
    *
FROM
    employees
WHERE
    first_name LIKE ('Mar%');
    
    
#executes all names ending with mar
SELECT 
    *
FROM
    employees
WHERE
    first_name LIKE ('%mar');
    

#retrieve a list with all employees who have been hired in the year 2000
SELECT
    *
FROM
    employees
WHERE
    hire_date LIKE ('%2000%');
    

    
    
    
