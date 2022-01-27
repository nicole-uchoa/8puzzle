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
# [[1, 2, 3], 
#                  [0, 4, 6],
#                  [7, 5, 8]]
puzzle = np.array([[1, 2, 3], 
                 [4, 0, 5],
                 [6, 7, 8]])

if m.tem_solucao(puzzle): 
    #checar se está certa ou não 
    while c.check_ideal(puzzle) == False:
        #checar as possibilidades de movimento
        movimento = c.check_movimento(puzzle, g)
        puzzle, puzzle_original = m.movimenta_matriz(movimento, puzzle)
        
        c.check_ideal(puzzle)
        g += 1

        # if g > 15:
        #     print("Problema sem solução")

        #     break


    
    print("\n_____8-PUZZLE COMPLETO_____\n")
    m.print_matriz(puzzle)
    print(f"\nMovimentos: {g}")
        
else:
    print("Problema sem solução")
