# || Produto dos Valores Digitados || #
#
# Digitar n números e realizar a multiplicação de cada um deles até o último
# Dificuldade: Orientar a forma de entrada de dado (Um por um, lista, array etc...)

n = 1
prod = 1
tamanho = 0


while (n != 0):
    try:
        n = int(input("Digite um número para a lista ou para encerrar digite 0 :"))
    except (TypeError, ValueError):
        print("Tipo de dado irreconhecível, tente novamente (ex: 10)")
    else:
        if(n != 0):
            prod = prod * n
            print("Produto: ", prod)
            tamanho = tamanho + 1
        else:
            print("Produto final é ", prod)
            print("Foram multiplicados ", tamanho, "números")