# Calcular raízes
# Calcular o Delta
# Delta Negativo: Não possui raíz real (Z)
# Delta igual a zero: Uma única raíz Real (R)
# Delta positivo: Duas raízes reais

# Pedir os coeficientes da equação de segundo grau
# ax² + bx + c = 0

import math

a, b, c = list(map(float, input("Quais os coeficientes da equação:  \nExemplo: x² + 4x + 9 = 0 4 9 : ").split()))

# delta não pode ser negativo portanto testar
delta = b ** 2 - 4 * a * c
if(a == 0):
    print("Não é equação do segundo grau")
else:
    if (b ** 2 < 4 * a * c ):
        print("esta equação não possui raízes reais")

        if (delta == 0):
            raiz1 = ((- b)/(2 * a))
            print("a raiz desta equação é ", raiz1)
    else:
        raizDelta = math.sqrt(delta)
        raiz1 = ((- b + raizDelta)/(2 * a))
        raiz2 = ((- b - raizDelta)/(2 * a))
        if(raiz1 > raiz2):
            aux = raiz2
            raiz2 = raiz1
            print("as raízes da equação são", aux, "e", raiz2)
        else:
            print("as raízes da equação são", raiz1, "e", raiz2)

               

