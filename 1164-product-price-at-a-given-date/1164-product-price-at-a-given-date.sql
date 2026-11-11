# Write your MySQL query statement below
SELECT p.product_id,COALESCE(latest.new_price,10) AS price
FROM (SELECT DISTINCT(product_id) FROM Products) p
LEFT JOIN Products latest
ON p.product_id=latest.product_id AND
latest.change_date=(SELECT MAX(p2.change_date) FROM Products p2 where change_date<='2019-08-16' and p.product_id=p2.product_id )
