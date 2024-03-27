from classes.No import No

class Fila:
    def __init__(self):
        self.__inicio = self.__fim = None

    def enfileirar(self, linha, coluna, no_pai):
        novo_no = No(linha, coluna, no_pai)
        if self.__fim is None:
            self.__inicio = novo_no
            self.__fim = novo_no
        else:
            self.__fim.set_prox(novo_no)
            self.__fim = novo_no

    def exibeCaminho(self):
        atual = self.__fim
        caminho = []
        while atual.get_pai()!=None:
            caminho.append((atual.get_linha(), atual.get_coluna()))
            atual = atual.get_pai()
       
        return caminho        

    def desenfileirar(self):
        if self.__inicio is None:
            return None

        no_removido = self.__inicio
        self.__inicio = self.__inicio.get_prox()
        if self.__inicio is None:
            self.__fim = None
        return no_removido

    def esta_vazia(self):
        return self.__inicio is None