select
    p.product_name,
    sum(o.unit) as unit
from
    Orders o
    left join Products p on o.product_id = p.product_id
where
    year (order_date) = 2020
    and month (order_date) = 2
group by
    o.product_id
having
    unit >= 100