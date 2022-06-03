largura = []
vazado = []

def retangulo(l, a):
    buraco = (l - 3) * ' '
    vazado = l
    while l > 0:
        largura.append('#')

        l = l - 1

    print(*largura, sep="")
    if vazado > 2:
        print("#", buraco, end= "")
        print("#")
    else:
        pass

    print(*largura, sep="")


l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

retangulo(l, a)
