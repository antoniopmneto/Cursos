def remove_repetidos(lista):
    lista.sort()
    i = len(lista) - 1
    while i >= 0:
        if lista[i] == lista[i - 1]:
            lista.pop(i)
            i = i - 1
        else:
            i = i - 1

    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 6, 7, 8, 9, 4, 2, 3, 2, 1, 10]

print(remove_repetidos(lista))
