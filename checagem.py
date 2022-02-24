import numpy as np
from movimento import Movimento

mov = Movimento()

class Checagem():
    def __init__(self):
        self.score_down = 0
        self.score_up = 0
        self.score_left = 0
        self.score_right = 0
        self.end = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#        self.end = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
        self.lista_matrizes = []


    def check_ideal(self, matriz):  # verifica se a matriz está no estado final
        if np.array_equal(matriz, self.end):
            return True
        else:
            return False

    def backup_matriz(self, matriz_original):
       list_matriz = matriz_original.flatten().tolist()
       self.lista_matrizes.append(list_matriz)

       return self.lista_matrizes

    def checa_movimento_valido(self, matriz, lista_movimentos, lista_backup_matrizes):
        for index in range(4):
            if lista_movimentos[index] == 1:
                matriz_teste_lista =[]
                matriz_teste = mov.movimenta(index, matriz)
                for r in matriz_teste:
                    for valor in r:
                        matriz_teste_lista.append(valor)

                # retornar matriz para estado de inicio
                if index == 0:
                    matriz_teste = mov.movimenta(1, matriz)
                if index == 1:
                    matriz_teste = mov.movimenta(0, matriz)
                if index == 2:
                    matriz_teste = mov.movimenta(3, matriz)
                if index == 3:
                    matriz_teste = mov.movimenta(2, matriz)

                if matriz_teste_lista in lista_backup_matrizes:
                    lista_movimentos[index] = 0
    
        return lista_movimentos                

    

    
