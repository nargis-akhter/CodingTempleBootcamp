/* 
-cross join connects all the values, not just those that match like inner joins
-useful when the tables in a database are not well connected
-cross join is used to generate a paired combination of each row of the first table with each row of the second table
-can cross join more than two tables
*/

#use a CROSS JOIN to return a list with all possible combinations between managers from the dept_manager table and department number 9
SELECT 

    dm.*, d.*
    
FROM

    departments d
    
        CROSS JOIN
        
    dept_manager dm
    
WHERE

    d.dept_no = 'd009'
    
ORDER BY d.dept_no;


#return a list with the first 10 employees with all the departments they can be assigned to
#hint: Don’t use LIMIT; use a WHERE clause
SELECT

    e.*, d.*

FROM

    employees e

        CROSS JOIN

    departments d

WHERE

    e.emp_no < 10011

ORDER BY e.emp_no, d.dept_name;


