select p.product_name, sum(unit) as unit
from Products p left join Orders o on p.product_id=o.product_id
where order_date >= '2020-02-01'
AND order_date < '2020-03-01'
group by p.product_id
having unit>=100
order by unit desc