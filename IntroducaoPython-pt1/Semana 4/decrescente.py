## || Verificar se ordem é decrescente || ##
# Receber input's até que a ordem não seja mais decrescente

# input(n)
# verificar n < n1
# while if -> digita outro numero / começa dnv
# else -> para e printa a sequência não é mais decrescente

# while if -> digita outro numero / começa dnv
# else -> para e printa a sequência não é mais decrescente

condicao = True
n1 = int(input("Digite o primeiro número da sequência: "))
print(n1)

while(condicao):
    n = int(input("Digite o próximo número da sequência: "))
    if(n < n1):
        print(n)
        n1 = n
        condicao = True
    else:
        print("A sequência não é mais decrescente")
        condicao = False
