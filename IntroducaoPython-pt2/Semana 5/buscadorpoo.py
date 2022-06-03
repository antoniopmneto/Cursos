class Buscador:
    def __init__(self, lista=[], elemento=0):
        self.lista = lista
        self.x = elemento

    def __repr__(self):
        return "Lista: " + repr(self.lista) + " Elemento da busca: " + repr(self.x)

    def busca_sequencia(self):

        for i in range(len(self.lista)):
            if self.lista[i] == self.x:
                return i
        return -1

    def busca_binaria(self):
        primeiro = 0
        ultimo = len(self.lista) - 1
        encontrado = False

        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if self.lista[meio] == self.x:
                return meio
            else:
                if x < self.lista[meio]:
                    ultimo = meio-1
                else:
                    primeiro = meio + 1

        return encontrado


def main():
    lista = [1, 2, 3, 4, 5, 6]
    lista2 = [1, 2, 3, 4, 5]
    lista3 = ["a", "e", "i"]

    Busca1 = Buscador(lista, 5)
    print(Busca1)

main()
