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
    return matrizIncidencia[0]

def main():
    
    capacidades,matriz_incidencia=leEntrada()
    c = popular_vetor_c(matriz_incidencia)
    #popular vetor b

    """
    #popular b
    my_simplex = Simplex(c,b,restricoes)
    my_simplex.resolver()
    my_simplex.imprimeResultado()
    """
   
    
if __name__ == '__main__':
    main()