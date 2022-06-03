n = int(input("Digite um número: "))

aux = 1 ##
primo = False
contador = 0
i = 2

def verificarPrimo(n):
    i = 2
    if(n == 0 or n == 1):
        primo = False
    elif(n == 2):
        primo = True
    else:
        while(i < n):
            aux = n % i
            if aux != 0:
                primo = True
                i = i + 1
            else:
                primo = False
                return primo
    return primo

def n_primos(n, contador):
    while n >= 2:
        if verificarPrimo(n) == True:
            contador = contador + 1
        else:
            pass
        n = n - 1
    print(contador)

n_primos(n, contador)
