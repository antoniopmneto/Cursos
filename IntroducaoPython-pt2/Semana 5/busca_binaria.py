def busca(lista, elemento):
    first = 0
    last = len(lista)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        print(midpoint)
        if lista[midpoint] == elemento:
            found = True
            return midpoint
        else:
            if elemento < lista[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

testlist = [1, 2, 3, 4, 5]
