#map()
# fazendo um gancho com o tópico anterior, é uma função de mapeamento, 
# contudo, ela recebe o iterável em conjunto a uma função, a que fará o mapeamento

def func(x):
    """
    Exemplo do tópico passado
    """
    return x +2

list(map(func, [1,2,3])) # [3, 4, 5]

# Uma lista de listas, isso em python também é uma matriz
lista = [[1,2], [2,3], [3,4], [4,5], [5,6]]

def func(x):
    """
    Retorna a mesma coisa que entrou
    """
    return x

list(map(func, lista))

# Uma lista de listas, isso em python também é uma matriz
lista = [[1,2], [2,3], [3,4], [4,5], [5,6]]

def func_rev(x):
    """
    Retorna a lista que entrou, porém invertida
    """
    return list(reversed(x))

list(map(func_rev, lista)) # [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5]]

#  que fizemos agora é uma composição de funções, mas dentro de um map(). 
# A notação matemática disso, caso você tenha curiosidade em saber é:
### uma função comum = f(x)

### composição de funções = f(g(x))

#############################################################################################################
###  Funções de ordem superior são funções que recebem funções como argumento, ou retornam outra funções. ###
#############################################################################################################

# max()
# A função max() é uma função de redução, e sem a função como parâmetro, ela vai ter o 
# comportamento das funções que vimos no outro tópico.
max([1, 2, 3, 4, 5]) # 5

# Se essa lista for uma lista de listas, como prosseguir?
lista = [[1,2], [2,3], [3,4], [4,5], [5,6]]

max(lista) # [5, 6]

lista = [[7,2], [5,3], [5,4], [5,5], [5,6]]

max(lista) # [7, 2]
# [7, 2] é um bom resultado, mas vamos pensar que o que eu queria eram as somas dois dois elementos, 
# nesse caso o resultado veio errado. 7 + 2 = 9 quando 5 + 6 = 11. Vamos tentar outra vez:

lista = [[7,2], [5,3], [5,4], [5,5], [5,6]]

def func(x):
    return x[0] + x[1]

max(lista, key=func) # [5,6]

lista = [[7,2], [5,3], [5,4], [5,5], [5,6]]

max(lista, key=sum) # [5, 6]

# Como você já sabe compor funções, vamos imaginar que nossa sequência de 
# entrada poderia ser maior que dois elementos, uma maneira bonita de fazer 
# isso seria usar o sum(). Fica muito mais elegante.

# min()

# A função min() é a função equivalente a max(). Quando a max() pega o maior item da sequência, 
# min() pega o menor.
lista = [[7,2], [5,3], [5,4], [5,5], [5,6]]

min(lista, key=sum) # [5, 3]

# iter()
# A função embutida iter() tem duas formas, a primeira devolve o iterável de uma sequência.
lista = [1, 2, 3, 4, 5]

iter(lista) # <list_iterator at xpto>

"""
Exemplo roubado do Steven Lott
"""
lista = [1, 2, 3, 4, 5]

list(iter(lista.pop, 3)) #[5, 4]

# Como passamos como callable pop() e se pop() for chamado sem argumentos, 
# ele retorna o último elemento da lista e retira ele da mesma. 
# Nesse caso o sentinela é 3. Então ele vai desmontando a lista e 
# gerando um novo iterável de tudo que foi removido da lista anterior

## (1) lista = [1, 2, 3, 4, 5]
## (2) saida = []
## (3) saida.append(lista.pop())
## (4) print(saida) # [5]

# Agora que o pop_append ficou claro, deu pra entender o que faz a segunda forma da função iter()? Sim, deu.
# Então vamos explorar um exemplo mais eficiente, o da documentação:
with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        print(line) # só essa linha foi modificada

# O método readline, quando passado sem parâmetros efetua a leitura de um único caracter. 
# Nesse caso ele printaria uma letra do arquivo por linha. Mas, como usamos iter(fp.readline, '') 
# ele vai nos retornar uma sequência de strings até que o sentinela que no caso é vazio apareça.

# Ou seja, é passado um objeto com um método no lugar de uma função. 
# O método tem suas particularidades como não precisar de argumentos e 
# agir no objeto em si. Isso parece óbvio, porém, quando construímos nossas próprias classes, 
# o retorno pode não ser o esperado, como nas sequências embutidas do python.

# sorted()
# Para os viciados em listas, como eu, o método sort da lista funciona bem, 
# apesar de ordenar a lista e não trazer uma nova lista, o que as vezes é uma dor de cabeça.
lista = [1, 2, 3, 3, 2, 1]

lista.sort()

print(lista) # [1, 1, 2, 2, 3, 3]
# Para agradar a todos, temos a função embutida sorted().Assim como as outras HOFs, 
# temos o parâmetro opcional key e podemos decidir como a ordenação será feita.

# Vamos pensar em uma tupla de tuplas, uma saída de um banco, por exemplo:
autores = (('Fernando Pessoa', 17, 'Portugal'),
           ('Carlos Drummond Andrade', 14, 'Brasil'),
           ('Nenê Altro', 4, 'Brasil'))

# sorted(autores)

#[('Carlos Drummond Andrade', 14, 'Brasil'),
# ('Fernando Pessoa', 17, 'Portugal'),
# ('Nenê Altro', 4, 'Brasil')]

# Até então, tudo certo. Ele ordenou pelo index 0 da tupla, 
# que nesse caso eram os nomes. Vamos tentar usar a magia da key agora:
sorted(autores, key=lambda x: x[1])

#[('Nenê Altro', 4, 'Brasil'),
# ('Carlos Drummond Andrade', 14, 'Brasil'),
# ('Fernando Pessoa', 17, 'Portugal')]

# Nesse caso, a ordenação foi dada pelo index 1, que foi o que nós determinamos na função lambda, vamos tentar mais um caso:
sorted(autores, key=lambda x: x[0][-1])

# [('Fernando Pessoa', 17, 'Portugal'),
# ('Carlos Drummond Andrade', 14, 'Brasil'),
# ('Nenê Altro', 4, 'Brasil')]

# Nesse caso ele fez a ordenação pelo index 0, só que invertido.

# Mas não paramos por aí. sorted() ainda tem mais um argumento escondido, reverse, 
# que por padrão vem sempre False. Mas podemos pedir o True dele:

sorted(autores, key=lambda x: x[0][-1], reverse=True)

#[('Nenê Altro', 4, 'Brasil'),
# ('Carlos Drummond Andrade', 14, 'Brasil'),
# ('Fernando Pessoa', 17, 'Portugal')]

# E agora obtivemos o mesmo resultado, só que invertido.

# Só pra não dizer que não falei das flores. No lugar desse lambda que não é muito bonito, 
# existe uma função bem bonita no módulo operator chamada itemgetter():
from operator import itemgetter

sorted(autores, key=itemgetter(1))

#[('Nenê Altro', 4, 'Brasil'),
# ('Carlos Drummond Andrade', 14, 'Brasil'),
# ('Fernando Pessoa', 17, 'Portugal')]

# filter()
# filter() não é uma função nem de mapeamento, nem de redução. filter() é uma função de filtragem.
lista = [1, 2, 3, 4, 5]

impares = lambda x: x % 2

filter(impares, lista) # [1, 3, 5]