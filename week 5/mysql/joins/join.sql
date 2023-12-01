/*inner join syntax

SELECT
	t1.column_name, t1.column_name, ..., t2.column_name, ...
From 
	table_1 t1
JOIN
	table_2 t2 ON t1.column_name = t2.column_name; #without using the keyword AS
*/

#in left join, order matters

SELECT 
    *
FROM
    dept_manager_dup
ORDER BY dept_no;


SELECT 
    *
FROM
    departments_dup
ORDER BY dept_no;


SELECT 
    m.dept_no, m.emp_no, m.from_date, m.to_date, d.dept_name
FROM
    dept_manager_dup m
        JOIN
    departments_dup d ON m.dept_no = d.dept_no
ORDER BY m.dept_no;