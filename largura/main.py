# Fontes:
# - https://www.linkedin.com/pulse/solving-8-puzzle-using-algorithm-python-ajinkya-sonawane/
# - https://ipvs.informatik.uni-stuttgart.de/mlr/marc/teaching/14-ArtificialIntelligence/14-AI-script.pdf 

import numpy as np 
from matriz import Matriz
from movimento import Movimento
from checagem import Checagem
g = 0 # numero de movimentos
c = Checagem()
m = Matriz()
mov = Movimento()
#gera matriz aleatória
#puzzle = m.gera_matriz()


#    [[1, 2, 3], 
#     [0, 4, 6],
#     [7, 5, 8]]

#    [[0, 1, 3], 
#     [4, 2, 5],
#     [7, 8, 6]]

puzzle = np.array([[1, 5, 2], 
                   [8, 6, 3],
                   [7, 0, 4]])

    #checar se está certa ou não 
while c.check_ideal(puzzle) == False:
    if m.tem_solucao(puzzle):
    #checar as possibilidades de movimento
        lista_matrizes = m.backup_matriz(puzzle)
        movimento = c.check_movimento(puzzle, g, lista_matrizes)
        if movimento is not None:
            m.movimenta_matriz(movimento, puzzle)
            c.check_ideal(puzzle)
            g += 1
            print(f"\nMovimentos: {g}")
        else:
            print("Problema sem solução. 0 não tem mais movimentos válidos")
            break
    
    else:
        print("Problema sem solução")
