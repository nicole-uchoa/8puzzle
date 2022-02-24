from numpy.random import default_rng

from checagem import Checagem
from movimento import Movimento

check = Checagem()
mov = Movimento()

class Matriz:
    def __init__(self):
        self.backup_matrizes = []

    def gera_matriz(self):
        #gera matriz aleatória entre 0 e 8 
        rng = default_rng()
        puzzle = rng.choice(range(0,9), size=(3, 3), replace=False)

        return puzzle

    def tem_solucao(self, puzzle):
        ninversao = 0
        count = 0
        puzzle_list = []

        for r in puzzle:
            for valor in r:
                puzzle_list.append(valor)

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

    def print_matriz(self, matriz):
        for row in matriz:
            print ('  '.join(map(str, row)))
    
    #faz uma lista com as todas as matrizes
    def backup_matriz(self, matriz_original):
        matriz_em_lista = []
        for r in matriz_original:
            for valor in r:
                matriz_em_lista.append(valor)
        
        self.backup_matrizes.append(matriz_em_lista)

        return self.backup_matrizes
