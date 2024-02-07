select a.codautor, a.nome, count(livro.cod) as quantidade_publicacoes

from autor a
inner join livro 
on a.codautor = livro.autor
group by a.codautor, a.nome
having count(livro.cod) = (
select count(cod)
from livro
group by autor 
order by count(cod) desc
limit 1
);