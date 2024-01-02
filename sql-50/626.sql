select
    id,
    if (
        id % 2 = 0,
        lag(student, 1) over (
            order by
                id
        ),
        ifnull (
            lead(student, 1) over (
                order by
                    id
            ),
            student
        )
    ) as student
from
    Seat