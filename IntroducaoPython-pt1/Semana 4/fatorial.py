


n = int(input("Digite um número: "))

i = 1

if n == 0:
    print("1")
elif(n == 1):
    print("1")
else:
    while(n >= 1):
        i = i * n
        n = n - 1
        if(n == 1):
            print(i)
        else:
            continue
