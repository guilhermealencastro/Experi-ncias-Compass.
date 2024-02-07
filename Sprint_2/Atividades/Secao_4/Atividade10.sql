SELECT
  ve.nmvdd AS vendedor,
  SUM(v.qtd * v.vrunt) AS valor_total_vendas,
  round(perccomissao / 100.0 * sum(v.qtd * v.vrunt), 2) as comissao        
  
 

FROM tbvendedor ve
LEFT JOIN tbvendas v ON ve.cdvdd = v.cdvdd
where status = 'Concluído'
GROUP BY ve.nmvdd
ORDER BY comissao DESC;


