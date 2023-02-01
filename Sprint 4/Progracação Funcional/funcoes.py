# Funções como objeto de primeira classe

# Funções como objeto de primeira classe

func = lambda x: x # a função anônima, lambda, foi armazenada em uma variável

def func_2(x):
    return x + 2

lista = [func, func_2] # a variável que armazena a função foi inserida em uma estrutura, assim como uma função gerada com def

lista_2 = [lambda x: x, lambda x: x+1] # aqui as funções foram definidas dentro de uma estrutura

# Funções puras - O meio não altera o retorno com parametro igual.
valor = 5

def mais_cinco(x):
    return x + 5

assert mais_cinco(5) == 10 # True

valor = 7

assert mais_cinco(5) == 10 # True

# Funções de ordem superior (HOFs)
func = lambda x: x + 2 # uma função simples, soma mais 2 a qualquer inteiro

def func_mais_2(funcao, valor):
    """
    Função que usamos antes.
    """
    return funcao(valor) + 2

assert func_mais_2(func, 2) == 6 # true

def func_quadrada(val):
    """
    Eleva o valor de entrada ao quadrado.
    """
    return val * val

assert func_mais_2(func_quadrada, 2) == 6 # true

##  Um exemplo usando funções embutidas
def func(arg):
    return arg + 2

lista = [2, 1, 0]

list(map(func, lista)) == [4, 3, 2] # true

# Funções geradoras
# Funções geradoras são funções que nos retornam um iterável. Mas ele é lazy (só é computado quando invocado). 
# Para que uma função seja geradora, em tese, só precisamos trocar o return por yield:
def gen(lista):
    for elemento in lista:
        yield elemento

gerador = gen([1, 2, 3, 4, 5])

next(gerador) # 1
next(gerador) # 2
next(gerador) # 3
next(gerador) # 4
next(gerador) # 5
next(gerador) # StopIteration

# função geradora nos retorna um iterável que é preguiçoso. Ou seja, ele só vai efetuar a computação quando for chamado.

# Funções anônimas (lambda)
def func():
  pass

type(func) # function

lambda_func = lambda arg: arg

type(lambda_func) # function

# Uma coisa que vale ser lembrada é que funções anônimas em python só executam uma expressão. 
# Ou seja, não podemos usar laços de repetição (while, for), tratamento de exceções (try, except, finally). 
# Um simples if com uso de elif também não pode ser definido. Como sintaticamente só são aceitas expressões, 
# o único uso de um if é o ternário:

func = lambda argumento: argumento + 2 if argumento > 0 else argumento - 2
