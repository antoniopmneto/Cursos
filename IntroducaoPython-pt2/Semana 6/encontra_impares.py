def encontra_impares(lista, newlist = []):
    if len(lista) == 0:
        return newlist
    elif lista[0] % 2 == 0:
        del lista[0]
        return encontra_impares(lista, newlist)
    else:
        item = lista[0]
        newlist.append(item)
        del lista[0]
        return encontra_impares(lista, newlist)


lista = [-9, 4, 5, -8, -7]
print(encontra_impares(lista))
