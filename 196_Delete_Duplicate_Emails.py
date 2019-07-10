"""
196. Delete Duplicate Emails
Easy

280

334

Favorite

Share
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Note:

Your output is the whole Person table after executing your sql. Use delete statement.
"""
"""
DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND
p1.Id > p2.Id

EXPLANATION:

Take the table in the example
Id | Email

1 | john@example.com

2 | bob@example.com

3 | john@example.com

Join the table on itself by the Email and you'll get:
FROM Person p1, Person p2 WHERE p1.Email = p2.Email

p1.Id | p1.Email | p2.Id | p2.Email

1	| john@example.com	| 1	| john@example.com

3	| john@example.com | 1	| john@example.com

2	| bob@example.com	| 2	| bob@example.com

1	| john@example.com	| 3	| john@example.com

3	| john@example.com	| 3	| john@example.com

From this results filter the records that have p1.Id>p2.ID, in this case you'll get just one record:
AND p1.Id > p2.Id

p1.Id | p1.Email | p2.Id | p2.Email

3	| john@example.com	| 1	| john@example.com

This is the record we need to delete, and by saying
DELETE p1

in this multiple-table syntax, only matching rows from the tables listed before the FROM clause are deleted, in this case just

p1.Id | p1.Email

3	| john@example.com

will be deleted
credit to fabrizio3, from https://leetcode.com/problems/delete-duplicate-emails/discuss/55553/Simple-Solution 
"""

# Write your MySQL query statement below
DELETE p1 
FROM Person as p1, Person as p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id;

"""
Success
Details 
Runtime: 1089 ms, faster than 6.56% of MySQL online submissions for Delete Duplicate Emails.
Memory Usage: N/A
"""
