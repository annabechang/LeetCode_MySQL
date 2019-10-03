"""
178. Rank Scores
Medium

549

87

Favorite

Share
SQL Schema
Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
"""
# Write your MySQL query statement below
SELECT tb1.Score As Score, (SELECT count(distinct tb2.Score)
                            FROM Scores As tb2
                            WHERE tb2.Score > tb1.Score)+1 AS Rank
FROM Scores AS tb1 
# re arrange
ORDER BY tb1.Score DESC

"""
Success
Details 
Runtime: 570 ms, faster than 61.46% of MySQL online submissions for Rank Scores.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.
"""
SELECT Score,
    (SELECT count(distinct Score)
     FROM Scores 
     WHERE Score >= tb1.Score) Rank

FROM Scores AS tb1
ORDER BY Score DESC
"""
Success
Details 
Runtime: 602 ms, faster than 47.28% of MySQL online submissions for Rank Scores.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.
"""
# Write your MySQL query statement below
SELECT Score,
       (SELECT count(*)
        FROM (SELECT distinct Score s FROM Scores) tmp
        WHERE s >= Score) Rank
FROM Scores
ORDER BY Score DESC
"""
Success
Details 
Runtime: 205 ms, faster than 87.92% of MySQL online submissions for Rank Scores.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.
"""
SELECT s.Score, count(distinct t.score) Rank
FROM Scores AS s JOIN Scores t ON s.Score <= t.score
GROUP BY s.Id
ORDER BY s.Score DESC
"""
Success
Details 
Runtime: 636 ms, faster than 32.40% of MySQL online submissions for Rank Scores.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.
"""
