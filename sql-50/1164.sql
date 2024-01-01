select
    d.product_id,
    p.new_price as price
from
    (
        select
            product_id,
            max(change_date) as last_change_date
        from
            Products
        where
            change_date <= '2019-08-16'
        group by
            product_id
    ) as d
    left join Products as p on d.product_id = p.product_id
    and d.last_change_date = p.change_date
union
select
    d.product_id,
    10 as price
from
    (
        select
            product_id,
            min(change_date) as min_change_date
        from
            Products
        group by
            product_id
        having
            min_change_date > '2019-08-16'
    ) as d