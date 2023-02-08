# E3
import functools

# A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários.
# Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito).
#
# Abaixo apresentando uma possível entrada para a função.

# lancamentos = [
#     (200,'D'),
#     (300,'C'),
#     (100,'C')
# ]

# A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos.
# Na lista anterior, por exemplo, teríamos como resultado final 200.
#
# Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:

## reduce (módulo functools)
## map


import functools


def calcula_saldo(lancamentos) -> float:
    return functools.reduce(lambda a, b: a + b, list(map(lambda x: x[0] * -1 if x[1] == 'D' else x[0], lancamentos)))


lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

print(calcula_saldo(lancamentos))
