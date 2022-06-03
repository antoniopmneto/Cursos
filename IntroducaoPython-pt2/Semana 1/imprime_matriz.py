m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[10, 20, 30], [40, 50, 60]]

# m1 = matriz.cria_matriz(num_linhas, num_colunas)
# m2 = matriz.cria_matriz(num_linhas, num_colunas)

def imprime_matriz(matriz):

    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])

    # 2 linhas, 3 colunas (0, 1 // 0, 1, 2)

    for linha in range(qtd_linhas):
        for coluna in range(qtd_colunas):
            if coluna == qtd_colunas - 1:
                print(str(matriz[linha][coluna]))
            else:
                print(str(matriz[linha][coluna]), end = " ")


imprime_matriz(m1)

# (str(matriz[linha][coluna]), end=" ")
