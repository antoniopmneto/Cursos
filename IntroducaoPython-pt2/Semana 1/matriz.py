def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for lin in range(num_linhas):
        linha = []
        for col in range(num_colunas):
            valor = int((input("Digite o elemento: ")))
            linha.append(valor)
        matriz.append(linha)

    return matriz

lin = int(input("Número de linhas: "))
col = int(input("Número de colunas: "))

print(cria_matriz(lin, col)
