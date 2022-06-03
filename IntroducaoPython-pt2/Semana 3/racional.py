# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula18.html

class Racional:
    def __init__(self, n=0, d=1):
        self.put(n, d)

    def __str__(self):
        if self.den != 1:
            return "%d/%d"%(self.num, self.den)
        else:
            return"%d"%(self.num)

    def get(self):
        return self.num, self.den

    def put(self, n=0, d=1):
        self.num, self.den = n, d

    def __mul__(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Racional(n, d)

    def __truediv__(self, other):
        n = self.num * other.den
        d = self.den * other.num
        return Racional(n, d)

    def __add__(self, other):
        d = self.den * other.den
        n = self.num * other.den + other.num * self.den
        return Racional(n, d)

    def __sub__(self, other):
        d = self.den * other.den
        n = self.num * other.den - other.num * self.den
        return Racional(n, d)


# testes
r1 = Racional(2)
r2 = Racional(1,5)
r3 = Racional(3, 7)

# print(r1, '*', r2, '=>', r1.mul(r2))
# print(r2, '/', r3, '=>', r2.div(r3))
# print(r1, '+', r2, '=>', r1.add(r2))
# print(r1, '-', r2, '=>', r1.sub(r2))

r4 = r1 * r2
r5 = r2 / r3
r6 = r1 + r2
r7 = r1 - r2
print(r4, r5, r6, r7)
