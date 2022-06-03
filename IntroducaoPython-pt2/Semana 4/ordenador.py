def ordenada(lista):
    x = lista[0]
    for i in range(len(lista)):
        if lista[i] < x:
            return False
        else:
            pass

    return True

def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
        else:
            pass

    return False




numeros = [55,33,0,900,-432,10,77,2,11]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(ordenada(numeros))
print(ordenada(lista))
print(busca(numeros, 11))
