# Calcular raízes
# Calcular o Delta
# Delta Negativo: Não possui raíz real (Z)
# Delta igual a zero: Uma única raíz Real (R)
# Delta positivo: Duas raízes reais

# Pedir os coeficientes da equação de segundo grau
# ax² + bx + c = 0

import math

# a, b, c = list(map(float, input("Quais os coeficientes da equação:  \nExemplo: x² + 4x + 9 = 0 4 9 : ").split()))

a = float(input())
b = float(input())
c = float(input())

# delta não pode ser negativo portanto testar
delta = b ** 2 - 4 * a * c

if(a == 0):
    print("Não é equação do segundo grau")
elif(b ** 2 < 4 * a * c ):
    print("esta equação não possui raízes reais")
elif (delta == 0):
    raiz1 = ((- b)/(2 * a))
    print(f'a raiz desta equação é {raiz1:.2f}')
else:
    raizDelta = math.sqrt(delta)
    raiz1 = ((- b + raizDelta)/(2 * a))
    raiz2 = ((- b - raizDelta)/(2 * a))
    if(raiz1 > raiz2):
        aux = raiz2
        raiz2 = raiz1
        print(f'as raízes da equação são {aux:.2f} e {raiz2:.2f}')
    else:
        print(f'as raízes da equação são {raiz1:.2f} e {raiz2:.2f}')
