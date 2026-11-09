# Write your MySQL query statement below
SELECT person_name 
FROM (
    SELECT person_name,
           SUM(weight) OVER(ORDER BY turn) as total
    FROM Queue
) AS q
WHERE total<=1000
ORDER BY total DESC
LIMIT 1;
