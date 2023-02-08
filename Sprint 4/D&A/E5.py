# E5
# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV.
# Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação,
# no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.
#
# Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em
# formato textual contendo as seguintes informações:
#
# Nome do estudante
# Três maiores notas, em ordem decrescente
# Média das três maiores notas, com duas casas decimais de precisão
#
# O resultado do processamento deve ser escrito na saída padrão (print),
# ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
#
# Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
#
# Exemplo:
#
# Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
#
# Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
#
# Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
#
# round
#
# map
#
# sorted
import functools
from operator import itemgetter
from statistics import mean

arq = open('estudantes.csv')
students = arq.readlines()

arq.close()

for line in sorted(students):
    student = list(line.replace("\n", '').split(','))
    grades = sorted(map(lambda x: int(x), student[1:]), reverse=True)[:3]
    print(f"Nome: {student[0]} Notas: {grades} Média: {round(mean(map(lambda x: float(x), grades)), 2)}")
