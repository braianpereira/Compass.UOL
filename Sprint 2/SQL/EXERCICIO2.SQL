/* Considerando o que vc aprendeu sobre performance, resolva os exercicios abaixo */

SELECT COUNT(*) FROM FUNCIONARIOS;

--Traga os funcionarios que trabalhem
--no departamento de filmes OU no
--departamento de roupas

-- 21 | Filmes   53 | Roupas

--Como estamos trabalhando com OR e a segunda condicao é opcional
--colocamos na primeira condicao quem tem mais chances de uma saida
--verdadeira, pois a segunda condicao nao será checada nesse caso.

select * from funcionarios
where departamento = 'Roupas'
or
departamento = 'Filmes';

SELECT COUNT(*), departamento
FROM FUNCIONARIOS
group by departamento;

SELECT COUNT(*), departamento
FROM FUNCIONARIOS
group by departamento
order by 1;

WHERE DEPARTAMENTO = 'Filmes' OR DEPARTAMENTO = 'Roupas'

--O gestor de marketing pediu a lista das funcionarias (AS) = FEMININO que trabalhem no departamento 
--de filmes ou no departamento lar. Ele necessita enviar um email para as colaboradoras
--desses dois setores. OR +  AND *

--Feminino 491 ocorrencias
select count(*), sexo
from funcionarios
group by sexo;

--52 | Lar  21 Filmes
select count(*), departamento
from funcionarios
group by departamento;

SELECT * FROM FUNCIONARIOS
WHERE
( DEPARTAMENTO = 'Lar' AND SEXO = 'Feminino' )
OR
( DEPARTAMENTO = 'Filmes' AND SEXO = 'Feminino' );

--Traga os funcionarios do sexo masculino
--ou os funcionarios que trabalhem no setor Jardim

SELECT * FROM FUNCIONARIOS
WHERE
SEXO = 'Masculino' OR
DEPARTAMENTO = 'Jardim';




