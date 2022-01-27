import numpy as np

END = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

class Node:
    #def __init__(self, no_atual, no_anterior, g, h, dir): # h = numero de peças mal colocadas | g = numero de nos percorridos
    def __init__(self, g):
        self.g = g

    def f(self, g, h):
        return g + h

    def get_score_h(self, matriz):
        countf = 0
        countr = 0
        countc = 0
        for row in matriz:
            while countc < 3:
                for elemento in row:
                    if elemento != END[countr][countc] and elemento != 0:
                        countf += 1
                    countc += 1
            countc = 0
            countr += 1

        return countf

    def sum_score_g(self, g):
        self.g += 1
        return self.g




