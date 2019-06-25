"""
177. Nth Highest Salary
Medium

247

195

Favorite

Share
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
"""
#LIMIT (OFFSET, COUNT) 
#OFFSET STARTS FROM 0 THUS TO RETURN Nth ITEM, IT'S N-1

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE m INT;
SET m = n-1;

  RETURN (
      SELECT Salary 
      FROM Employee 
      GROUP BY Salary 
      ORDER BY Salary DESC
      LIMIT m, 1
  );
END

"""

Success
Details 
Runtime: 180 ms, faster than 84.63% of MySQL online submissions for Nth Highest Salary.
Memory Usage: N/A
"""
