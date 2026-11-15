select
d.name as Department,
s.name as Employee,
s.salary as Salary
from Employee s
join (
    select id,max(salary) as maxi,departmentId
    from Employee group by departmentId 
) s2
on  s.departmentId=s2.departmentId and s.salary=s2.maxi 
left join Department d
on s.departmentId = d.id