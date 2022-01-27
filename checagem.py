import numpy as np
from movimento import Movimento

mov = Movimento()


class Checagem():
    def __init__(self):
        self.score_down = 0
        self.score_up = 0
        self.score_left = 0
        self.score_right = 0
        self.list_valor = []
        self.end = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.lista_matrizes = []
    
    def check_movimento(self, matriz, g):

        up = mov.up(matriz)
        down = mov.down(matriz)
        right = mov.right(matriz)
        left = mov.left(matriz)

        if up:
            self.score_up = mov.score_mov_up(matriz, g)
            self.list_valor.append(self.score_up)
        else: 
            self.list_valor.append(0)

        if down:
            self.score_down = mov.score_mov_down(matriz, g)
            self.list_valor.append(self.score_down)
        else: 
            self.list_valor.append(0)

        if right:
            self.score_right = mov.score_mov_right(matriz, g)
            self.list_valor.append(self.score_right)
        else: 
            self.list_valor.append(0)

        if left:
            self.score_left = mov.score_mov_left(matriz, g)
            self.list_valor.append(self.score_left)
        else: 
            self.list_valor.append(0)

        # 0: UP, 1: DOWN, 2: RIGHT, 3: LEFT
        contador = 0
        indice = None
        minimo = max(self.list_valor)
        for num in self.list_valor:
            if num < minimo and num != 0:
                minimo = num
                indice = contador
            contador+=1

        if indice is None:
            movimento = self.list_valor.index(minimo)
        else: 
            movimento = indice

        self.list_valor = []
        return movimento

    def check_ideal(self, matriz):  # verifica se a matriz está no estado final
        if np.array_equal(matriz, self.end):
            return True
        else:
            return False

    

