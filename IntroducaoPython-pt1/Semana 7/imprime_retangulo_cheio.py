largura = []

def retangulo(l, a):
    while l > 0:
        largura.append('#')
        l = l - 1

    while a > 0:
        print(*largura, sep="")
        a = a - 1

l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

retangulo(l, a)
