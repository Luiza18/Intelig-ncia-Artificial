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

    def enfileirar_com_custo(self, linha, coluna, no_pai, custo):
        novo_no = No(linha, coluna, no_pai, custo)

        if self.__inicio is None:
            self.__inicio = self.__fim = novo_no
        elif custo < self.__inicio.get_custo():
            novo_no.set_prox(self.__inicio)
            self.__inicio = novo_no
        else:
            no_atual = self.__inicio
            while no_atual.get_prox() is not None and custo >= no_atual.get_prox().get_custo():
                no_atual = no_atual.get_prox()

            novo_no.set_prox(no_atual.get_prox())
            no_atual.set_prox(novo_no)

            if novo_no.get_prox() is None:
                self.__fim = novo_no

    def exibeCaminho(self, fim:tuple):
        atual = self.__inicio
        inicio = (atual.get_linha(), atual.get_coluna())
        while fim != inicio:
            atual = atual.get_prox()
            inicio = (atual.get_linha(), atual.get_coluna())

        caminho = []
        while atual.get_pai() is not None:
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

    def desenfileirar_com_custo(self):
        if self.__inicio is None:
            return None

        no_minimo = self.__inicio
        no_pai_minimo = None

        # Encontra o nó com menor custo
        no_atual = self.__inicio
        no_anterior = None
        while no_atual is not None:
            if no_atual.get_custo() < no_minimo.get_custo():
                no_minimo = no_atual
                no_pai_minimo = no_anterior
            no_anterior = no_atual
            no_atual = no_atual.get_prox()

        # Remove o nó da fila
        if no_pai_minimo is not None:
            no_pai_minimo.set_prox(no_minimo.get_prox())
        else:
            self.__inicio = no_minimo.get_prox()

        if no_minimo == self.__fim:
            self.__fim = no_pai_minimo

        return no_minimo

    def enfileirar_com_heuristica(self, linha, coluna, no_pai, custo, heuristica):
        novo_no = No(linha, coluna, no_pai, custo)

        if self.__inicio is None:
            self.__inicio = self.__fim = novo_no
        elif custo + heuristica < self.__inicio.get_custo() + self.__heuristica_no((self.__inicio.get_linha(), self.__inicio.get_coluna()), self.__inicio):
            novo_no.set_prox(self.__inicio)
            self.__inicio = novo_no
        else:
            no_atual = self.__inicio
            while no_atual.get_prox() is not None and custo + heuristica >= no_atual.get_prox().get_custo() + self.__heuristica_no((no_atual.get_prox().get_linha(), no_atual.get_prox().get_coluna()), no_atual.get_prox()):
                no_atual = no_atual.get_prox()

            novo_no.set_prox(no_atual.get_prox())
            no_atual.set_prox(novo_no)

            if novo_no.get_prox() is None:
                self.__fim = novo_no

    def desenfileirar_com_heuristica(self, fim:tuple):
            if self.__inicio is None:
                return None

            no_minimo = self.__inicio
            no_pai_minimo = None

            # Encontra o nó com menor custo total (custo atual + heurística)
            no_atual = self.__inicio
            no_anterior = None
            while no_atual is not None:
                custo_total_atual = no_atual.get_custo() + self.__heuristica_no(fim,no_atual)
                custo_total_minimo = no_minimo.get_custo() + self.__heuristica_no(fim,no_minimo)
                if custo_total_atual < custo_total_minimo:
                    no_minimo = no_atual
                    no_pai_minimo = no_anterior
                no_anterior = no_atual
                no_atual = no_atual.get_prox()

            # Remove o nó da fila
            if no_pai_minimo is not None:
                no_pai_minimo.set_prox(no_minimo.get_prox())
            else:
                self.__inicio = no_minimo.get_prox()

            if no_minimo == self.__fim:
                self.__fim = no_pai_minimo

            return no_minimo

    def __heuristica_no(self, fim:tuple, no):
        return (abs(no.get_linha() - fim[0]) + abs(no.get_coluna() - fim[1]))

    def esta_vazia(self):
        return self.__inicio is None