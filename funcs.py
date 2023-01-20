# Olá, professor! Se interessar a você, versionamos nosso código no GitHub! 
# Link: https://github.com/Leonardo-Reis/Trabalho-Automata-Celular

import numpy as np
import matplotlib.pyplot as plt

def aplicaRegra(vivos, atual, lista_stay, lista_born):
    maior = max(lista_stay)
    menor = min(lista_born) 

    retorno = 0

    if atual == 1 and vivos < maior:
        retorno = 0
    
    if atual == 1 and vivos in lista_stay:
        retorno = 1
    
    if atual == 1 and vivos > menor:
        retorno = 0
    
    if atual == 0 and vivos in lista_born:
        retorno = 1

    return retorno
    
def retornaQuantidadeVivosPorCelula(lista, lin, col):
    qtd_vivos = 0
    qtd_mortos = 0

    x = []

    try: #direita
        x.append(lista[lin][col + 1])
    except:
        x.append(lista[lin][0])

    try: #esquerda
        x.append(lista[lin][col - 1])
    except:
        pass

    try: #baixo
        x.append(lista[lin + 1][col])
    except:
        x.append(lista[0][col])

    try: #cima
        x.append(lista[lin - 1][col])
    except:
        pass



    try: #cima-direita
        x.append(lista[lin - 1][col + 1])
    except:
        x.append(lista[lin - 1][0])

    try: #cima-esquerda
        x.append(lista[lin - 1][col - 1])
    except:
        pass

    try: #baixo-direita
        x.append(lista[lin + 1][col + 1])
    except:
        if   lin + 1 == lista.shape[0] and col + 1 != lista.shape[1]: # extrapola linha
            x.append(lista[0][col + 1])
        elif col + 1 == lista.shape[1] and lin + 1 != lista.shape[0]: # extrapola coluna
            x.append(lista[lin + 1][0])
        else: # extrapola os dois
            x.append(lista[0][0])

    try: #baixo-esquerda
        x.append(lista[lin + 1][col - 1])
    except:
        x.append(lista[0][col - 1])
    
    for c in x:
        if c == 1:
            qtd_vivos += 1
        if c == 0:
            qtd_mortos += 1
    
    return (qtd_vivos, qtd_mortos)
    
def atualizaMatriz(lista, artist):
    matrix = np.matrix(lista)
    artist.set_data(matrix)
    plt.pause(0.01)

def criaGrid(l, c):
    lista = np.zeros(shape=(l, c))
    return lista
