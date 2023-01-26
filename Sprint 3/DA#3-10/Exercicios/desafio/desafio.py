# Armazene o arquivo actors.csv dentro de uma nova pasta, após isso crie 5 arquivos do tipo “txt”
# vazios (1 para cada exercício do desafio).
#
# Em seguida para cada uma das tarefas da sequencia, leia o arquivo actors.csv
# utilizando Python como linguagem de programação e depois de obter as repostas
# necessárias armazene cada um dos resultados em um dos arquivos “txt” criados.

# Pontos de Atenção:
#
# Para desenvolvimento deste exercício, não deve ser utilizado as bibliotecas Pandas
# e NumPy e/ou outras bibliotecas e engines que utilizam de dataframes.
#
# Todas as transformações que julgarem necessárias, devem ser feitas utilizando os scripts Python e
# nenhuma modificação deve ser feita no arquivo actors.csv
#
# Para leitura do arquivo actors.csv, não deve ser utilizado o módulo csv nativo do Python.
#
# Perguntas dessa tarefa
# O ator/atriz com maior número de filmes e o respectivo número de filmes.
#
# A média do número de filmes por autor.
#
# O ator/atriz com a maior média por filme.
#
# O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
#
# A lista dos Autores ordenada por pagamento. Do mais bem pago para o menos bem pago
import re


class Csv:
    def __init__(self):
        self.__data = ""

    def load_file(self):
        arq = open("actors.csv", "r")

        self.__data = arq.readlines()

        lista = []
        for a in self.__data[1:]:
            lista.append(re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", a.replace('\n', '')))

        self.__data = lista

        arq.close()

    def save_to_file(self, file_name, data):
        arq = open(file_name, 'w')
        arq.write(f"{data}")
        arq.close()

    def debug_print_data(self):
        for a in self.__data:
            print(a)

    # O ator/atriz com maior número de filmes e o respectivo número de filmes.
    def actor_with_bigger_films_count(self):
        actors_dict = dict(zip([row[0] for row in self.__data], [int(row[2]) for row in self.__data]))

        actor = max(actors_dict, key=actors_dict.get)
        films_cont = actors_dict[actor]

        self.save_to_file("1.txt", f"{actor}, {films_cont}")

    # A média do número de filmes por autor.
    def actors_avarege_films(self):
        total_films = len(self.__data)
        actors_dict = dict(zip([row[0] for row in self.__data], [row[2] for row in self.__data]))
        avg = sum([float(value) for value in actors_dict.values()]) / total_films

        self.save_to_file("2.txt", f"{avg}")

    # A média do número de filmes por autor.
    def highest_average_actor(self):
        actors_dict = dict(zip([row[0] for row in self.__data], [float(row[3]) for row in self.__data]))

        actor = max(actors_dict, key=actors_dict.get)

        self.save_to_file("3.txt", f"{actor}")

    # O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
    def most_frequent_films(self):
        films_dict = dict.fromkeys([row[4] for row in self.__data], 0)

        for row in self.__data:
            films_dict[row[4]] += 1

        film = max(films_dict, key=films_dict.get)
        frequency = films_dict[film]

        to_file = ""

        for index, f in films_dict.items():
            if f == frequency:
                to_file += f'{index}, {frequency}\n'

        self.save_to_file("4.txt", to_file)

    # A lista dos Autores ordenada por pagamento. Do mais bem pago para o menos bem pago
    def actors_by_gross(self):
        actors_dict = dict(zip([row[0] for row in self.__data], [float(row[5]) for row in self.__data]))

        res = {key: val for key, val in sorted(actors_dict.items(), key=lambda ele: ele[1], reverse=True)}

        to_file = ""

        for index, f in res.items():
            to_file += f'{index}\n'

        self.save_to_file("5.txt", to_file)


csv = Csv()
csv.load_file()

csv.actor_with_bigger_films_count()
csv.actors_avarege_films()
csv.highest_average_actor()
csv.most_frequent_films()
csv.actors_by_gross()