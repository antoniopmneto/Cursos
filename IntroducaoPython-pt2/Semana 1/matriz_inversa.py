import numpy as np

def cria_matriz(num_linhas, num_colunas):
    j = 0
    matriz = []  #lista vazia
    while np.size(matriz, 0) <= num_linhas:
        linha = []
        while j <= 1:
            valor = int(input("Digite o elemento :"))
            linha.append(valor)
            J += 1
        matriz.append(linha)
        j = 0
    for i in range (0, np.size(matriz, 1)):
        print (str(matriz[i]) + "\n")
    return matriz

m = cria_matriz(3, 3)

print(m[1][1])
