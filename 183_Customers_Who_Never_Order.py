"""
183. Customers Who Never Order

Easy

247

30

Favorite

Share
SQL Schema
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

"""
# Write your MySQL query statement below
SELECT tb1.Name as Customers 
FROM Customers as tb1 
LEFT JOIN Orders as tb2 
ON tb1.Id = tb2.CustomerId
WHERE tb2.Id is null; 



"""
Success
Details 
Runtime: 331 ms, faster than 9.30% of MySQL online submissions for Customers Who Never Order.

"""
