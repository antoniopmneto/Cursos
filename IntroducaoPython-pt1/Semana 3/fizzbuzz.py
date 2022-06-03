import math

n = int(input("Digite o nª a ser verificado: "))

teste = n % 3
teste2 = n % 5

if(teste == 0 and teste2 == 0):
    print("FizzBuzz")
else:
    print(n)