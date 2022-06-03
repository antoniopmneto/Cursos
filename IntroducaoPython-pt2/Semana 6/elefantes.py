def incomodam(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "incomodam "

    else:
        return incomodam(1) * n


def elefantes(n):
    if n == 0:
        return ""
    elif n <= 2:
        return "Um elefante incomoda muita gente\n%d elefantes "%(n) + incomodam(n) + "muito mais\n"
    else:
        return str(elefantes(n - 1)) + "%d elefantes incomodam muita gente\n"%(n-1) + "%d elefantes "%(n)+ incomodam(n) + "muito mais\n"


print(elefantes(4))






# if n >= 2:
#     for i in range (2, n):
#         print("%d Elefantes"%i + i * " incomodam " + "muito mais")
#         print("%d Elefantes"%i + " incomodam muita gente")
# #
# #     print("%d Elefantes"%n + n * " incomodam " + "muito mais")
# "%d Elefantes"%i + i * " incomodam " + "muito mais\n%d Elefantes incomodam muito mais"%i
# "Um elefante incomoda muita gente\n%d Elefantes "%(n+1) + incomodam(n+1) + "muito mais\n"
