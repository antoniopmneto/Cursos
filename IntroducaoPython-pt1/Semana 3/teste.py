entrada = [None, None, None]


for i in range(0,3):

    entrada[i]= int(input("Digite seus valores: "))


if entrada[0] > entrada[1] and entrada[0] > entrada[2] and entrada[1] > entrada[2] :

    print("A ordem é decrescente.")

elif entrada[0] < entrada[1] and entrada[0] < entrada[2] and entrada[1] < entrada[2] :

    print("A ordem é crescente.")

else:

    print("Não existe ordem crescente ou decrescente.")