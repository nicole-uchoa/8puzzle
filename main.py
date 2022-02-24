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

# mais rápido = [[1, 2, 3], [0, 4, 6],[7, 5, 8]]
# [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
# [[2, 5, 3], [1, 6, 8], [4, 7, 0]]
# end = [[1, 2, 3], [8, 0, 4], [7, 6, 5]] => [[2, 8, 1],[0, 4, 3],[7, 6, 5]] (segundo o método de inversões não tem solução, mas tem)

puzzle = [[2, 5, 3], [1, 6, 8], [4, 7, 0]]

m.print_matriz(puzzle)


if m.tem_solucao(puzzle): 
#checar se está certa ou não 
    while c.check_ideal(puzzle) == False:
        #checar as possibilidades de movimento
        lista_matrizes = m.backup_matriz(puzzle)
        movimentos_possiveis = mov.movimentos_possiveis(puzzle)
        # checar quais movimentos validos
        movimentos_possiveis_validado = c.checa_movimento_valido(puzzle, movimentos_possiveis, lista_matrizes)
        pontos_movimentos = mov.monta_lista_movimentos(movimentos_possiveis_validado, puzzle, g)
        movimento_ideal = mov.retorna_movimento_ideal(pontos_movimentos) 
        novo_puzzle = mov.movimenta(movimento_ideal, puzzle)
        pontos_movimentos.clear()
        # printa o puzzle depois do movimento
        print("\n_____8-PUZZLE_____\n")
        m.print_matriz(novo_puzzle)
        c.check_ideal(puzzle)
        g += 1

    print("\n_____8-PUZZLE COMPLETO_____\n")
    m.print_matriz(puzzle)
    print(f"\nMovimentos: {g}")
    
else:
    print("Problema sem solução")
