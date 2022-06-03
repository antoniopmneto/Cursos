import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    fator = []
    resultado = 0

    for i in range(0, len(as_a), 1):
        fator.append(abs(as_a[i] - as_b[i]))

    for i in range(0, len(fator), 1):
        resultado = resultado + fator[i]

    resultado = resultado / 6

    return resultado

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = []
    frases = []
    palavras = []

    caracteres = 0
    caracteres_sentenca = 0
    caracteres_frase = 0

    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))

    for frase in frases:
        palavras.extend(separa_palavras(frase))

    for palavra in palavras:
        caracteres = caracteres + len(palavra)

    qtd_palavras = len(palavras)
    qtd_frases = len(frases)
    qtd_sentencas = len(sentencas)

    for sentenca in sentencas:
        caracteres_sentenca = caracteres_sentenca + len(sentenca)

    for frase in frases:
        caracteres_frase = caracteres_frase + len(frase)

    qtd_palavras_unicas = n_palavras_unicas(palavras)
    qtd_palavras_diferentes = n_palavras_diferentes(palavras)

    wal = float(caracteres / qtd_palavras)
    ttr = float(qtd_palavras_diferentes / qtd_palavras)
    hlr = float(qtd_palavras_unicas / qtd_palavras)
    sal = float(caracteres_sentenca / qtd_sentencas)
    sac = float(qtd_frases / qtd_sentencas)
    pal = float(caracteres_frase / qtd_frases)


    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    grau_similaridade = []

    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))

    for i in range (0, len(assinaturas), 1):
        grau_similaridade.append(compara_assinatura(ass_cp, assinaturas[i]))

    infectado = min(grau_similaridade)

    for i in range (0, len(grau_similaridade), 1):
        if grau_similaridade[i] == infectado:
            texto_infectado = i + 1

    return texto_infectado

def main():

    ass_cp = le_assinatura()
    textos = le_textos()

    print("O autor do texto", avalia_textos(textos, ass_cp), "está infectado com COH-PIAH.")

main()

