aux = 1
i = 2
# primo = True  # variavel global sempre vai ser true

def maior_primo(n):
    i = 2
    if(n == 0 or n == 1):
        primo = False
        global maiorPrimo
        maior
    elif(n == 2):
        primo = True
    else:
        while(i < n):
            aux = n % i
            if(aux != 0):
                primo = True
                print(n, i, aux, "testando")
                i = i + 1
                global maiorPrimo
                maiorPrimo = n
            else:
                primo = False
                print(n, "não é primo na divisão por", i)
                n = n - 1
                i = 2

    return n

print(maior_primo(int(input("digite: "))))
