-- E1
-- Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, 
-- em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: 
-- cod, titulo, autor, editora, valor, publicacao, edicao, idioma

SELECT *
FROM livro
WHERE publicacao >= '2015-01-01'
ORDER BY cod ASC;

-- E2
-- Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  
-- Atenção às colunas esperadas no resultado final:  titulo, valor.
SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT 10;

-- E3
 -- Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
 -- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
 -- Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.
SELECT COUNT(livro.editora) as quantidade, nome, estado, cidade
FROM editora
INNER JOIN livro on codeditora = editora
INNER JOIN endereco on codendereco = endereco
group by nome, estado, cidade
ORDER BY  quantidade DESC
LIMIT 5

-- E4
-- Apresente a query para listar a quantidade de livros publicada por cada autor. 
-- Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, 
-- apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).
SELECT nome, codautor, nascimento, count(autor) as quantidade
FROM autor
left JOIN livro on autor = codautor
GROUP BY nome, codautor, nascimento
ORDER BY nome ASC

-- E5
-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil.
-- Ordene o resultado pela coluna nome, em ordem crescente.
SELECT autor.nome
FROM autor
LEFT JOIN livro l on autor.codautor = l.autor
INNER JOIN editora e on e.codeditora = l.editora
INNER JOIN endereco e2 on e2.codendereco = e.endereco
WHERE  e2.estado <> 'RIO GRANDE DO SUL' AND e2.estado <> 'PARANÁ'
ORDER BY autor.nome ASC

-- E6
-- Apresente a query para listar o autor com maior número de livros publicados. 
-- O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.
SELECT codautor, nome, quantidade_publicacoes
FROM  (SELECT autor, count(*) as quantidade_publicacoes
    FROM livro
    GROUP BY autor) l
LEFT JOIN autor on autor.codautor = l.autor
WHERE quantidade_publicacoes = (SELECT MAX(ct.quantidade_publicacoes) FROM (SELECT autor, count(*) as quantidade_publicacoes
    FROM livro
    GROUP BY autor) as ct)
GROUP BY codautor, nome, quantidade_publicacoes;

-- E7
-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
SELECT  autor.nome
FROM autor
LEFT JOIN livro l on autor.codautor = l.autor
GROUP BY autor.nome
HAVING count(l.autor) == 0
ORDER BY autor.nome ASC

