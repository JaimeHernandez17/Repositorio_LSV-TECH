"""sudukuDefecto=[[0,9,2,0,0,4,7,0,0],
               [1,5,0,0,6,0,2,0,8],
               [0,0,0,0,1,2,0,4,9],
               [0,0,0,0,5,8,6,0,0],
               [8,4,0,0,3,0,0,5,2],
               [0,0,3,2,9,0,0,0,0],
               [6,1,0,8,4,0,0,0,0],
               [2,0,5,0,7,0,0,6,1],
               [0,0,7,6,0,0,8,9,0]]"""
"""
sudukuDefecto=[[5,0,4,3,0,6,0,7,0],#Sudoku fácil
               [0,0,1,0,0,0,0,0,0],
               [0,7,6,0,0,2,9,0,0],
               [0,8,0,7,0,5,6,0,1],
               [7,6,0,0,3,0,0,8,9],
               [9,0,3,8,0,4,0,2,0],
               [0,0,8,1,0,0,2,9,0],
               [0,0,0,0,0,0,3,0,0],
               [0,3,0,4,0,7,1,0,6]]"""

sudukuDefecto = [[8, 0, 0, 0, 0, 0, 0, 0, 0],  # el más dificil del mundo
                 [0, 0, 3, 6, 0, 0, 0, 0, 0],
                 [0, 7, 0, 0, 9, 0, 2, 0, 0],
                 [0, 5, 0, 0, 0, 7, 0, 0, 0],
                 [0, 0, 0, 0, 4, 5, 7, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 3, 0],
                 [0, 0, 1, 0, 0, 0, 0, 6, 8],
                 [0, 0, 8, 5, 0, 0, 0, 1, 0],
                 [0, 9, 0, 0, 0, 0, 4, 0, 0]]
sudoku = sudukuDefecto


def buscaRango(numero): # Función que setorifica un número en tres diferentes rangos(Para poder buscar por grupos)
    if numero < 3:
        rango = 0;
    elif numero > 2 and numero < 6:
        rango = 3;
    elif numero > 5 and numero < 9:
        rango = 6;
    return rango;


def buscaGrupo(matriz, fila, columna, numero): #Función que identifica si el número existe en el grupo indicado
    # print("Este es el rango de Fila: ", buscaRango(fila))
    filaH = buscaRango(fila)
    # print("Este es el rango de Columna: ", buscaRango(columna))
    columnaH = buscaRango(columna)
    grupo = []
    for i in range(filaH, filaH + 3):
        for j in range(columnaH, columnaH + 3):
            grupo.append(matriz[i][j])
    if grupo.count(numero) > 0:
        # print("Existe el número: ")
        return 1
    else:
        # print("No existe el número")
        return 0

#buscaGrupo(sudukuDefecto, 2, 0, 8);

def fila_columna(matriz, fila, columna,
                 numero):  # Función que comprueba si el número existe en la columna y fila, y además valida si existe en el grupo
    columnaT = []
    for i in range(len(matriz)):
        columnaT.append(matriz[i][columna])
    if matriz[fila].count(numero) > 0 or columnaT.count(numero) > 0 or buscaGrupo(matriz, fila, columna, numero) > 0 or \
            matriz[fila][columna] > 0:
        print("El número ", numero, " existe en la fila: ", matriz[fila], " Esta es la columna: ", columnaT)
        return 1
    else:
        return 0

def muestra(sudoku): #función encargada de mostrar el sudoku
    longitud = len(sudoku)
    # print(longitud)
    for i in range(longitud):
        list = ''
        for j in range(longitud):
            if (j - 2) % 3 == 0:
                list = list + str(sudukuDefecto[i][j]) + ' * '
            else:
                list = list + str(sudukuDefecto[i][j]) + '|'
        print(list)

muestra(sudukuDefecto)

def llenar(matriz, fila, columna, valor): #Función encargada de llenar el sudoku
    if fila_columna(matriz, fila, columna, valor) == 0:
        matriz[fila][columna] = valor
        print("llenado: ", valor)
        muestra(sudukuDefecto)
        print("---------------------")
        return 0
    else:
        # print("nada")
        # muestra(sudukuDefecto)
        print("---------------------")
        return 1


def resolver(matriz, fila, columna): #Función encargada de resolver el sudoku
    if columna >= 9:
        columna = 0;
        fila = fila + 1
    if fila == 9:
        return True
    if sudoku[fila][columna] is not 0:
        if resolver(matriz, fila, columna + 1):
            return True
    for i in range(1, 10):
        if (llenar(matriz, fila, columna, i) == 0):
            print("*****************************")
            if resolver(matriz, fila, columna + 1):
                # print(columna,"-----")
                # muestra(matriz)
                # print("ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ")
                return True
            matriz[fila][columna] = 0
    return False


resolver(sudukuDefecto, 0, 0)
print("***************\nSolución de SUDOKU")
muestra(sudukuDefecto)

