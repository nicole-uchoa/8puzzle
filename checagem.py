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
    
    def check_movimento(self, matriz, g, lista_matrizes):
        self.list_valor = []

        up = mov.up(matriz, lista_matrizes)
        down = mov.down(matriz, lista_matrizes)
        right = mov.right(matriz, lista_matrizes)
        left = mov.left(matriz, lista_matrizes)

        self.list_valor = self.monta_lista_movimentos(up, down, right, left, matriz, g)

        # 0: UP, 1: DOWN, 2: RIGHT, 3: LEFT
        movimento = self.retorna_movimento(self.list_valor)

        lista_novos_movimentos = self.teste_matriz_valida(movimento, matriz, lista_matrizes, self.list_valor)

        if set(self.list_valor) !=  set(lista_novos_movimentos):
            movimento = self.retorna_movimento(lista_novos_movimentos)

        return movimento #CHECAR MATRIZ

    def check_ideal(self, matriz):  # verifica se a matriz está no estado final
        if np.array_equal(matriz, self.end):
            return True
        else:
            return False

    def backup_matriz(self, matriz_original):
       list_matriz = matriz_original.flatten().tolist()
       self.lista_matrizes.append(list_matriz)

       return self.lista_matrizes

    def check_matrizes_iguais(self, matriz, lista_matrizes):
        matriz = matriz.flatten().tolist()

        if matriz in lista_matrizes: return True
        else: return False

    def teste_matriz_valida(self, movimento, matriz, lista_matrizes, list_valor):
        if movimento == 0:
            matriz_teste = mov.mov_up(matriz)
            if self.check_matrizes_iguais(matriz, lista_matrizes):
                list_valor[movimento] = 0
            matriz_teste = mov.mov_down(matriz)
            
            
        elif movimento == 1:
            matriz_teste = mov.mov_down(matriz)
            if self.check_matrizes_iguais(matriz, lista_matrizes):
                list_valor[movimento] = 0 
            matriz_teste = mov.mov_up(matriz)
            

        elif movimento == 2:
            matriz_teste = mov.mov_right(matriz)
            if self.check_matrizes_iguais(matriz, lista_matrizes):
                list_valor[movimento] = 0
            matriz_teste = mov.mov_left(matriz)
            
        
        elif movimento == 3:
            matriz_teste = mov.mov_left(matriz)
            if self.check_matrizes_iguais(matriz, lista_matrizes):
                list_valor[movimento] = 0
            matriz_teste = mov.mov_right(matriz)

        return list_valor

    def retorna_movimento(self, list_valor):
        contador = 0
        indice = None
        minimo = max(list_valor)
        for num in list_valor:
            if num < minimo and num != 0:
                minimo = num
                indice = contador
            contador+=1

        if indice is None:
            movimento = self.list_valor.index(minimo)
        else: 
            movimento = indice

        return movimento

    def monta_lista_movimentos(self, up, down, right, left, matriz, g):
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

        return self.list_valor