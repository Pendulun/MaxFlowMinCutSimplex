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
    O vetor c da PL é igual à linha relativa ao vértice "s" na matriz de incidência
    """
    return matrizIncidencia[0]

def popular_matriz_restricoes(matriz_incidencia):
    """A matriz de restrições é formada por todas as linhas da matriz_incidencia
    relativas a vértices que não sejam de "s" e nem de "t" além de ter uma matriz 
    identidade do tamanho do número de arestas
    |  M  | 
    |  I  |
    """
    linhas_vertices = matriz_incidencia[1:-1].copy()
    num_arestas = matriz_incidencia.shape[1]
    restricoes = np.concatenate((linhas_vertices, np.identity(num_arestas)), axis=0)
    return restricoes

def popular_vetor_b(num_vertices_intermediarios, capacidades):
    """
    O vetor b da PL será formado por entradas 1's relativas aos vértices que não sejam
    "s" nem "t" seguido das capacidades máximas de cada vértice
    |   1's |
    | cap's |
    """
    vetor_uns = np.ones(num_vertices_intermediarios)
    b = np.concatenate((vetor_uns, capacidades), axis = 0)
    return b

def main():
    
    capacidades,matriz_incidencia=leEntrada()
    c = popular_vetor_c(matriz_incidencia)
    print("Vetor C:\n{}".format(c))
    restricoes = popular_matriz_restricoes(matriz_incidencia)
    print("Matriz Restricoes:\n{}".format(restricoes))
    b = popular_vetor_b(matriz_incidencia.shape[0]-2, capacidades)
    print("Vetor b gerado:\n{}".format(b))

    """
    #popular b
    my_simplex = Simplex(c,b,restricoes)
    my_simplex.resolver()
    my_simplex.imprimeResultado()
    """
   
    
if __name__ == '__main__':
    main()