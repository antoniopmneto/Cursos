n = int(input("Digite um número: "))

i = 0
num = 0

while(i < n):
    num = num + 1
    if(num % 2 != 0):
        print(num)
        i = i + 1
    else:
        continue
