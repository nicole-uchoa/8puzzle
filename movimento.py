from adicionais import add_matriz_lista_matrizes, check_matrizes_iguais
from node import Node

class Movimento:        

    ###############################################
    ##### VERIFICAR SE O MOVIMENTO É POSSÍVEL #####
    ###############################################    
    def up(self, matriz): # se o índice da linha for diferente de 0 o espaço em branco (zero) pode ser movido para cima
        countRow = 0
        for row in matriz:
            for elemento in row:
                if elemento == 0:
                    indexRow = countRow
            countRow += 1
        
        if indexRow != 0:
            matriz_atual, matriz_original = self.mov_up(matriz)
            # adicionar matriz original na lista de matrizes => backup matrizes
            add_matriz_lista_matrizes(matriz_original)

            # desfazendo o movimento 
            self.mov_down(matriz_atual)

            # verificar se matriz existe na lista de matrizes
            if check_matrizes_iguais(matriz_atual): 
                return False
            else: 
                return True             
        else: 
            return False

    def down(self, matriz): # se o índice da linha for diferente de 2 o espaço em branco (zero) pode ser movido para baixo
        countRow = 0
        for row in matriz:
            for elemento in row:
                if elemento == 0:
                    indexRow = countRow
            countRow += 1
        
        if indexRow != 2:
            matriz_atual, matriz_original = self.mov_down(matriz)
            # adicionar matriz original na lista de matrizes => backup matrizes
            add_matriz_lista_matrizes(matriz_original)
            
            # desfazendo o movimento 
            self.mov_up(matriz_atual)

            # verificar se matriz existe na lista de matrizes
            if check_matrizes_iguais(matriz_atual): 
                return False
            else: 
                return True             
        else: 
            return False

    def left(self, matriz): # se o índice da coluna for diferente de 0 o espaço em branco (zero) pode ser movido para cima
        countC = 0
        for row in matriz:
            while countC < 3:
                for elemento in row:
                    if elemento == 0:
                        indexCol = countC
                    countC += 1
            countC = 0
        
        if indexCol != 0:
            matriz_atual, matriz_original = self.mov_left(matriz)
            # adicionar matriz original na lista de matrizes => backup matrizes
            add_matriz_lista_matrizes(matriz_original)
            
            # desfazendo o movimento 
            self.mov_right(matriz_atual)

            # verificar se matriz existe na lista de matrizes
            if check_matrizes_iguais(matriz_atual): 
                return False
            else: 
                return True             
        else: 
            return False

    def right(self, matriz): # se o índice da coluna for diferente de 0 o espaço em branco (zero) pode ser movido para cima
        countC = 0
        for row in matriz:
            while countC < 3:
                for elemento in row:
                    if elemento == 0:
                        indexCol = countC
                    countC += 1
            countC = 0

        if indexCol != 2:
            matriz_atual, matriz_original = self.mov_right(matriz)
            # adicionar matriz original na lista de matrizes => backup matrizes
            add_matriz_lista_matrizes(matriz_original)
            
            # desfazendo o movimento 
            self.mov_left(matriz_atual)

            # verificar se matriz existe na lista de matrizes
            if check_matrizes_iguais(matriz_atual): 
                return False
            else: 
                return True             
        else: 
            return False

    #####################################
    ##### MÓDULOS PARA MOVER O ZERO #####
    #####################################

    def mov_up(self, matriz):
        countC = 0
        countRow = 0
        for row in matriz:
            while countC < 3:
                for elemento in row:
                    if elemento == 0:
                        indexCol = countC
                        indexRow = countRow
                    countC += 1
            countRow += 1
            countC = 0

        numero_trocado = matriz[indexRow-1][indexCol]
        matriz[indexRow][indexCol] = numero_trocado
        matriz[indexRow-1][indexCol] = 0
        matriz_original, nsei = self.mov_down(matriz)

        return matriz, matriz_original

    def mov_down(self, matriz):
        countC = 0
        countRow = 0
        for row in matriz:
            while countC < 3:
                for elemento in row:
                    if elemento == 0:
                        indexCol = countC
                        indexRow = countRow
                    countC += 1
            countRow += 1
            countC = 0

        numero_trocado = matriz[indexRow+1][indexCol]
        matriz[indexRow][indexCol] = numero_trocado
        matriz[indexRow+1][indexCol] = 0

        matriz_original, nsei = self.mov_up(matriz)

        return matriz, matriz_original
        

    def mov_right(self, matriz):
        countC = 0
        countRow = 0
        for row in matriz:
            while countC < 3:
                for elemento in row:
                    if elemento == 0:
                        indexCol = countC
                        indexRow = countRow
                    countC += 1
            countRow += 1
            countC = 0

        numero_trocado = matriz[indexRow][indexCol+1]
        matriz[indexRow][indexCol] = numero_trocado
        matriz[indexRow][indexCol+1] = 0

        matriz_original, nsei = self.mov_left(matriz)
        return matriz, matriz_original
    
    def mov_left(self, matriz):
        countC = 0
        countRow = 0
        for row in matriz:
            while countC < 3:
                for elemento in row:
                    if elemento == 0:
                        indexCol = countC
                        indexRow = countRow
                    countC += 1
            countRow += 1
            countC = 0

        numero_trocado = matriz[indexRow][indexCol-1]
        matriz[indexRow][indexCol] = numero_trocado
        matriz[indexRow][indexCol-1] = 0

        matriz_original, nsei = self.mov_right(matriz)
        return matriz, matriz_original

    ############################
    ##### PONTOS F GERADOS #####
    ############################

    def score_mov_up(self, matriz, g):
        no = Node(g)
        nova_matriz = self.mov_up(matriz)
        no.g = no.sum_score_g(g)
        score_h = no.get_score_h(nova_matriz)
        self.mov_down(nova_matriz)
        f = no.f(no.g, score_h)
        return f

    def score_mov_down(self, matriz, g):
        no = Node(g)
        nova_matriz = self.mov_down(matriz)
        no.g = no.sum_score_g(g)
        score_h = no.get_score_h(nova_matriz)
        self.mov_up(nova_matriz)
        f = no.f(no.g, score_h)
        return f
    
    def score_mov_right(self, matriz, g):
        no = Node(g)
        nova_matriz = self.mov_right(matriz)
        no.g = no.sum_score_g(g)
        score_h = no.get_score_h(nova_matriz)
        self.mov_left(nova_matriz)
        f = no.f(no.g, score_h)
        return f

    def score_mov_left(self, matriz, g):
        no = Node(g)
        nova_matriz = self.mov_left(matriz)
        no.g = no.sum_score_g(g)
        score_h = no.get_score_h(nova_matriz)
        self.mov_right(nova_matriz)
        f = no.f(no.g, score_h)
        return f    
         

# countC = 0
# for row in matriz:
#     while countC < 3:
#         for elemento in row:
#             print(elemento)
#             countC += 1
#     print("\n")
#     countC = 0