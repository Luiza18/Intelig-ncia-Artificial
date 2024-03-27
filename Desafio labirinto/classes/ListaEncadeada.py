from classes.No import No

class ListaEncadeada:
    def __init__(self):
        self.__cabeca = None

    def adicionar(self, linha, coluna):
        novo_no = No(linha, coluna)
        novo_no.set_prox(self.__cabeca) #Conecta o novo nó ao restante da lista, definindo o próximo nó como a cabeça atual da lista
        self.__cabeca = novo_no #Atualiza a cabeça da lista para ser o novo nó adicionado

    def esta_na_lista(self, linha, coluna):
        atual = self.__cabeca
        while atual is not None:
            if atual.get_linha() == linha and atual.get_coluna() == coluna:
                return True
            atual = atual.get_prox()
        return False