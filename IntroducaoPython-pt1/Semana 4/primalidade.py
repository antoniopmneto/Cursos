# verificar se um número é primo
# ele tem que ser divisivel por todos antes dele exceto 1 e 0

n = int(input("Digite um número: "))

aux = 1 ##
i = 2
primo = False

def verificarPrimo(i, n):
    if(n == 0 or n == 1):
        print("não primo")
        primo = False
    elif(n == 2):
        print("primo")
        primo = True
    else:
        while(i < n):
            aux = n % i
            # print(aux)
            if(aux != 0):
                primo = True
                print(i, aux)
                i = i + 1
            else:
                primo = False
                print("não é primo na divisão por:", i)
                break

verificarPrimo(i, n)
