/* 
ifnull() syntax:
IFNULL(expression_1, expression_2)
-expression_1 = returns not null values
-expression_2 = returns null values

-ifnull() replaces the "NULL" text with something else
*/

SELECT 
	dept_no,
	IFNULL(dept_name, 
			'Department name not provided') as dept_name
FROM
	departments_dup;
	