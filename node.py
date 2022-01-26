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





# def euclidianCost(puzzle): # calcula distancia euclidiana
#     cost = 0
#     for row in range(len(puzzle)):
#         for col in range(len(puzzle[0])):
#             pos = get_pos(END, puzzle[row][col])
#             cost += abs(row - pos[0]) + abs(col - pos[1])
#     return cost


# def get_pos(current_state, element):
#     for row in range(len(current_state)):
#         if element in current_state[row]:
#             return (row, current_state[row].index(element))

# print(euclidianCost(puzzle))





#def possible_mov():


