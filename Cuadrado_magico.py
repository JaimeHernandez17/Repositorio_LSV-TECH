n = int(input("Ingrese el numero de la matriz: "))
matriz = []
num = 1
for i in range(n):
    vec = []
    for j in range(n):
        vec.append(0)
    matriz.append(vec)

a = 0
b = int(n/2)
for i in range(n*n):
    matriz[a][b] = num
    num = num +1
    a=a-1
    b=b+1
    if (a == -1 and b == n):
        a = a+2
        b = n-1
    if (a == -1):
        a = n-1
    if (b == n):
        b = 0
    if (matriz[a][b] != 0):
        a = a + 2
        b = b - 1

for i in range(n):
    print("")
    for j in range(n):
        print(matriz[i][j], end=' ')

