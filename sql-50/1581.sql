select
    customer_id,
    count(customer_id) as count_no_trans
from
    Visits V
    left join Transactions T using (visit_id)
where
    T.transaction_id is null
group by
    V.customer_id