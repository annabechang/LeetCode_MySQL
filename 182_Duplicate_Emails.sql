"""
182. Duplicate Emails
Easy

277

16

Favorite

Share
SQL Schema
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.
"""
# Write your MySQL query statement below
SELECT DISTINCT tb1.Email
FROM Person as tb1
INNER JOIN Person as tb2
ON tb1.Email = tb2.Email AND tb1.Id != tb2.Id;
"""
Success
Details 
Runtime: 376 ms, faster than 5.29% of MySQL online submissions for Duplicate Emails.
"""
SELECT Email
FROM Person
GROUP BY Email
Having count(*) > 1
"""
Runtime: 186 ms, faster than 85.14% of MySQL online submissions for Duplicate Emails.
"""
