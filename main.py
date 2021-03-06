import numpy as np
from simplex import Simplex

def leEntrada():
    num_vertices, num_arestas = input().split()

    num_vertices = int(num_vertices)
    num_arestas = int(num_arestas)
    matriz_incidencia = np.zeros((num_vertices,num_arestas), dtype="int16")
    capacidades = np.array(input().split(), dtype="int32")

    for i in range(num_vertices):
        matriz_incidencia[i] = np.array(list(input().split()))

    return capacidades,matriz_incidencia

def popular_vetor_c(matrizIncidencia):
    """
    O vetor c da PL é igual à linha relativa ao vértice "s" na matriz de incidência acrescentado do mesmo
    número de zeros, efetivamente dobrando o tamanho da linha
    """
    c = matrizIncidencia[0]*-1
    c = np.concatenate((c,np.zeros(c.shape[0])), axis=0)
    return c

def popular_matriz_restricoes(matriz_incidencia):
    """A matriz de restrições é formada por todas as linhas da matriz_incidencia
    relativas a vértices que não sejam de "s" e nem de "t" completadas com 0's além de ter duas matrizes 
    identidade do tamanho do número de arestas
    |  M  0  | 
    |  I  I  |
    """
    linhas_vertices = matriz_incidencia[1:-1].copy()
    linhas_vertices = np.concatenate((linhas_vertices, np.zeros_like(linhas_vertices)), axis=1)
    num_arestas = matriz_incidencia.shape[1]
    identidades = np.concatenate((np.identity(num_arestas), np.identity(num_arestas)), axis = 1)
    restricoes = np.concatenate((linhas_vertices, identidades), axis=0)
    return restricoes

def popular_vetor_b(num_vertices_intermediarios, capacidades):
    """
    O vetor b da PL será formado por entradas 1's relativas aos vértices que não sejam
    "s" nem "t" seguido das capacidades máximas de cada vértice
    |   1's |
    | cap's |
    """
    vetor_uns = np.zeros(num_vertices_intermediarios)
    b = np.concatenate((vetor_uns, capacidades), axis = 0)
    return b

def produzVetorMinCut(certificado, numVertices):
    """
    O vértice 's' com certeza faz parte do corte mínimo. O vértice 't' com certeza não faz.
    Sendo 'n' o número de vértices != {s,t}, os 'n' primeiros números do certificado de otimalidade
    da PL primal correspondem aos outros 'n' vértices do grafo. Dessa forma, podemos construir
    um vetor dos vértices pertecentes ao corte mínimo com essas informações
    """
    min_cut = np.zeros(numVertices)
    min_cut[0] = 1
    if numVertices-2 > 0 and min_cut.shape[0] > 2:
        min_cut[1:-1] = certificado[:numVertices-2]
    return min_cut

def main():
    
    capacidades,matriz_incidencia=leEntrada()
    c = popular_vetor_c(matriz_incidencia)
    restricoes = popular_matriz_restricoes(matriz_incidencia)
    b = popular_vetor_b(matriz_incidencia.shape[0]-2, capacidades)

    my_simplex = Simplex(c,b,restricoes)
    estaEmFPI = True
    my_simplex.resolver(estaEmFPI)
    
    print(int(my_simplex.getValorOtimo()))
    solucaoOtima = my_simplex.getSolucaoOtima()
    print(solucaoOtima)
    certificadoOtima = my_simplex.getVetorCertificadoOtima() 
    min_cut = produzVetorMinCut(certificadoOtima, matriz_incidencia.shape[0])
    print(my_simplex.stringVetor(min_cut))
    
if __name__ == '__main__':
    main()