
n = int(input("Digite um número: "))

aux = 1
i = 2
primo = False

if(n == 0 or n == 1):
    print("não primo")
    primo = False
elif(n == 2):
    print("primo")
    primo = True
else:
    while(i < n):
        aux = n % i
        if(aux != 0):
            primo = True
            print(i, aux)
            i = i + 1
        else:
            primo = False
            print(i, aux, "não é primo")
            break
if(primo):
    print("primo")
else:
    print("não é primo")
