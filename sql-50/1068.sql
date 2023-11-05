select
    P.product_name,
    S.year,
    S.price
from
    (
        select distinct
            product_id,
            year,
            price
        From
            Sales
    ) S
    left join Product P on S.product_id = P.product_id