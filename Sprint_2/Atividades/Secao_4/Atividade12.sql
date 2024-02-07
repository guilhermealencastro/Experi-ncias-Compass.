select de.cddep, de.nmdep, de.dtnasc, v.valor_total_vendas

from tbdependente de
join(
select cdvdd,
sum(qtd * vrunt) as valor_total_vendas
from tbvendas
where status = 'Concluído' 
group by cdvdd
having valor_total_vendas > 0
order by valor_total_vendas asc
limit 1
) v on de.cdvdd = v.cdvdd;

