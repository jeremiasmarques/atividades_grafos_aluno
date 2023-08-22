from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

paraiba = GrafoListaAdjacencia(["A", "B", "C", "D", "E", "F", "G", "H", "I"])

paraiba.adicionaVertice("J")

paraiba.adicionaAresta("a1", "J", "C")
paraiba.adicionaAresta("a2", "H", "I")
paraiba.adicionaAresta("a3", "F", "D")
paraiba.adicionaAresta("a4", "E", "I")
paraiba.adicionaAresta("a5", "A", "C")
paraiba.adicionaAresta("a6", "B", "H")
paraiba.adicionaAresta("a7", "J", "F")

print(paraiba)
