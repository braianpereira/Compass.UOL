# E2

# Utilizando high order functions, implemente o corpo da função conta_vogais.
# O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

def conta_vogais(texto: str) -> int:
    return len(list(filter(lambda x: x in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'), texto)))