import math

# resto da divisão por 2 => 0 = nº par
# resto da divisão por 2 => 1 = nº ímpar

n = int(input("Digite o número a ser verificado: "))

teste = n % 2

if(teste == 0):
    print("par")
else:
    print("ímpar")
