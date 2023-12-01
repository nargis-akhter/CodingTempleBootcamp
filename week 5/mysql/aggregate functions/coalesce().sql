/* 
coalesce() syntax:
COALESCE(expression_1, expression_2..., expression_N)

-think of coalesce() as ifnull() that can have one, two, or more parameters
*/

#three arguments
SELECT 
    dept_no,
    dept_name,
    COALESCE(dept_manager, dept_name, 'N/A') AS dept_manager
FROM
    departments_dup
ORDER BY dept_no ASC;

#single argument
SELECT dept_no,
	dept_name,
	COALESCE('department manager name') AS fake_col
FROM
	departments_dup;