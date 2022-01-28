
from numpy.random import default_rng

from checagem import Checagem
from movimento import Movimento

check = Checagem()
mov = Movimento()

class Matriz:
    def __init__(self):
        self.lista_matriz = []

    def gera_matriz(self):
        #gera matriz aleatória entre 0 e 8 
        rng = default_rng()
        puzzle = rng.choice(range(0,9), size=(3, 3), replace=False)

        return puzzle

    def tem_solucao(self, puzzle):
        ninversao = 0
        count = 0

        #transforma matriz em lista
        puzzle_list = puzzle.flatten().tolist()

        #percorre a lista e calcula quantas inversões de valores existem
        for n in puzzle_list:
            for i in range(count,8):
                valor = puzzle_list[i+1]
                if n > valor and valor != 0:
                    ninversao += 1
            count += 1
        #se o numero de inversões for par é solucionável, se for ímpar não é solucionável                  
        if (ninversao % 2) != 0:
            return False
        else: return True

    def movimenta_matriz(self, movimento, matriz):
        # checa qual movimento deve ser feito e executa o movimento
        if movimento == 0:
            nova_matriz = mov.mov_up(matriz)
        elif movimento == 1:
            nova_matriz = mov.mov_down(matriz)
        elif movimento == 2:
            nova_matriz = mov.mov_right(matriz)
        elif movimento == 3:
            nova_matriz = mov.mov_left(matriz)
        
        # printa o puzzle depois do movimento
        print("\n_____8-PUZZLE_____\n")
        self.print_matriz(nova_matriz)
        #print(f"\nMovimentos: {g}", g)

        return nova_matriz

    def print_matriz(self, matriz):
        for row in matriz:
            print ('  '.join(map(str, row)))
    
    #faz uma lista com as todas as matrizes
    def backup_matriz(self, matriz_original):
        list_matriz = matriz_original.flatten().tolist()
        self.lista_matriz.append(list_matriz)

        return self.lista_matriz
