# __getitem__
# O padrão de projeto iterator em python já vem implementado por padrão, 
# como já foi dito antes. Basta que um objeto tenha os métodos __iter__ ou __getitem__ 
# para que um laço possa ser utilizado.

class iteravel:
    """
    Um objeto que implementa o `__getitem__` pode ser acessado por posição
    """
    def __init__(self, sequencia):
        self.seq = sequencia

    def __getitem__(self, posicao):
        """
        Por exemplo, quando tentamos acessar um elemento da sequência usando
        slice:
            >>> iteravel[2]

        O interpretador python chama o __getitem__ do objeto e nos retorna
            a posição solicitada

        um exemplo:
        IN: lista = [1, 2, 3, 4]
        IN: lista[0]
        OUT: 1
        """
        return self.seq[posicao]

# __iter__
# Agora os objetos que implementam __iter__ tem algumas peculiaridades. 
# Por exemplo, quando o iterável (vamos pensar no for) chamar a sequência, ela vai pedir o __iter__ 
# que vai retornar uma instância de si mesmo para o for e ele vai chamar o __next__ até que a exceção 
# StopIteration aconteça.

# Uma classe que implementa __iter__:
class iteravel:
    def __init__(self, sequencia):
       self.data = sequencia

    def __next__(self):
        """
        Neste caso, como o método pop do objeto data é chamado
            (vamos pensar em uma lista) ele vai retornar o primeiro elemento
            (o de index 0) e vai remove-lo da lista

        E quando a sequência estiver vazia ele vai nos retornar um StopIteration
            O que vai fazer com que a iteração acabe.

        Porém, estamos iterando com pop, o que faz a nossa iteração ser a única,
            pois ela não pode ser repetida, dado que os elementos foram
            removidos da lista
        """
        if not self.sequencia:
           raise StopIteration
        return self.sequencia.pop()

    def __iter__(self):
        return self