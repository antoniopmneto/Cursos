import math

x1 = int(input("Numero xa"))
y1 = int(input("Numero ya"))
x2 = int(input("Numero xb"))
y2 = int(input("Numero yb"))

dAB = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# dAB = math.sqrt(dAB)

if(dAB >= 10):
    print("longe")
else:
    print("perto")
