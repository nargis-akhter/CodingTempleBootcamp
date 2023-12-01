/* 
-unions and joins are similar
-union combines the results of two or more select statements
-columns should have the same # of columns, same name, should be in the same order, and contain related data types
-union only displays distinct values
-union all includes any duplicates
-looking for better results? use union
-seeking to optimize performance? opt for union all
*/

SELECT 
    *
FROM
    dept_emp 
UNION 
SELECT 
    *
FROM
    dept_manager;
    
    
SELECT 
    e.emp_no,
    e.first_name,
    e.last_name,
    NULL AS dept_no,
    NULL AS from_date
FROM
    employees_dup e
WHERE
    e.emp_no = 10001 
UNION ALL SELECT 
    NULL AS emp_no,
    NULL AS first_name,
    NULL AS last_name,
    m.dept_no,
    m.from_date
FROM
    dept_manager m;
