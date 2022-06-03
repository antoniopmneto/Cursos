string = 'programamos em python'


def conta_letras(frase, contar = 'vogais'):
    vogais = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    qtd = 0
    frase = frase.strip()
    frase = frase.replace(" ", "")
    frase = list(frase)
    qtd = 0
    caracteres = len(frase)

    for i in range(0, caracteres):
        if frase[i] in vogais:
            qtd += 1

    if contar == "vogais":
        return(qtd)
    else:
        return(caracteres - qtd)

print(conta_letras(string, "consoantes"))


# Valores decimais de caracteres vogais
# A, E, I, O, U, a, e, i, o, u
# 65,
