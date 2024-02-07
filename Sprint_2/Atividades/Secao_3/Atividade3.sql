select count(livro.cod) as quantidade,
editora.nome, endereco.estado, endereco.cidade

from livro
inner join editora on 
    livro.editora = editora.codeditora
inner join endereco on 
    editora.endereco = endereco.codendereco
group by editora.nome, endereco.estado, endereco.cidade
order by quantidade desc
limit 5;
