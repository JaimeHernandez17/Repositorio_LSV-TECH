import math
gigas = int(input("Ingresar el numero de gigas: "))
conver = gigas * 1024

r = math.ceil(conver / 700)

print("Necesitará ",r," CDS")
