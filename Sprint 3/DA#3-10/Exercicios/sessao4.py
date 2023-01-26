# 5
# Dada duas listas como as no exemplo abaixo:
# a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Escreva um programa que retorne o que ambas as listas têm em comum (sem repetições). 
# O seu programa deve funcionar para listas de qualquer tamanho.
def estaNoArray(arr, numero):
    for i in arr:
        if numero == i:
            return True
    return False

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

c = []

for i in b:
    if estaNoArray(a, i):
        if not estaNoArray(c,i):
            c.append(i)

print(c)

# 7
# Dada a seguinte lista:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Faça um programa que gere uma nova lista contendo apenas números ímpares.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 == 1]

print(b)

# 8
# Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
# Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
a = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in a:
    if palavra == palavra[::-1]:
        print("A palavra:", palavra ,"é um palíndromo")
    else:
        print("A palavra:", palavra, "não é um palíndromo")

# 9
# Dada as listas a seguir:
# primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
# sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
# idades = [19, 28, 25, 31]
#Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos"
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, pNome, sNome, idade in zip(range(len(idades)), primeirosNomes, sobreNomes, idades):
    print("{} - {} {} está com {} anos".format(i, pNome, sNome, idade))

# 10
# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.
# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
def unicosNaLista(lista):
    lista.sort()
    return list(set(lista))

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

print(unicosNaLista(lista))

# 11
# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
# Dica: leia a documentação da função open(...)
arq = open("arquivo_texto.txt", "r")

print(arq.read())

arq.close()

# 12
# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
# Dica: leia a documentação do pacote json
import json 

f = open('person.json')
  
data = json.load(f)
  
print(data)

f.close()

# 13
# Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. 
# Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.
# Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.
def my_map(lista, f):
    list1 = list(map(lambda x: f(x), lista))
    return list1


def potencia(num):
    return num**2

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_map(a, potencia))

# 14
# Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros 
# nomeados e imprime o valor de cada parâmetro recebido.

# Teste sua função com os seguintes parâmetros:

# (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
def func(*args, **kwargs):
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(value)


func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

# 15
# Implemente a classe Lampada. 
# A classe Lâmpada recebe um booleano no seu construtor, 
# True se a lâmpada estiver ligada,
#  False caso esteja desligada. 
# A classe Lampada possuí os seguintes métodos:

# liga(): muda o estado da lâmpada para ligada
# desliga(): muda o estado da lâmpada para desligada
# esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
# Para testar sua classe:
# Ligue a Lampada
# Imprima: A lâmpada está ligada? True
# Desligue a Lampada
# Imprima: A lâmpada ainda está ligada? False
class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return str(self.ligada)


lampada = Lampada(True)

lampada.liga()
print(f"A lâmpada está ligada? {lampada.esta_ligada()}")
lampada.desliga()
print(f"A lâmpada ainda está ligada? {lampada.esta_ligada()}")


# 16
# Escreva uma função que recebe uma string de números separados por 
# vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.
# A string deve ter valor  "1,3,4,6,10,76"
text = "1,3,4,6,10,76"

lista = text.split(",")

soma = sum([int(x) for x in lista])

print(soma)

# 17
# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: 
# a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def divideEmTres(seq):
    avg = len(seq) / float(3)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

listas = divideEmTres(lista)

print(f"{listas[0]} {listas[1]} {listas[2]}")

# 18
# Dado o dicionário a seguir:

# speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

# Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

uniao = set(speed.values()) & set(speed.values())
print(list(uniao))

# 19
# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:

# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
# import random
# # amostra aleatoriamente 50 números do intervalo 0...500
# random_list = random.sample(range(500),50)

# Use as variáveis abaixo para representar cada operação matemática

# mediana
# media
# valor_minimo
# valor_maximo
import random

random_list = random.sample(range(500), 50)


def calcula_mediana(lista):
    lista.sort()
    total = len(lista)
    elemento_central = round(total / 2) - 1
    if total % 2 == 0:
        return (lista[elemento_central] + lista[elemento_central+1]) / 2
    else:
        return lista[elemento_central]


def calcula_media(lista):
    soma = sum(lista)
    return soma / len(lista)


def maior_valor(lista):
    lista.sort()
    return lista[len(lista)-1]


def menor_valor(lista):
    lista.sort()
    return lista[0]

mediana = calcula_mediana(random_list)
media = calcula_media(random_list)
valor_minimo = menor_valor(random_list)
valor_maximo = maior_valor(random_list)

# 24
# Crie uma classe Ordenadora que contenha um atributo listaBaguncada e
# contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.
#
# Instancie um objeto chamado crescente dessa classe Ordenadora que tenha
# como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto,
# decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].
#
# Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método
#
# ordenacaoDecrescente.
#
# Imprima o resultado da ordenação crescente e da ordenação decresce
#
# [1, 2, 3, 4, 5]
# [9, 8, 7, 6]


class Ordenadora:
    def __init__(self, lista):
        self.listaBaguncada = lista

    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada

    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort()
        self.listaBaguncada.reverse()
        return self.listaBaguncada


crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())

# 25
# Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.
# Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.
# Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
# Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
# “O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.
# Sendo x, y, z e w cada um dos atributos da classe “Avião”.

# Valores de entrada:
# modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul
# modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul
# modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul

class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.capacidade = capacidade
        self.velocidade_maxima = float(velocidade_maxima)
        self.modelo = modelo
        self.cor = "Azul"

    def print(self):
        print(f"O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, "
              f"capacidade para {self.capacidade} passageiros e é da cor {self.cor}")


aviao = [
    Aviao("BOIENG456", 1500, 400),
    Aviao("Embraer Praetor 600", 863, 14),
    Aviao("Antonov An-2", 258, 12)
]

for x in aviao:
    x.print()