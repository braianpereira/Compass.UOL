# E1

# Você está recebendo um arquivo contendo 10.000 números inteiros,
# um em cada linha. Utilizando lambdas e high order functions,
# apresente os 5 maiores valores pares e a soma destes.

arq = open('number.txt', "r")

numbers = arq.read()

arq.close()

numbers = sorted(filter(lambda x: not (x % 2), map(lambda x: int(x), numbers.split("\n"))), reverse=True)[:5]

print(list(numbers))

print(sum(numbers))