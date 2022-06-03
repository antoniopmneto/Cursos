frase = 'Programamos em python 2?'
# deve devolver 'PORMMS'

def maiusculas(frase):
    lista = [*frase]
    resultado = ''

    for i in lista:
        valor = ord(i)
        if 65 <= valor <= 90:
            resultado = resultado + i

    return resultado

maiusculas(frase)
