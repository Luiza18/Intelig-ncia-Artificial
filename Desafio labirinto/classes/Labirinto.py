from random import randint
from classes.Pilha import Pilha
from classes.ListaEncadeada import ListaEncadeada
from classes.Fila import Fila

LINHAS = 10
COLUNAS = 10
LIMITE_MUROS = 20
INICIO = (0, 0)
FIM = (LINHAS - 1, COLUNAS - 1)

class Labirinto():
    def __init__(self) -> None:
        self.__matriz = self.__criar_mapa()

    def get_mapa(self):
        mapa = self.__matriz
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                if linha == 0 and coluna == 0:
                    mapa[linha][coluna] = '*'
                elif linha == LINHAS - 1 and coluna == COLUNAS - 1:
                    mapa[linha][coluna] = '?'
                elif mapa[linha][coluna] == 0:
                    mapa[linha][coluna] = '-'
                else:
                    mapa[linha][coluna] = '|'

        return mapa

    def __criar_mapa(self):
        mapa = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
        qtd_muros = 0  # Contador de muros

        while qtd_muros < LIMITE_MUROS:
            # Escolher randomicamente o local do muro
            linha = randint(0, COLUNAS - 1)
            coluna = randint(0, LINHAS - 1)

            # Adicionando os muros e verificando se a pocição é o ínicio ou o fim
            if (linha, coluna) != INICIO and (linha, coluna) != FIM and mapa[linha][coluna] == 0:
                mapa[linha][coluna] = 1
                qtd_muros += 1

        return mapa

    def verificar_posicao(self, linha, coluna):
        if 0 <= linha < LINHAS and 0 <= coluna < COLUNAS and self.__matriz[linha][coluna] != 1:
            return True  # Posição válida dentro dos limites do labirinto e não é um muro
        else:
            return False  # Posição fora dos limites do labirinto ou é um muro

    def __buscar_por_profundidade(self):
        pilha = Pilha()
        cp_pilha = Pilha()
        visitados = ListaEncadeada()
    
        pilha.push(INICIO[0], INICIO[1], None) 
        cp_pilha.push(INICIO[0], INICIO[1], None) 

        visitados.adicionar(INICIO[0], INICIO[1])  
        
        while not pilha.is_empty():
            no_atual = pilha.get_topo()

            movimentos = [(-1, 0), (1, 0),(0, 1), (0, -1)]

            for movimento in movimentos:
                nova_linha = no_atual.get_linha() + movimento[0]
                nova_coluna = no_atual.get_coluna() + movimento[1]

                if not visitados.esta_na_lista(nova_linha, nova_coluna) and self.verificar_posicao(nova_linha, nova_coluna):
                        pilha.push(nova_linha, nova_coluna, no_atual) 
                        visitados.adicionar(nova_linha, nova_coluna) 

                        if (nova_linha, nova_coluna) == FIM:  
                            caminho = cp_pilha.exibeCaminho()
                            return caminho, True
            
                   
        return "Caminho não encontrado", False

    def __busca_por_amplitude(self):
        fila = Fila()
        cp_fila = Fila()
        visitados = ListaEncadeada()

        fila.enfileirar(INICIO[0], INICIO[1], None)
        cp_fila.enfileirar(INICIO[0], INICIO[1], None)
        
        visitados.adicionar(INICIO[0], INICIO[1])

        while not fila.esta_vazia():
            no = fila.desenfileirar()
            linha_atual = no.get_linha()
            coluna_atual = no.get_coluna()

            movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for movimento in movimentos:
                nova_linha = linha_atual + movimento[0]
                nova_coluna = coluna_atual + movimento[1]

                #print(f"A posição : {(nova_linha, nova_coluna)}  é {self.verificar_posicao(nova_linha, nova_coluna)}")
                if self.verificar_posicao(nova_linha, nova_coluna) and not visitados.esta_na_lista(nova_linha, nova_coluna):
                    fila.enfileirar(nova_linha, nova_coluna, no)
                    cp_fila.enfileirar(nova_linha, nova_coluna, no)
                    visitados.adicionar(nova_linha, nova_coluna)

                    if (nova_linha, nova_coluna) == FIM:
                        caminho = cp_fila.exibeCaminho()
                        return caminho, True

        return "Caminho não encontrado", False

    def __construir_caminho(self, caminho_encontrado):
        mapa = self.__matriz

        for i in caminho_encontrado:
            linha, coluna = i 
            if i != FIM :
                mapa[linha][coluna]= 'X'

        return mapa

    def buscar_caminho(self, tipo_busca):
        if tipo_busca == 'Profundidade':
            caminho_encontrado, flag = self.__buscar_por_profundidade()
        elif tipo_busca == 'Amplitude':
            caminho_encontrado, flag = self.__busca_por_amplitude()
        else:
            return None

        if flag:
            print(caminho_encontrado)
            mapa =  self.__construir_caminho(caminho_encontrado)
            return mapa
        else:
            return None