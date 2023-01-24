# 1
# Escreva um código Python que imprime o nome e a idade do João de 37 anos e 
# imprime o ano em que ele completará 100 anos.

# Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem'). 
# Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.
name = "João"
idade = '37'
ano = 2022 + 100 - int(idade)
print (ano)

# 2
# Escreva um código Python que verifica se os números 0, 7851 e 9 elevado na potência 3  são pares ou ímpares. 
# Para cada número, imprima o Par: ou Ímpar: e o número correspondente.
import math

list = [0, 7851, math.pow(9,3)]

for numero in list:
    if numero % 2 == 0:
        print("Par:", int(numero))
    else:
        print("Ímpar:", int(numero))

# 3
# Escreva um código Python que imprime os números pares de 0 até 20 (incluso).
# Dica: olhe a documentação da função range().

for i in range(0, 21, 2):
    print(int(i))

# 4
# Escreva um código Python que imprime todos os números primos de 0 até 100.
def primo(n):
    for val in range(2,n):
        if n % val == 0:
            return False

    return True
        

n = 100
for val in range(2,n+1):
    if(primo(val)):
        print(val)

# 5
# Escreva um código Python que tem 3 variáveis dia (22), mês(10) e ano(2022) e imprime a data completa no formato a seguir:
# Exemplo: 22/10/2022
dia = 22
mes = 10
ano = 2022

print(str(dia) + "/" + str(mes) + "/" + str(ano))

