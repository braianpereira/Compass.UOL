-- Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV.
-- Utilizar o caractere ; (ponto e vírgula) como separador.
-- Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e
-- seus respectivos nomes de cabeçalho que listamos abaixo:

select	l.cod as 'CodLivro',
		l.titulo as 'Titulo',
		l.autor as 'CodAutor',
		a.nome as 'NomeAutor',
		l.valor as 'Valor',
		l.editora as 'CodEditora',
		e.nome as 'NomeEditora'
from livro l
	inner join autor a on l.autor = a.codautor 
	inner join editora e on l.editora = e.codeditora 
order by valor desc
limit 10

-- Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV. 
-- Utilizar o caractere | (pipe) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de 
-- colunas e seus respectivos nomes de cabeçalho que listamos abaixo:
 -- CodEditora

 -- NomeEditora

 -- QuantidadeLivros

SELECT 
    e.CodEditora, 
    e.nome as NomeEditora, 
    count(l.cod) as QuantidadeLivros
FROM editora e
LEFT JOIN livro l ON e.codeditora = l.editora
GROUP BY e.CodEditora, e.nome
ORDER BY QuantidadeLivros DESC
LIMIT 5