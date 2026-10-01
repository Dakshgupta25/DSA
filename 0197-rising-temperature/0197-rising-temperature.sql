SELECT today.id as Id
FROM Weather AS today
JOIN Weather AS yesterday
ON today.recordDate = DATE_ADD(yesterday.recordDate,INTERVAL 1 DAY)
WHERE today.temperature > yesterday.temperature;