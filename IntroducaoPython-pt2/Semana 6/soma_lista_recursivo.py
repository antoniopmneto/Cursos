def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        lista[1] = lista[0] + lista[1]
        del lista[0]
        return soma_lista(lista)

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 101]

print(soma_lista(lista))
