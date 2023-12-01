/*
-on delete cascade - if a specific value from the parent table's primary key has been deleted, all the records from the child table will be removed as well
-where clause is very important or else you will lose all of your information!
*/

COMMIT;

SELECT 
    *
FROM
    titles
WHERE
    emp_no = 999903;


DELETE FROM employees 
WHERE
    emp_no = 999903;

ROLLBACK;