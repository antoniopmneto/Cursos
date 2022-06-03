n = int(input("Digite um número: ")) # Número inteiro a ser decomposto #
aux = 1 # Base para Resto da divisão
i = 2 # Primeiro número primo
primos = []

def verificarPrimo(i, n):
    if(n == 0 or n == 1):
        return 1
    elif(n == 2):
        return 2
    else:
        while(i < n):
            aux = n % i
            if(aux != 0):
                i = i + 1
            else:
                # Não é primo em i
                break
        return i


while verificarPrimo(i, n) <= n:
    if n % i == 0:
        n = n // i
        primos.append(i)
        print(primos)
    else:
        i = i + 1
