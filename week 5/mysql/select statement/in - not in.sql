SELECT 
    *
FROM
    employees
WHERE
    first_name IN ('Denis' , 'Elvis'); #like multiple equal statements
    
SELECT 
    *
FROM
    employees
WHERE
    first_name NOT IN ('John' , 'Mark', 'Jacob');