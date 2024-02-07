select nome

from autor a 
left join livro l  
on a.codautor = l.autor
where l.autor is null
order by nome asc;