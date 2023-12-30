select
    t1.customer_id as customer_id
from
    (
        select distinct
            customer_id,
            product_key
        from
            Customer
    ) as t1
group by
    t1.customer_id
having
    count(t1.product_key) = (
        select
            count(*)
        from
            Product
    )