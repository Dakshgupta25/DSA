# Write your MySQL query statement below
SELECT w1.id 
FROM Weather w1
JOIN Weather prev
ON w1.recordDate=prev.recordDate+ INTERVAL 1 DAY
WHERE prev.temperature<w1.temperature

