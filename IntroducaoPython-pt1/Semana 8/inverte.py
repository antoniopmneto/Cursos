lista1 = []
lista2 = []

n = 1
while n != 0:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    else:
        lista1.append(n)

i = len(lista1) - 1
n = 0
while i >= 0:
    lista2.append(lista1.pop(i))
    i = i - 1
    n = n + 1

for i in lista2:
    print(i)
