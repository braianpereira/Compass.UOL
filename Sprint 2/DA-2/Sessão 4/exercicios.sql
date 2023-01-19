--E8
-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
-- e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
SELECT t.cdvdd, v.nmvdd
FROM tbvendedor v
INNER JOIN tbvendas t on v.cdvdd = t.cdvdd
WHERE t.status = 'Concluído'
GROUP BY t.cdvdd, v.nmvdd
HAVING count(t.cdvdd) = (SELECT MAX(qtd) FROM (SELECT COUNT(cdvdd) as qtd FROM tbvendas WHERE status = 'Concluído' GROUP BY tbvendas.cdvdd) as tt);

-- E9
-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, 
-- e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.
SELECT cdpro, nmpro
FROM tbvendas
WHERE status = 'Concluído' AND dtven between '2014-02-03' AND '2018-02-02'
GROUP BY cdpro, nmpro
HAVING count(cdpro) = (SELECT MAX(qtd) FROM (SELECT COUNT(cdpro) as qtd FROM tbvendas WHERE status = 'Concluído' AND dtven between '2014-02-03' AND '2018-02-02' GROUP BY cdpro, nmpro) as tt)

-- E10
-- A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
-- O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

-- Com base em tais informações, calcule a comissão de todos os vendedores, 
--considerando todas as vendas armazenadas na base de dados com status concluído.

-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. 
--O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.
SELECT v.nmvdd as VENDEDOR,
       SUM(t.qtd * t.vrunt) as VALOR_TOTAL_VENDAS,
        round( SUM(t.qtd * t.vrunt * v.perccomissao) / 100, 2) as COMISSAO
FROM tbvendedor v
LEFT JOIN tbvendas t on v.cdvdd = t.cdvdd
WHERE t.status = 'Concluído'
GROUP BY v.nmvdd
ORDER BY comissao DESC;

-- E11
-- Apresente a query para listar o código e nome cliente com maior gasto na loja. 
-- As colunas presentes no resultado devem ser cdcli, nmcli e gasto, 
-- esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.
SELECT cdcli, nmcli, SUM(qtd * vrunt) as gasto
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY cdcli, nmcli
HAVING SUM(qtd * vrunt) = (SELECT max(val) FROM (SELECT SUM(qtd * vrunt) as val FROM tbvendas WHERE status = 'Concluído'
GROUP BY cdcli, nmcli )  )

-- E12
-- Apresente a query para listar código, nome e data de nascimento dos dependentes do 
-- vendedor com menor valor total bruto em vendas (não sendo zero). 
-- As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

-- Observação: Apenas vendas com status concluído.
SELECT dependente.cddep,
       dependente.nmdep,
       dependente.dtnasc,
       SUM(vendas.qtd * vendas.vrunt) AS valor_total_vendas
FROM tbvendas AS vendas
         JOIN tbvendedor AS vendedor ON vendas.cdvdd = vendedor.cdvdd
         JOIN tbdependente AS dependente on vendedor.cdvdd = dependente.cdvdd
WHERE vendas.status = 'Concluído'
GROUP BY cddep, nmdep, dtnasc
ORDER BY valor_total_vendas
LIMIT 1;

-- E13
-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz 
-- (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

SELECT cdpro,
       nmcanalvendas,
       nmpro,
       SUM(qtd) AS quantidade_vendas
FROM tbvendas
WHERE (nmcanalvendas = 'Ecommerce'
    OR nmcanalvendas = 'Matriz')
    AND status = 'Concluído'
GROUP BY cdpro, nmcanalvendas, nmpro
ORDER BY quantidade_vendas
LIMIT 10;

-- E14
-- Apresente a query para listar o gasto médio por estado da federação. 
-- As colunas presentes no resultado devem ser estado e gastomedio. 
-- Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

-- Observação: Apenas vendas com status concluído.
SELECT estado,
       ROUND(AVG(qtd * vrunt),2) AS gastomedio
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado;

-- E15
-- Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.
SELECT cdvdd
FROM tbvendas
WHERE deletado = 1
ORDER BY cdvdd;

-- E16
-- Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
-- As colunas presentes no resultado devem ser estado, nmpro e quantidade_media. 
-- Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

-- Observação: Apenas vendas com status concluído.
SELECT estado,
       nmpro,
       ROUND(AVG(qtd),4) AS quantidade_media
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado, nmpro
ORDER BY estado, nmpro;