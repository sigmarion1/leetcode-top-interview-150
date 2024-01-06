(
    select
        name as results
    from
        Users u
        join MovieRating mr on mr.user_id = u.user_id
    group by
        1
    order by
        count(*) desc,
        1
    limit
        1
)
union all
(
    select
        title as results
    from
        Movies m
        join MovieRating mr on mr.movie_id = m.movie_id
    where
        month (created_at) = 2
        and year (created_at) = 2020
    group by
        1
    order by
        avg(rating) desc,
        1
    limit
        1
)