from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from sys import maxsize
import heapq as hq

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''

        nodos = self.N

        lista = set()

        for nodo1 in nodos:
            for nodo2 in nodos:

                if nodo1 != nodo2:
                    vezes = 0

                    for i in self.A:

                        if nodo1 == self.A[i].getV1() and nodo2 == self.A[i].getV2():
                            vezes += 1
                        if nodo1 == self.A[i].getV2() and nodo2 == self.A[i].getV1():
                            vezes += 1

                    if vezes == 0:
                        if "{}-{}".format(nodo2, nodo1) not in lista:
                            lista.add("{}-{}".format(nodo1, nodo2))

        return lista

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
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

        for i in self.A:
            if self.A[i].getV1() == V:
                grau += 1
            if self.A[i].getV2() == V:
                grau += 1

        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        for i in self.A:
            for j in self.A:

                if j != i:
                    if self.A[i].getV1() == self.A[j].getV1() and self.A[i].getV2() == self.A[j].getV2():
                        return True
                    if self.A[i].getV1() == self.A[j].getV2() and self.A[i].getV2() == self.A[j].getV1():
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

        lista = set()

        for i in self.A:
            if V == self.A[i].getV1() or V == self.A[i].getV2():
                lista.add(i)

        return lista

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

    def dijkstra(self, V, v):
        if V not in self.N:
            raise VerticeInvalidoException("O primeiro vertice nao esta no grafo")
        if v not in self.N:
            raise VerticeInvalidoException("O segundo vertice nao esta no grafo")

        betas = []
        alfas = []
        anteriores = []

        for i in self.N:
            betas.append(maxsize)
            alfas.append(0)
            anteriores.append("Vazio")

        betas[self.N.index(V)] = 0
        alfas[self.N.index(V)] = 0
        proximo = [V]
        V_i = V

        for b in proximo:
            V = b
            sobre_V = self.arestas_sobre_vertice(V)

            for a in sobre_V:
                v_temp = self.vertice_oposto(a, V)

                if alfas[self.N.index(v_temp)] == 0:
                    if betas[self.N.index(v_temp)] > self.A[a].peso + betas[self.N.index(V)]:
                        betas[self.N.index(v_temp)] = self.A[a].peso + betas[self.N.index(V)]
                        anteriores[self.N.index(v_temp)] = V

                if v_temp not in proximo:
                    proximo.append(v_temp)

            alfas[self.N.index(V)] = 1

        if alfas[self.N.index(v)] == 0:
            return []

        ant = v
        temp_s = [v]
        saida = []

        while ant != V_i:
            temp_s.append(anteriores[self.N.index(ant)])
            ant = anteriores[self.N.index(ant)]

        for i in range(len(temp_s)):
            saida.append(temp_s.pop(-1))

        return saida




    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass

    def vertice_oposto(self, A, V):

        if self.A[A].getV1() == V:
            v = self.A[A].getV2()

        elif self.A[A].getV2() == V:
            v = self.A[A].getV1()

        return v

    def dfs(self, V = ' ', arvore_dfs = 0, arestas_visitadas = 0):

        try:
            if arvore_dfs == 0:
                arvore_dfs = MeuGrafo([])
                arestas_visitadas = MeuGrafo([])
        except:
            pass

        sobre_V = self.arestas_sobre_vertice(V)

        for a in sobre_V:

            if a not in arestas_visitadas.A:

                v = self.vertice_oposto(a, V)

                repetida = False

                for b in arvore_dfs.A:
                    if b == a:
                        repetida = True

                for c in arestas_visitadas.A:
                    if c == a:
                        repetida = True

                if V not in arestas_visitadas.N:
                    arestas_visitadas.adicionaVertice(V)

                if v not in arestas_visitadas.N:
                    arestas_visitadas.adicionaVertice(v)
                    arestas_visitadas.adicionaAresta(a, V, v)

                if not repetida:

                    if V not in arvore_dfs.N:
                        arvore_dfs.adicionaVertice(V)

                    if v not in arvore_dfs.N:
                        arvore_dfs.adicionaVertice(v)
                        arvore_dfs.adicionaAresta(a, V, v)

                        arvore_dfs = self.dfs(v, arvore_dfs, arestas_visitadas)

        return arvore_dfs

    def bfs(self, V=''):

        lista_bfs = MeuGrafo(self.N[::])

        visitado = []
        fila = []

        if V not in self.N:
            raise VerticeInvalidoException("O vertice nao esta no grafo")

        visitado.append(V)
        fila.append(V)

        while len(fila) != 0:
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                analisando = fila[0]

                if v1 == analisando or v2 == analisando:

                    if analisando == v1:
                        adjacente = v2
                    else:
                        adjacente = v1

                    if adjacente not in visitado:
                        fila.append(adjacente)
                        visitado.append(adjacente)
                        lista_bfs.adicionaAresta(a, analisando, adjacente)

            fila.pop(0)

        return lista_bfs

    def conexo(self):

       if len(self.A) < (len(self.N) - 1):
           return False

       arvore = self.dfs(self.N[0])

       if len(arvore.N) != len(self.N):
           return False

       return True

    def caminho_dois_vertices(self, x, y):

        for i in self.A:

            if self.A[i].getV1() == x and self.A[i].getV2() == y:
                return i

            if self.A[i].getV2() == x and self.A[i].getV1() == y:
                return i

        return False

    def encontra_ciclo(self, V, final, sequencia = [], arestas_visitadas = [], encontrado = False):

        sobre_V = self.arestas_sobre_vertice(V)

        for a in sobre_V:

            if a not in arestas_visitadas:
                arestas_visitadas.append(a)

                v = self.vertice_oposto(a, V)
                if v == final:
                    encontrado = True

                if encontrado == False:
                    sequencia, encontrado = self.encontra_ciclo(v,final, sequencia, arestas_visitadas, encontrado)

                if encontrado == True:
                    sequencia.append(v)
                    sequencia.append(a)
                    break


        return sequencia, encontrado

    def ha_ciclo(self):

        if self.ha_laco():

            for i in self.A:
                if self.A[i].getV1() == self.A[i].getV2():
                    return [self.A[i].getV1(), i, self.A[i].getV2()]

        for inicial in self.N:
            seq, x = self.encontra_ciclo(inicial,inicial,[],[])
            if x == True:
                seq.append(inicial)
                break

        return seq

    def encontra_caminho(self, tam_max, V, sequencia = [], arestas_visitadas = [], vertices_visitados = [], tamanho = 1):
        sobre_V = self.arestas_sobre_vertice(V)

        for a in sobre_V:

            if a not in arestas_visitadas:
                v = self.vertice_oposto(a, V)
                if v not in vertices_visitados:

                    arestas_visitadas.append(a)
                    vertices_visitados.append(v)
                    tamanho +=2

                    if tamanho < tam_max:
                        sequencia, tamanho = self.encontra_caminho(tam_max, v, sequencia, arestas_visitadas,vertices_visitados, tamanho)

                    if tamanho == tam_max:
                        sequencia.append(v)
                        sequencia.append(a)
                        break

        return sequencia, tamanho

    def caminho(self, n):

        for inicial in self.N:
            seq, x = self.encontra_caminho(n, inicial, [], [], [])
            seq.append(inicial)
            if x == n:
                break

        if x != n:
            seq = []
        print(seq)
        return seq

    def mst_prim(self, V):
        arvore_s = MeuGrafo()
        arvore_s.adicionaVertice(V)
        proximo = [V]

        while True:
            V = proximo[0]

            lista = self.arestas_sobre_vertice(V)
            prioridade = []

            for i in lista:
                prioridade.append([self.A[i].peso, i])

            hq.heapify(prioridade)

            for a in prioridade:
                v = self.vertice_oposto(a[1], V)

                if v not in arvore_s.N:
                    arvore_s.adicionaVertice(v)
                    arvore_s.adicionaAresta(a[1], V, v)
                    proximo.append(v)

            proximo.pop(0)

            if len(proximo) == 0:
                break

        return arvore_s

    def mst_kruskal(self):
        arvore_s = MeuGrafo()
        for n in self.N:
            arvore_s.adicionaVertice(n)

        lista = []
        for a in self.A:
            lista.append([self.A[a].peso, a])

        hq.heapify(lista)

        for i in lista:
            aresta = i[1];

            s = arvore_s.dijkstra(self.A[aresta].getV1(), self.A[aresta].getV2())

            if s == []:
                arvore_s.adicionaAresta(aresta, self.A[aresta].getV1(), self.A[aresta].getV2(), self.A[aresta].peso)

        return arvore_s