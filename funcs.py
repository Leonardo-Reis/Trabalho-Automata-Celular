import numpy as np
from time import sleep

import matplotlib.pyplot as plt

def verificaParedeVizinha(lista, lin, col):
    if lista[lin][col] == -1:
        return False

    vizinhos = []

    direita  = lista[lin][col + 1]
    esquerda = lista[lin][col - 1]
    encima   = lista[lin - 1][col]
    baixo    = lista[lin + 1][col]

    encima_direita  = lista[lin - 1][col + 1]
    encima_esquerda = lista[lin - 1][col - 1]
    baixo_direita   = lista[lin + 1][col + 1]
    baixo_esquerda  = lista[lin + 1][col - 1]

    vizinhos.append(direita)
    vizinhos.append(esquerda)
    vizinhos.append(encima)
    vizinhos.append(baixo)
    vizinhos.append(encima_direita)
    vizinhos.append(encima_esquerda)
    vizinhos.append(baixo_direita)
    vizinhos.append(baixo_esquerda)

    if -1 in vizinhos:
        return True
    else:
        return False

def aplicaRegra(vivos, atual, lista_stay, lista_born):
    maior = max(lista_stay)
    menor = min(lista_born) 

    retorno = 0

    if atual == 1 and vivos < maior:
        retorno = 0
    
    if atual == 1 and vivos in lista_stay:#(vivos == 2 or vivos == 3):
        retorno = 1
    
    if atual == 1 and vivos > menor:
        retorno = 0
    
    if atual == 0 and vivos in lista_born:#(vivos == 3 or vivos == 6):
        retorno = 1

    return retorno
    
def retornaQuantidadeVivosPorCelula(lista, lin, col):
    if lista[lin][col] == -1:
        return (-1, -1)

    vizinhos = []
    qtd_vivos = 0
    qtd_mortos = 0

    direita  = lista[lin][col + 1]
    esquerda = lista[lin][col - 1]
    encima   = lista[lin - 1][col]
    baixo    = lista[lin + 1][col]

    encima_direita  = lista[lin - 1][col + 1]
    encima_esquerda = lista[lin - 1][col - 1]
    baixo_direita   = lista[lin + 1][col + 1]
    baixo_esquerda  = lista[lin + 1][col - 1]

    vizinhos.append(direita)
    vizinhos.append(esquerda)
    vizinhos.append(encima)
    vizinhos.append(baixo)
    vizinhos.append(encima_direita)
    vizinhos.append(encima_esquerda)
    vizinhos.append(baixo_direita)
    vizinhos.append(baixo_esquerda)

    for c in vizinhos:
        if c == 1:
            qtd_vivos += 1
        if c == 0:
            qtd_mortos += 1
    
    return (qtd_vivos, qtd_mortos)
    
def atualizaMatriz(lista):
    matrix = np.matrix(lista)
    plt.imshow(matrix, cmap='Blues_r')
    #plt.show(block=False)
    plt.pause(0.3)

def criaGrid(l, c):
    lista = np.zeros(shape=(l, c))
    for i in range(l):
        for j in range(c):
            if i == 0:
                lista[i][j] = -1
            if i == l-1:
                lista[i][j] = -1
            if j == 0:
                lista[i][j] = -1
            if j == c-1:
                lista[i][j] = -1

    return lista
