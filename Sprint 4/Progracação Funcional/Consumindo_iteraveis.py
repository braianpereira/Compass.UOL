# List comprehension

[elemento + 2 for elemento in [1, 2, 3, 4, 5]] # [3, 4, 5, 6, 7]

lista = [1, 2, 3, 4, 5]
lista_mais_2 = [] # Olha só, uma lista vazia, que medo

for elemento in lista:
    lista_mais_2.append(elemento + 2)

(x+2 for x in [1, 2, 3, 4, 5]) # <generator object <genexpr> at xpto>