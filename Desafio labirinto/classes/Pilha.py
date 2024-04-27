from classes.No import No 

class Pilha:
    def __init__(self):
        self.__topo = None
    
    def push(self, linha, coluna,no_pai):
        novo_no = No(linha, coluna, no_pai)
        novo_no.set_prox(self.__topo)
        self.__topo = novo_no

    def pop(self):
        if self.__topo is None:
            return None

        no_removido = self.__topo
        self.__topo = self.__topo.get_prox()
        return no_removido
    
    def exibeCaminho(self, fim: tuple):
        atual = self.__topo
        inicio = (atual.get_linha(), atual.get_coluna())
        while fim != inicio:
            atual = atual.get_prox()
            inicio = (atual.get_linha(), atual.get_coluna())

        caminho = []
        while atual.get_pai() is not None:
            caminho.append((atual.get_linha(), atual.get_coluna()))
            atual = atual.get_pai()

        return caminho

    def get_topo(self):
        return self.__topo

    def set_topo(self, linha, coluna):
        if self.__topo is not None:
            self.__topo.set_linha(linha)
            self.__topo.set_coluna(coluna)

    def is_empty(self):
        return self.__topo is None