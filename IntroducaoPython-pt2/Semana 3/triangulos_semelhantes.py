
class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def __str__(self):
        return "Triângulo de lados: %d, %d, %d"%(self.a, self.b, self.c)

    def tipo_lado(self):
        x = self.a
        y = self.b
        z = self.c

        if x == y and y == z:
            return "equilátero"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isóceles"
        else:
            return "escaleno"

    def retangulo(self):

        lados = [self.a, self.b, self.c]
        x = max(lados)
        print(x)

        if x == self.a:
            if self.a**2 == self.b**2 + self.c**2:
                return True
            else:
                return False
        elif x == self.b:
            if self.b**2 == self.a**2 + self.c**2:
                return True
            else:
                return False
        elif x == self.c:
            if self.c**2 == self.a**2 + self.b**2:
                return True
            else:
                return False
        else:
            return "erro"


    def semelhantes(self, other):
        x = self.a / other.a
        y = self.b / other.b
        z = self.c / other.c

        if x == y == z:
            return True
        else:
            return False

def main():

    t = Triangulo(9, 12, 15)
    t2 = Triangulo(3, 4, 5)
    t.a
    t.b
    t.c

    per = t.perimetro()
    print(t.tipo_lado())
    print(t.retangulo())
    print(t.semelhantes(t2))

main()
