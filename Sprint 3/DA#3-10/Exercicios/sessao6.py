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

