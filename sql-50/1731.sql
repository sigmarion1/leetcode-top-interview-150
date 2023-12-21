select
    employee_id,
    name,
    r.reports_count,
    r.average_age
from
    Employees e
    inner join (
        select
            reports_to,
            round(avg(age)) as average_age,
            count(reports_to) as reports_count
        from
            Employees
        group by
            reports_to
    ) r ON e.employee_id = r.reports_to
order by
    employee_id