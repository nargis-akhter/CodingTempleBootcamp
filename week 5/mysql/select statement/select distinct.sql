#extracts duplicate values
#distinct ignores null values unless told not to

SELECT DISTINCT
    gender
FROM
    employees;
    
SELECT 
    COUNT(DISTINCT first_name)
FROM
    employees;