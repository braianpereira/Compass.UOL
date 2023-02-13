import hashlib as hlib

salt = 'Arroz Para Todos Que Tem Fome'

while True:
    plain = input('Informe uma mensagem: ')
    encripted = hlib.sha1(plain.encode() + salt.encode())
    print(encripted.hexdigest())