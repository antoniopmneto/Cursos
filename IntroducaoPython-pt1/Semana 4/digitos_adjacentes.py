# || verificar se existe adjacentes iguais, se sim, quantos ||
# for

num = input("Digite um número: ")


list = []

for i in num:
    list.append(int(i))

a = 0
b = 1
c = len(list) - 1
condicao = True # é sequência "sim"


if(len(list) == 1 or len(list) == 2):
    if(len(list) == 1):
        condicao = False
    elif(len(list) == 2):
        if(list[a] == list[b]):
            condicao = True
        else:
            condicao = False

    else:
        while(b < c):
            #print(list[a])
            #print(list[b])
            a = a + 1
            b = b + 1
            if(list[a] != list[b]):
                condicao = False
            else:
                condicao = True
                break

print(condicao)
