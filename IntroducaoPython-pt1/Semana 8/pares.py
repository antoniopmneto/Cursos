n = int(input("n: "))
i = 2

while (i <= n):
    if(i % 2 == 0):
        e = i**2
        print("{0}^2 = {1}".format(i, e))
        i = i + 2
    else:
        i = i + 2
