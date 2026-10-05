
SELECT
    ROUND(
        SUM(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1.0 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS immediate_percentage
FROM Delivery d
JOIN (
    SELECT customer_id, MIN(order_date) AS min_order_date
    FROM Delivery 
    GROUP BY customer_id
) d2
  ON d.customer_id = d2.customer_id
 AND d.order_date = d2.min_order_date;