"""
181. Employees Earning More Than Their Managers

Easy

352

40

Favorite

Share
SQL Schema
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+
"""
# Write your MySQL query statement below
SELECT tb1.Name as Employee
FROM Employee as tb1
LEFT JOIN Employee as tb2
ON tb1.ManagerId = tb2.Id
WHERE tb1.Salary > tb2.Salary
"""
Success
Details 
Runtime: 680 ms, faster than 5.28% of MySQL online submissions for Employees Earning More Than Their Managers.
"""

SELECT tb1.Name as Employee
FROM Employee as tb1, Employee as tb2
WHERE tb1.ManagerId = tb2.Id and tb1.Salary a> tb2.Salary

"""
Success
Details 
Runtime: 644 ms, faster than 7.11% of MySQL online submissions for Employees Earning More Than Their Managers.
"""
