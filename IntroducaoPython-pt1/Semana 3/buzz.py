import math

n = int(input("Digite o nª a ser verificado: "))

teste = n % 5

if(teste == 0):
    print("Buzz")
else:
    print(n)