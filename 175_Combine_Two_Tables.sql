"""
175. Combine Two Tables
Easy

642

93

Favorite

Share
SQL Schema
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
 

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State

"""
# Write your MySQL query statement below

SELECT tb1.FirstName as FirstName, tb1.LastName as LastName, tb2.City as City, tb2.State as State
FROM Person as tb1 
LEFT JOIN Address as tb2 
ON tb1.PersonId = tb2.PersonId;
"""
Success
Details 
Runtime: 223 ms, faster than 42.96% of MySQL online submissions for Combine Two Tables.
Memory Usage: N/A
"""
