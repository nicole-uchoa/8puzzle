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
        backup_list = []
        up = mov.up(matriz, lista_matrizes)
        down = mov.down(matriz, lista_matrizes)
        right = mov.right(matriz, lista_matrizes)
        left = mov.left(matriz, lista_matrizes)

        self.list_valor = self.monta_lista_movimentos(up, down, right, left, matriz, g)

        # 0: UP, 1: DOWN, 2: RIGHT, 3: LEFT
        movimento = self.retorna_movimento(self.list_valor)
        if len(lista_matrizes) != 1:
            for valor in self.list_valor:
                backup_list.append(valor)

            for item in range(3):
                lista_novos_movimentos = self.teste_matriz_valida(movimento, matriz, lista_matrizes, self.list_valor)
                if lista_novos_movimentos == [0, 0, 0, 0]:
                    movimento = None
                else:
                    validacao = (backup_list == lista_novos_movimentos)
                    if validacao == False:
                        movimento = self.retorna_movimento(lista_novos_movimentos)
                

        return movimento #CHECAR MATRIZ

    def check_ideal(self, matriz):  # verifica se a matriz está no estado final
        if np.array_equal(matriz, self.end):
            return True
        else:
            return False

    # def backup_matriz(self, matriz_original):
    #    list_matriz = matriz_original.flatten().tolist()
    #    self.lista_matrizes.append(list_matriz)

    #    return self.lista_matrizes

    def check_matrizes_iguais(self, matriz, lista_matrizes):
        matriz_em_lista = matriz.flatten().tolist()

        if matriz_em_lista in lista_matrizes: return True
        else: return False

    def check_zero_invalido(self, matriz, lista_matrizes):
        countRow = 0
        countC = 0
        for row in matriz:
            while countC < 3:
                for elemento in row:
                    if elemento == 0:
                        indexCol = countC
                        indexRow = countRow
                    countC += 1
            countRow += 1
            countC = 0
        for r in range(len(lista_matrizes)-1):
            for c in range(len(lista_matrizes[r])-1):
                if lista_matrizes[r][c] == matriz[indexRow][indexCol]:
                    validade = True
                else: 
                    validade = False
        
        return validade

    def teste_matriz_valida(self, movimento, matriz, lista_matrizes, list_valor):
        if movimento == 0:
            mov.mov_up(matriz)
            if self.check_matrizes_iguais(matriz, lista_matrizes) or self.check_zero_invalido(matriz, lista_matrizes):
                list_valor[movimento] = 0
            mov.mov_down(matriz)
            
            
        if movimento == 1:
            mov.mov_down(matriz)
            if self.check_matrizes_iguais(matriz, lista_matrizes) or self.check_zero_invalido(matriz, lista_matrizes):
                list_valor[movimento] = 0 
            mov.mov_up(matriz)
            

        if movimento == 2:
            mov.mov_right(matriz)
            if self.check_matrizes_iguais(matriz, lista_matrizes) or self.check_zero_invalido(matriz, lista_matrizes):
                list_valor[movimento] = 0
            mov.mov_left(matriz)
            
        
        if movimento == 3:
            mov.mov_left(matriz)
            if self.check_matrizes_iguais(matriz, lista_matrizes) or self.check_zero_invalido(matriz, lista_matrizes):
                list_valor[movimento] = 0
            mov.mov_right(matriz)

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