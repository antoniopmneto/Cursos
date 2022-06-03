# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula17.html

class Complexo:
    # remova a linha abaixo e escreva os metodos da classe Complexo
    def __init__(self, r, c):
        self.real = r
        self.complexo = c


    def __str__(self):
        if self.complexo >= 0:
            n = "%d+%dj"%(self.real, self.complexo)
        else:
            n = "%d%di"%(self.real, self.complexo)
        return n

    def soma(n1, n2):
        a = n1.real + n2.real
        b = n1.complexo + n2.complexo
        resultado = Complexo(a, b)

        print(resultado)

    def multiplicacao(n1, n2):
        a = n1.real
        b = n1.complexo
        c = n2.real
        d = n2.complexo
        x = a * c - b * d
        y = a * d + c * b
        resultado = Complexo(x, y)

        print(resultado)


# testes como
# cpx1 = Complexo(2,3)
# print(cpx1)

# escreva outros testes

def main():

    cpx1 = Complexo(2, 3)
    cpx2 = Complexo(5, -7)

    print("cpx1 = ", cpx1)
    print("cpx2 = ", cpx2)
    Complexo.soma(cpx1, cpx2)
    Complexo.multiplicacao(cpx1, cpx2)

    cpx3 = Complexo(cpx1.real + cpx2.real, cpx1.complexo + cpx2.complexo)
    print("cpx3 = ", cpx3)
    print(type(cpx1), type(cpx2), type(cpx3))

    # cpx4 = complex(10, -10)
    # cpx5 = complex(cpx3.real, cpx3.complexo) * cpx4
    # print(cpx5, type(cpx5))

main()
