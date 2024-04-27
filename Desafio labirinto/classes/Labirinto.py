from random import randint
from classes.Pilha import Pilha
from classes.ListaEncadeada import ListaEncadeada
from classes.Fila import Fila
from copy import deepcopy

LINHAS = 20
COLUNAS = 20
LIMITE_MUROS = 80
INICIO = (0, 0)
FIM = (19, 19)

class Labirinto():
    def __init__(self) -> None:
        self.__matriz = self.criar_mapa()
    
    def get_mapa(self):
        return self.__matriz

    def criar_mapa(self):
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

    def verificar_posicao(self, linha, coluna):
        if 0 <= linha < LINHAS and 0 <= coluna < COLUNAS and self.__matriz[linha][coluna] != '|':
            return True  
        else:
            return False  

    def __buscar_por_profundidade(self):
        pilha = Pilha()
        cp_pilha = Pilha()
        visitados = ListaEncadeada()
    
        pilha.push(INICIO[0], INICIO[1], None) 
        cp_pilha.push(INICIO[0], INICIO[1], None) 

        visitados.adicionar(INICIO[0], INICIO[1])  
        
        while not pilha.is_empty():
            no = pilha.pop()
            linha_atual = no.get_linha() 
            coluna_atual = no.get_coluna()

            movimentos = [(-1, 0), (1, 0),(0, 1), (0, -1)]

            for movimento in movimentos:
                nova_linha = linha_atual + movimento[0]
                nova_coluna = coluna_atual + movimento[1]

                if self.verificar_posicao(nova_linha, nova_coluna) and not visitados.esta_na_lista(nova_linha, nova_coluna):

                    pilha.push(nova_linha, nova_coluna, no) 
                    cp_pilha.push(nova_linha, nova_coluna, no)
                    visitados.adicionar(nova_linha, nova_coluna) 

                    if (nova_linha, nova_coluna) == FIM:  
                        caminho = cp_pilha.exibeCaminho(FIM)
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

                if self.verificar_posicao(nova_linha, nova_coluna) and not visitados.esta_na_lista(nova_linha, nova_coluna):
                    fila.enfileirar(nova_linha, nova_coluna, no)
                    cp_fila.enfileirar(nova_linha, nova_coluna, no)
                    visitados.adicionar(nova_linha, nova_coluna)

                    if (nova_linha, nova_coluna) == FIM:
                        caminho = cp_fila.exibeCaminho(FIM)
                        return caminho, True

        return "Caminho não encontrado", False

    def __busca_por_custo_uniforme(self):
        fila = Fila()
        cp_fila = Fila()
        visitados = ListaEncadeada()

        fila.enfileirar_com_custo(INICIO[0], INICIO[1], None, 0)
        cp_fila.enfileirar_com_custo(INICIO[0], INICIO[1], None, 0)
        visitados.adicionar(INICIO[0], INICIO[1])

        while not fila.esta_vazia():
            no = fila.desenfileirar_com_custo()
            linha_atual = no.get_linha()
            coluna_atual = no.get_coluna()

            if (linha_atual, coluna_atual) == FIM:
                caminho = cp_fila.exibeCaminho(FIM)
                return caminho, True

            movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            c = 1
            for movimento in movimentos:
                nova_linha = linha_atual + movimento[0]
                nova_coluna = coluna_atual + movimento[1]
                novo_custo = no.get_custo() + c
                c = c *2

                if self.verificar_posicao(nova_linha, nova_coluna) and not visitados.esta_na_lista(nova_linha,nova_coluna):
                    fila.enfileirar_com_custo(nova_linha, nova_coluna, no, novo_custo)
                    cp_fila.enfileirar_com_custo(nova_linha, nova_coluna, no, novo_custo)
                    visitados.adicionar(nova_linha, nova_coluna)

        return "Caminho não encontrado", False

    def __busca_greedy(self):
        fila = Fila()
        cp_fila = Fila()
        visitados = ListaEncadeada()

        fila.enfileirar_com_heuristica(INICIO[0], INICIO[1], None, 0, self.__heuristica(INICIO))
        cp_fila.enfileirar_com_heuristica(INICIO[0], INICIO[1], None, 0, self.__heuristica(INICIO))
        visitados.adicionar(INICIO[0], INICIO[1])

        while not fila.esta_vazia():
            no = fila.desenfileirar_com_heuristica(FIM)
            linha_atual, coluna_atual = no.get_linha(), no.get_coluna()

            if (linha_atual, coluna_atual) == FIM:
                caminho = cp_fila.exibeCaminho(FIM)
                return caminho, True

            movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for movimento in movimentos:
                nova_linha = linha_atual + movimento[0]
                nova_coluna = coluna_atual + movimento[1]
               
                novo_custo = no.get_custo() + 1
                heuristica_nova_posicao = self.__heuristica((nova_linha, nova_coluna))

                if self.verificar_posicao(nova_linha, nova_coluna) and not visitados.esta_na_lista(nova_linha, nova_coluna):
                    fila.enfileirar_com_heuristica(nova_linha, nova_coluna, no, novo_custo, heuristica_nova_posicao)
                    cp_fila.enfileirar_com_heuristica(nova_linha, nova_coluna, no, novo_custo, heuristica_nova_posicao)
                    visitados.adicionar(nova_linha, nova_coluna)

        return "Caminho não encontrado", False

    def __busca_a_estrela(self):
        fila = Fila()
        cp_fila = Fila()
        visitados = ListaEncadeada()

        # Adiciona o nó inicial na fila com custo zero
        fila.enfileirar_com_heuristica(INICIO[0], INICIO[1], None, 0, self.__heuristica(INICIO))
        cp_fila.enfileirar_com_heuristica(INICIO[0], INICIO[1], None, 0, self.__heuristica(INICIO))
        visitados.adicionar(INICIO[0], INICIO[1])

        while not fila.esta_vazia():
            no = fila.desenfileirar_com_heuristica(FIM)
            linha_atual, coluna_atual = no.get_linha(), no.get_coluna()

            if (linha_atual, coluna_atual) == FIM:
                caminho = cp_fila.exibeCaminho(FIM)
                return caminho, True

            movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for movimento in movimentos:
                nova_linha = linha_atual + movimento[0]
                nova_coluna = coluna_atual + movimento[1]
               
                novo_custo = no.get_custo() + 1
                heuristica_nova_posicao = self.__heuristica((nova_linha, nova_coluna)) + novo_custo

                if self.verificar_posicao(nova_linha, nova_coluna) and not visitados.esta_na_lista(nova_linha, nova_coluna):
                    fila.enfileirar_com_heuristica(nova_linha, nova_coluna, no, novo_custo, heuristica_nova_posicao)
                    cp_fila.enfileirar_com_heuristica(nova_linha, nova_coluna, no, novo_custo, heuristica_nova_posicao)
                    visitados.adicionar(nova_linha, nova_coluna)

        return "Caminho não encontrado", False

    def __heuristica(self, posicao):
        if posicao[0] > FIM[0]:
            x = 1
        elif posicao[0] <= FIM[0]:
            x = 2
        elif posicao[1] > FIM[1]:
            x = 4
        else:
            x = 8
        return x * abs(posicao[0] - FIM[0]) + abs(posicao[1] - FIM[1])
            
    def __construir_caminho(self, caminho_encontrado):
        mapa_caminho = deepcopy(self.__matriz)
        for i in range(len(caminho_encontrado)):
            linha_atual, coluna_atual = caminho_encontrado[i]

            if (linha_atual, coluna_atual) != INICIO and (linha_atual, coluna_atual) != FIM:
                mapa_caminho[linha_atual][coluna_atual] = 'X'

        return mapa_caminho

    def buscar_caminho(self, tipo_busca):
        if tipo_busca == 'Profundidade':
            caminho_encontrado, flag = self.__buscar_por_profundidade()
        elif tipo_busca == 'Amplitude':
            caminho_encontrado, flag = self.__busca_por_amplitude()
        elif tipo_busca == 'Custo uniforme':
            caminho_encontrado, flag = self.__busca_por_custo_uniforme()
        elif tipo_busca == 'A*':
            caminho_encontrado, flag = self.__busca_a_estrela()
        elif tipo_busca == 'Greedy':
            caminho_encontrado, flag = self.__busca_greedy()
        else:
            flag = False

        if flag:
            mapa =  self.__construir_caminho(caminho_encontrado)
            return mapa
        else:
            return None