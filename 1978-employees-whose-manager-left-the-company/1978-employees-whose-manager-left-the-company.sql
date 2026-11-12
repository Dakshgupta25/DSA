# Write your MySQL query statement below
SELECT e.employee_id 
FROM Employees e
LEFT JOIN Employees e2 
ON e.manager_id=e2.employee_id
WHERE e.salary<30000 AND (e.manager_id IS not NULL AND e2.employee_id is null)
ORDER BY e.employee_id;