from funcs import *
from regras import *
from imagens import *
import matplotlib.pyplot as plt
import numpy as np

funcoes_regra = {
    1: regraB3_S23,
    2: regraB3_S236,
    3: regraB36_S23
}

imagens_padrao = {
    1: replicator,
    2: glider,
    3: pulsar,
    4: gosperGliderGun,
    5: bomber
}

lista = criaGrid(50, 50)

print("""
Qual regra deseja aplicar?
[ 1 ] B3/S23
[ 2 ] B3/S236
[ 3 ] B36/S23""")
opcao = int(input())

regra = funcoes_regra.get(opcao) 
while not regra:
    regra = funcoes_regra.get(opcao)   
    opcao = int(input())

print("""
Qual padrão de entrada deseja?
[ 1 ] Replicator
[ 2 ] Glider 
[ 3 ] Pulsar
[ 4 ] Gosper Glider Gun
[ 5 ] Bomber""")
opcao2 = int(input())

imagem = imagens_padrao.get(opcao2) 
while not imagem:
    imagem = imagens_padrao.get(opcao2)   
    opcao2 = int(input())

for i in imagem:
    l, c = i
    lista[l][c] = 1

lista_copia = lista.copy()

artist = plt.imshow(np.matrix(lista), cmap='Blues_r')

atualizaMatriz(lista, artist)

while True:
    for a in range(0, lista.shape[0]):
        for b in range(0, lista.shape[1]):
            vivos, mortos = retornaQuantidadeVivosPorCelula(lista, a, b)

            if vivos == -1 and mortos == -1:
               continue

            atual = lista[a][b]

            lista_copia[a][b] = regra(vivos, atual)
    lista = lista_copia.copy()
    atualizaMatriz(lista_copia, artist)       
