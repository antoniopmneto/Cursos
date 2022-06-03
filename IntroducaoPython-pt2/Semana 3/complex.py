class Complexo:
    def __init__(self, real, imaginario):
        self.r = real
        self.i = imaginario

    def __str__(self):
        n = complex(self.r, self.i)
        return str(n)

    def valor(self):
        v = complex(self.r, self.i)
        return v


def main():
    n1 = Complexo(5, 3)
    print(n1)
    print(n1.valor())

    n2 = complex(7, -5)
    print(n2)
    print(type(n1), type(n2))
    n3 = n1.valor() + n2
    print(n3)
    n4 = n1.valor() * n2
    print(n4)
    
main()




# testes como
# cpx1 = Complexo(2,3)
# print(cpx1)

# escreva outros testes
