from funcs import retornaQuantidadeVivosPorCelula, criaGrid, atualizaMatriz, aplicaRegra, verificaParedeVizinha
from time import sleep

colunas = 30
linhas  = 30

lista = criaGrid(linhas, colunas)

#teste = [(12,13),(12,14),(12,15),(14,12),(16,12)]
teste = [(10, 10), (10, 11), (10, 12),
         (11, 9), (12, 9), (13, 9)]
#         
#         (13, 22), (14, 22), (15, 22)]
#teste = [(13, 10), (14, 10), (15, 10), (15, 11), (14, 12)]
#teste = [(13, 10), (14, 10), (15, 10), (15, 11), (14, 12),
#         (8,  10) , (9, 10) , (10, 10), (10, 11), (9 , 12)]

for i in teste:
    l, c = i
    lista[l][c] = 1

lista_copia = lista.copy()

atualizaMatriz(lista)

born = [3, 6]
stay = [2, 3]

contador = 0
while True:
    for a in range(0, lista.shape[0]):
        for b in range(0, lista.shape[1]):
            vivos, mortos = retornaQuantidadeVivosPorCelula(lista, a, b)

            if vivos == -1 and mortos == -1:
               continue

            atual = lista[a][b]

            lista_copia[a][b] = aplicaRegra(vivos, atual, stay, born)
            
    print(contador)
    contador += 1
    lista = lista_copia.copy()
    atualizaMatriz(lista_copia)       



print(qtd)
