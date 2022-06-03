# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula18.html
# Exercicio 18.3

def main():
    # modifique o codigo para incluir o calculo de DE
    # e verifique se o resultado é diferente de ED usando
    # soma de reais e soma de racionais.

    n = 50
    soma_ed = 0
    soma_de = 0
    soma_ed_rac = Racional()
    soma_de2 = 0
    soma_de2_rac = Racional()

    for i in range(1, n+1):
        soma_ed = soma_ed + 1/i
        soma_ed_rac = soma_ed_rac + Racional(1, i)
        soma_de =  soma_de + 1/(n + 1 - i)


    for i in range(n, 0, -1):
        # i começa == 50, termina == 1
        soma_de2 = soma_de2 + 1/i # 1/(50) + 1/(49) ..... 1 == (50 + 1 + 1)
        soma_de2_rac = soma_de2_rac + Racional(1, i)

    print("Soma ED:          ", soma_ed)
    print("Soma ED racional: ", soma_ed_rac)
    print("Soma ED racional: ", soma_ed_rac.num/soma_ed_rac.den)
    print("Soma DE:          ", soma_de)
    print("Soma DE2:         ", soma_de2)
    print("Soma DE2 racional ", soma_de2_rac.num/soma_de2_rac.den)

def mdc(a, b):
    ''' (int, int) -> int
        recebe dois inteiros diferentes de zero e retorna o maximo
        divisor comum entre a e b'''
    if b == 0: return a
    if a == 0: return b
    while a%b != 0:
        a, b = b, a%b
    return b

class Racional:
    def __init__(self, n=0, d=1):
        div = mdc(n, d)
        self.num = n//div
        self.den = d//div

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

    def __add__(self, other):
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return Racional(n, d)

    def __mul__(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Racional(n, d)

    def __truediv__(self, other):
        n = self.num * other.den
        d = self.den * other.num
        return Racional(n, d)

    def __sub__(self, other):
        d = self.den * other.den
        n = self.num * other.den - other.num * self.den
        return Racional(n, d)

    # escreva aqui o seu codigo para os metodos
    # __truediv__
    # __mul__
    # __sub__
    # e ao menos um teste para cada metodo

main()
