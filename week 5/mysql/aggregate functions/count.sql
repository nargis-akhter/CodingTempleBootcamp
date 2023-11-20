#how many annual contracts with a value higher than or equal to $100,000 have been registered in the salaries table? 
SELECT 
    COUNT(*)
FROM
    salaries
WHERE
    salary >= 100000;


#how many managers do we have in the “employees” database? 
SELECT 
    COUNT(*)
FROM
    dept_manager;

