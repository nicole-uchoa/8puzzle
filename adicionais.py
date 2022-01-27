def add_matriz_lista_matrizes(self, matriz_original):
       list_matriz = matriz_original.flatten().tolist()
       self.lista_matrizes.append(list_matriz)

       return self.lista_matrizes


def check_matrizes_iguais(self, matriz_atual):
    matriz_atual = matriz_atual.flatten().tolist()
    
    if matriz_atual in self.lista_matrizes: return True
    else: return False