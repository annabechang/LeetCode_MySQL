"""
176. Second Highest Salary

Easy

491

252

Favorite

Share
SQL Schema
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

"""
# Write your MySQL query statement below
Select max(Salary) as SecondHighestSalary
From Employee
Where Salary < (SELECT max(Salary)
            FROM Employee);

"""
Success
Details 
Runtime: 157 ms, faster than 12.70% of MySQL online submissions for Second Highest Salary.
Memory Usage: N/A
"""
# Write your MySQL query statement below
Select max(Salary) as SecondHighestSalary
From Employee
Where Salary < (SELECT Salary
                FROM Employee
                ORDER BY Salary DESC
                LIMIT 1);

"""
Success
Details 
Runtime: 167 ms, faster than 7.38% of MySQL online submissions for Second Highest Salary.
"""

