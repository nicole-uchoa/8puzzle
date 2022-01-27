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
        self.mov_anterior = None

    def check_movimento(self, matriz, g):

        # verifica se o movimento é possível
        up = mov.up(matriz)
        down = mov.down(matriz)
        right = mov.right(matriz)
        left = mov.left(matriz)

        # faz uma lista com os pontos de cada movimento

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
        # índice correspondente a cada movimento => 0: UP, 1: DOWN, 2: RIGHT, 3: LEFT

        # o movimento que tiver a menor pontuação deve ser o movimento executado
        indice = None
        minimo = max(self.list_valor)

        indice, minimo = self.retorna_menor_valorf(indice, self.list_valor, minimo)

        if indice is None:
            movimento = self.list_valor.index(minimo)
            if self.mov_anterior is not None:
                movimento = self.evitar_loop_indice_none(
                    self.mov_anterior, movimento, minimo, self.list_valor)
        else:
            movimento = indice
            if self.mov_anterior is not None:
                movimento = self.evitar_loop_indice_not_none(
                    movimento, self.mov_anterior, self.list_valor, minimo, indice)

        self.mov_anterior = movimento

        self.list_valor = []
        return movimento

    def check_ideal(self, matriz):  # verifica se a matriz está no estado final
        if np.array_equal(matriz, self.end):
            return True
        else:
            return False

    def retorna_menor_valorf(self, indice, lista_valor, minimo):
        contador = 0

        for num in lista_valor:  # retorna o índice do menor valor da lista
            if num < minimo and num != 0:
                minimo = num
                indice = contador
            contador += 1

        return indice, minimo

    def evitar_loop_indice_none(self, mov_anterior, movimento, minimo, list_valor):

        if movimento == 0 and mov_anterior == 1:
            list_valor[movimento] = 0
            movimento = list_valor.index(minimo)
        elif movimento == 1 and mov_anterior == 0:
            list_valor[movimento] = 0

            movimento = list_valor.index(minimo)
        elif movimento == 2 and mov_anterior == 3:
            del(list_valor[movimento])
            movimento = list_valor.index(minimo)
        elif movimento == 3 and mov_anterior == 2:
            del(list_valor[movimento])
            movimento = list_valor.index(minimo)

        return movimento

    def evitar_loop_indice_not_none(self, movimento, mov_anterior, lista_valor, minimo, indice):

        if movimento == 0 and mov_anterior == 1:
            indice, minimo = self.retorna_menor_valorf(indice, lista_valor, minimo)
            movimento = indice
        elif movimento == 1 and mov_anterior == 0:
            indice, minimo = self.retorna_menor_valorf(indice, lista_valor, minimo)
            movimento = indice
        elif movimento == 2 and mov_anterior == 3:
            indice, minimo = self.retorna_menor_valorf(indice, lista_valor, minimo)
            movimento = indice
        elif movimento == 3 and mov_anterior == 2:
            indice, minimo = self.retorna_menor_valorf(indice, lista_valor, minimo)
            movimento = indice

        return movimento
