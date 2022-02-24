from node import Node

class Movimento:        
    
    ##### VERIFICAR SE O MOVIMENTOS POSSÍVEIS #####

    def movimentos_possiveis(self, puzzle):
        movimentos = []
        linha = 0
        coluna = 0

        # index do 0
        while 0 not in puzzle[linha]:linha += 1
        coluna = puzzle[linha].index(0) 
        
        #mover o 0 para cima
        if linha>0: movimentos.append(1)  
        else: movimentos.append(0)

        #mover o 0 para baixo
        if linha<2: movimentos.append(1)  
        else: movimentos.append(0)

        #mover o 0 para a direita
        if coluna<2: movimentos.append(1)  
        else: movimentos.append(0)

        #mover o 0 para a esquerda
        if coluna>0: movimentos.append(1)  
        else: movimentos.append(0)    

        return movimentos

    def monta_lista_movimentos(self, movimentos_possiveis, matriz, g):
        pontos_de_cada_movimento = []
        if movimentos_possiveis[0] == 1:
            self.score_up = self.score_mov_up(matriz, g)
            pontos_de_cada_movimento.append(self.score_up)
        else: 
            pontos_de_cada_movimento.append(0)

        if movimentos_possiveis[1] == 1:
            self.score_down = self.score_mov_down(matriz, g)
            pontos_de_cada_movimento.append(self.score_down)
        else: 
            pontos_de_cada_movimento.append(0)

        if movimentos_possiveis[2] == 1:
            self.score_right = self.score_mov_right(matriz, g)
            pontos_de_cada_movimento.append(self.score_right)
        else: 
            pontos_de_cada_movimento.append(0)

        if movimentos_possiveis[3] == 1:
            self.score_left = self.score_mov_left(matriz, g)
            pontos_de_cada_movimento.append(self.score_left)
        else: 
            pontos_de_cada_movimento.append(0)

        return pontos_de_cada_movimento
    
    def retorna_movimento_ideal(self, list_valor):
        contador = 0
        indice = None
        minimo = max(list_valor)
        for num in list_valor:
            if num < minimo and num != 0:
                minimo = num
                indice = contador
            contador+=1

        if indice is None:
            movimento = list_valor.index(minimo)
        else: 
            movimento = indice

        return movimento

    def movimenta(self, movimento_ideal, puzzle):
        linha = 0
        coluna = 0
        while 0 not in puzzle[linha]:linha += 1
        coluna = puzzle[linha].index(0) 
        if movimento_ideal == 0:
            puzzle[linha][coluna], puzzle[linha-1][coluna] = puzzle[linha-1][coluna], puzzle[linha][coluna] 

        if movimento_ideal == 1:
            puzzle[linha][coluna], puzzle[linha+1][coluna] = puzzle[linha+1][coluna], puzzle[linha][coluna] 

        if movimento_ideal == 2:
            puzzle[linha][coluna], puzzle[linha][coluna+1] = puzzle[linha][coluna+1], puzzle[linha][coluna] 

        if movimento_ideal == 3:
            puzzle[linha][coluna], puzzle[linha][coluna-1] = puzzle[linha][coluna-1], puzzle[linha][coluna] 

        return puzzle

    ##### PONTOS F GERADOS #####

    def score_mov_up(self, matriz, g):
        no = Node(g)
        nova_matriz = self.movimenta(0, matriz)
        no.g = no.sum_score_g(g)
        score_h = no.get_score_h(nova_matriz)
        self.movimenta(1, matriz)
        f = no.f(no.g, score_h)
        return f

    def score_mov_down(self, matriz, g):
        no = Node(g)
        nova_matriz = self.movimenta(1, matriz)
        no.g = no.sum_score_g(g)
        score_h = no.get_score_h(nova_matriz)
        self.movimenta(0, matriz)
        f = no.f(no.g, score_h)
        return f
    
    def score_mov_right(self, matriz, g):
        no = Node(g)
        nova_matriz = self.movimenta(2, matriz)
        no.g = no.sum_score_g(g)
        score_h = no.get_score_h(nova_matriz)
        self.movimenta(3, matriz)
        f = no.f(no.g, score_h)
        return f

    def score_mov_left(self, matriz, g):
        no = Node(g)
        nova_matriz = self.movimenta(3, matriz)
        no.g = no.sum_score_g(g)
        score_h = no.get_score_h(nova_matriz)
        self.movimenta(2, matriz)
        f = no.f(no.g, score_h)
        return f    
         

