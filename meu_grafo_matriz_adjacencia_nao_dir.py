from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''

        lista = set()

        for i in range(len(self.M)):
            for j in range(len(self.M)):

                if i != j:
                    if not self.M[i][j]:

                        if "{}-{}".format(self.N[i], self.N[j]) not in lista:
                            lista.add("{}-{}".format(self.N[i], self.N[j]))

        return lista

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        for i in range(len(self.M)):

            if self.M[i][i]:
                return True

        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if V not in self.N:
            raise VerticeInvalidoException("O vertice passado como paramentro nao existe")

        grau = 0

        for i in range(len(self.M)):

            if self.M[self.N.index(V)][i]:

                if i > self.N.index(V):
                    grau += len(self.M[self.N.index(V)][i])
                elif i == self.N.index(V):
                    grau += 2 * len(self.M[self.N.index(V)][i])
                else:
                    grau += len(self.M[i][self.N.index(V)])

        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if len(self.M[i][j]) > 1:
                    return True

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if V not in self.N:
            raise VerticeInvalidoException("O vertice passado como paramentro nao existe")

        arestas = set()

        for i in range(len(self.M)):

            if self.M[self.N.index(V)][i]:

                if i >= self.N.index(V):
                    for j in self.M[self.N.index(V)][i]:
                        arestas.add(j)

                else:
                    for j in self.M[i][self.N.index(V)]:
                        arestas.add(j)

        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        if self.vertices_nao_adjacentes() == set():
            if self.ha_laco() == False:
                if self.ha_paralelas() == False:
                    return True

        return False