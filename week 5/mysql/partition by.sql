USE employees2;
/*
-group by statement reduces the number of rows in the output by rolling them up and then calculating the sums or averages for each group
-partition by divides the resultset into partitions and changes how the window function is calculated
-partition by doesn't reduce the number of rows returned in the output
*/

SELECT FirstName, LastName, Gender, Salary, COUNT(Gender) OVER (PARTITION BY Gender) as TotalGender
FROM EmployeeDemographics dem
JOIN
EmployeeSalary sal 
ON dem.EmployeeID = sal.EmployeeID