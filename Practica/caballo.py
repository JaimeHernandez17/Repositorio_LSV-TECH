import numpy as np

tablero = []

fila = int(input("Ingrese la posicion de la fila en donde empezará: "))
columna = int(input("Ingrese la posicion de la columna en donde empezará: "))

num = 1
for i in range(8):
    vec = []
    for j in range(8):
        vec.append(0)
    tablero.append(vec)

tablero[fila][columna] = num


def movimiento(f, c):
    temporal = []
    posiciones = []
    if f + 2 <= 7 and c + 1 <= 7 and tablero[f + 2][c + 1] == 0:
        temporal.append(f + 2)
        temporal.append(c + 1)
        posiciones.append(temporal)
        temporal = []
    if f + 1 <= 7 and c + 2 <= 7 and tablero[f + 1][c + 2] == 0:
        temporal.append(f + 1)
        temporal.append(c + 2)
        posiciones.append(temporal)
        temporal = []
    if f + 2 <= 7 and c - 1 >= 0 and tablero[f + 2][c - 1] == 0:
        temporal.append(f + 2)
        temporal.append(c - 1)
        posiciones.append(temporal)
        temporal = []
    if f + 1 <= 7 and c - 2 >= 0 and tablero[f + 1][c - 2] == 0:
        temporal.append(f + 1)
        temporal.append(c - 2)
        posiciones.append(temporal)
        temporal = []
    if f - 2 >= 0 and c + 1 <= 7 and tablero[f - 2][c + 1] == 0:
        temporal.append(f - 2)
        temporal.append(c + 1)
        posiciones.append(temporal)
        temporal = []
    if f - 1 >= 0 and c + 2 <= 7 and tablero[f - 1][c + 2] == 0:
        temporal.append(f - 1)
        temporal.append(c + 2)
        posiciones.append(temporal)
        temporal = []
    if f - 2 >= 0 and c - 1 >= 0 and tablero[f - 2][c - 1] == 0:
        temporal.append(f - 2)
        temporal.append(c - 1)
        posiciones.append(temporal)
        temporal = []
    if f - 1 >= 0 and c - 2 >= 0 and tablero[f - 1][c - 2] == 0:
        temporal.append(f - 1)
        temporal.append(c - 2)
        posiciones.append(temporal)

    return posiciones


for i in range(2, 65):
    v = movimiento(fila, columna)
    var = []
    var2 = []
    menor = 0
    for j in range(len(v)):
        var.append(len(movimiento(v[j][0], v[j][1])))
        var2.append(len(movimiento(v[j][0], v[j][1])))
    var2.sort()
    var = np.array(var)
    menor = np.argmin(var)
    print(i)
    tablero[v[menor][0]][v[menor][1]] = i
    fila = v[menor][0]
    columna = v[menor][1]

print("")

for i in range(8):
    print("")
    for j in range(8):
        print(tablero[i][j], end=' ')

print("")
