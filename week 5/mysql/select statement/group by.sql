/*
-similar to distinct select statement - shows unique values in a column
-must be placed immediately after the where conditions and just before the order by clause
*/

SELECT 
    first_name, COUNT(first_name) AS names_count
FROM
    employees
GROUP BY first_name #only distinct values will be selected
ORDER BY first_name ASC;