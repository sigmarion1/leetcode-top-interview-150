select
    t1.person_name
from
    (
        select
            person_name,
            sum(weight) over (
                order by
                    turn
            ) as weight_sum
        from
            Queue
        order by
            weight_sum desc
    ) as t1
where
    t1.weight_sum <= 1000
limit
    1