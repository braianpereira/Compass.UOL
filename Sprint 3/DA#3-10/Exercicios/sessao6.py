# 21
# Implemente duas classes Pato e Pardal que herdem de uma classe
# Passaro a habilidade de voar e emitir som, porém, tanto Pato quanto Pardal
# devem emitir sons diferentes (de maneira escrita) no console.
#
#
#
# Imprima no console exatamente assim:
#
# Pato
# Voando...
# Pato emitindo som...
# Quack Quack
# Pardal
# Voando...
# Pardal emitindo som...
# Piu Piu

class Passaro:
    def __init__(self, nome, som):
        self.__som = som
        self.__nome = nome


    def voa(self):
        print("Voando...")

    def getNome(self):
        print(self.__nome)

    def falar(self):
        print(f"{self.__nome} emitindo som...")
        print(self.__som)


class Pato(Passaro):
    def __init__(self):
        super().__init__("Pato", "Quack Quack")

class Pardal(Passaro):
    def __init__(self):
        super().__init__("Pardal", "Piu Piu")




pato = Pato()

pato.getNome()
pato.voa()
pato.falar()

pardal = Pardal()

pardal.getNome()
pardal.voa()
pardal.falar()

# 22

# Crie uma classe Pessoa que tenha um atributo privado nome e um atributo público id.  Na sequência, adicione uma
# função que atribua um valor a nome  e uma função que retorne o valor de nome.
#
# Importante: Para atributos privados utilizamos “__” Ex: __atributo
#
# Para testar seu código use:
#
# pessoa = Pessoa(0)
# pessoa.nome = 'Fulano De Tal'
# print(pessoa.nome)

class Pessoa:
    def __init__(self, id):
        self.__id = id
        self.nome = ""


pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)

# 23

# Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y,
# e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração,
# que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).
#
# Utilize os valores abaixo para testar seu exercício:
#
# x = 4
# y = 5
# imprima:
#
# Somando: 4+5 = 9
# Subtraindo: 4-5 = -1


class Calculo:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y


x = 4
y = 5

calculo = Calculo()

som = calculo.soma(x, y)
sub = calculo.subtracao(x, y)

print(f"Somando:{x}+{y} = {som}")
print(f"Subtraindo:{x}-{y} = {sub}")

# 24

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

