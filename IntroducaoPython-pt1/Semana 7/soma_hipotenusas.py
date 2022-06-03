# n = int(input("Quantidade de testes: "))
N = int(input("Quantidade de esferas: "))
q = 1  # aumenta quando resto é zero (1 % 1) = 0
t = 0 # qtd esferas com nº par de divisores
R = N

while(N > 1):
    while (R > 1):
        if (N % R == 0):
            q = q + 1
            R = R - 1
        else:
            R = R - 1
    N = N - 1
    R = N
    if (q % 2 == 0):
        t = t + 1
    q = 1


print(t)

# 1 -> (1) (ímpar) #0
# 2 -> (1, 2) (par) # 1
# 3 -> (1, 3) (par) # 2
# 4 -> (1, 2, 4) (ímpar) # 2
# 5 -> (1, 5) (par) # 3
# 6 -> (1, 2, 3, 6) (par) # 4
# 7 -> (1, 7) par # 5
# 8 -> (1, 2, 4, 8) par # 6
# 9 -> (1, 3, 9) ímpar # 6
# 10 -> (1, 2, 5, 10) par # 7
