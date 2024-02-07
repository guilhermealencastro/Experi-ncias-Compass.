select autor.codautor, autor.nome, autor.nascimento, count(livro.cod) as quantidade
from autor
left join livro 
on livro.autor = autor.codautor
group by autor.codautor, autor.nome, autor.nascimento
order by autor.nome asc;