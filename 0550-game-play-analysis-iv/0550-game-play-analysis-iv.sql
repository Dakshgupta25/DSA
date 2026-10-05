
SELECT 
    ROUND(
        COUNT(a2.player_id) / COUNT(DISTINCT a1.player_id), 
        2
    ) AS fraction
FROM (
    -- Step 1: Get the first login date for each player
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) a1
-- Step 2: Check for a login on the immediate next day
LEFT JOIN Activity a2
    ON a1.player_id = a2.player_id
    AND a2.event_date = DATE_ADD(a1.first_login, INTERVAL 1 DAY);