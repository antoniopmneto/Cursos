def bubble_sort(lista):
    exchanges = True
    passnum = len(lista)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if lista[i]>lista[i+1]:
               exchanges = True
               temp = lista[i]
               lista[i] = lista[i+1]
               lista[i+1] = temp
               print(lista)
       passnum = passnum-1

    return lista


testlist=[54,26,93,17,77,31,44,55,20]
