lista = ['maria', ' josé  ', '  PAULO', 'Catarina  ']

def menor_nome(nomes):

    resultado = nomes[0]

    for i in nomes:
        aux = len(i.strip())
        if len(resultado) > aux:
            resultado = i.strip()


    resultado = resultado.capitalize()

    return resultado


print(menor_nome(lista))
