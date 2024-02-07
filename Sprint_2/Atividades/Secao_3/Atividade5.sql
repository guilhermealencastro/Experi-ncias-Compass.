select distinct 
    a.nome
from
    Autor a
    inner join livro l
        on a.codautor = l.autor
    inner join editora e
        on l.editora = e.codeditora
    left join endereco en
        on e.endereco = en.codendereco
    where upper(en.estado) not in ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
    order by a.nome asc