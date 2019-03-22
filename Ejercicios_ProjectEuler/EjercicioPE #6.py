cuadrado_sum = 0
suma_cuadrado = 0
for i in range(1,101):
    cuadrado_sum += i
    suma_cuadrado += i**2
diferencia = cuadrado_sum - suma_cuadrado
print("Suma de cuadrados = ",suma_cuadrado)
print("cuadrado de suma = ",cuadrado_sum**2)
print(cuadrado_sum**2, " - ",suma_cuadrado," = ", (cuadrado_sum**2)-suma_cuadrado)
                                                  