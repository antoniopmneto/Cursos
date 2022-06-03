def fatorial(num):
    i = 1
    if num == 0:
        return 1
    elif(num == 1):
        return 1
    else:
        while(num >= 1):
            i = i * num
            num = num - 1
            if(num == 1):
                return i
            else:
                continue

n = int(input("n :"))
k = int(input("k :"))

if(n < k):
    print("n menor que k")
else:
    aux = n - k
    n = fatorial(n)
    k = fatorial(k)
    aux = fatorial(aux)
    resultado = n / (k * aux)
    print(n)

    print(k)

    print(aux)

    print(resultado)
