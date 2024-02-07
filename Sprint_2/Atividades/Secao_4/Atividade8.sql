select t.cdvdd, t.nmvdd

from tbvendedor t
where t.cdvdd = (
    select v.cdvdd
    from tbvendas v
    group by v.cdvdd
    order by count(*) desc
    limit 1
)