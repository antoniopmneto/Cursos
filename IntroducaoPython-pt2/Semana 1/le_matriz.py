import matriz

def le_matriz():
    linhas = int(input("Nº de linhas: "))
    colunas = int(input("Nº de colunas: "))

    return cria_matriz(linhas, colunas)


print(le_matriz())
