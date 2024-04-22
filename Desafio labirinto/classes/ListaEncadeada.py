from classes.No import No

class ListaEncadeada:
    def __init__(self):
        self.__cabeca = None

    def adicionar(self, linha, coluna):
        novo_no = No(linha, coluna)
        novo_no.set_prox(self.__cabeca) 
        self.__cabeca = novo_no 


    def esta_na_lista(self, linha, coluna):
        atual = self.__cabeca
        while atual is not None:
            if atual.get_linha() == linha and atual.get_coluna() == coluna:
                return True
            atual = atual.get_prox()
        return False