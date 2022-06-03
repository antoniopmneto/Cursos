# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula18.html
# Exercicio 18.5

def main():

    a = Ponto(1, 2, 5)
    b = Ponto(5, 7, 3)

    print(a, b)
    print(Ponto.dab(a, b))
    print(Ponto.medio(a, b))
    print(Ponto.distOrigin(a))
    print(Ponto.distOrigin(b))

class Ponto:
    def __init__(self, x=0, y=0, z=0):
        self.xaxis = x
        self.yaxis = y
        self.zaxis = z

    def __str__(self):
        return "(%d,%d,%d)"%(self.xaxis, self.yaxis, self.zaxis)

    def dab(self, other):
        dx = (self.xaxis - other.xaxis) ** 2
        dy = (self.yaxis - other.yaxis) ** 2
        dz = (self.zaxis - other.zaxis) ** 2
        r = dx + dy + dz
        r = r ** (1/2)
        return r

    def medio(self, other):
        mx = self.xaxis + other.xaxis
        my = self.yaxis + other.yaxis
        mz = self.zaxis + other.zaxis

        m = Ponto((mx/2), (my/2), (mz/2))

        return m

    def distOrigin(self):
        dx = (self.xaxis) ** 2
        dy = (self.yaxis) ** 2
        dz = (self.zaxis) ** 2
        r = dx + dy + dz
        r = r ** (1/2)
        return r

main()
