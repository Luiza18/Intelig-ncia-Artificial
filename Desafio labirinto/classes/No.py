class No:
    def __init__(self, linha, coluna, pai=None, custo=0, heuristica=0):
        self.__linha = linha
        self.__coluna = coluna
        self.__prox = None
        self.__pai = pai
        self.__custo = custo
        self.__heuristica = heuristica

    def get_heuristica(self):
        return self.__heuristica

    def set_heuristica(self, heuristica):
        self.__heuristica = heuristica

    def get_custo(self):
        return self.__custo

    def set_custo(self, custo):
        self.__custo = custo

    def get_linha(self):
        return self.__linha

    def set_linha(self,linha):
        self.__linha = linha

    def get_coluna(self):
        return self.__coluna

    def set_coluna(self, coluna):
        self.__coluna = coluna

    def get_prox(self):
        return self.__prox

    def set_prox(self, prox):
        self.__prox = prox

    def get_pai(self):
        return self.__pai

    def set_pai(self, pai):
        self.__pai = pai