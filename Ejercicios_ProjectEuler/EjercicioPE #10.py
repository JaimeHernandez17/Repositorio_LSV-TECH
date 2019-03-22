# Encontrar la suma de todos los números primos por debajo de dos millones.
divs = [2,3,5,7,11]

#En esta función le paso un numero, me devuelve si es primo o no y me agrega el numero primo a una lista si este es mayor a 11
def isCousin(num):
    for fac in divs:
        if(num % fac != 0):
            if num / fac < fac:
                if num > 11:
                    divs.append(num)
                return True
        else:
            return False
    return False

#Ingreso todos los numeros desde el 2 hasta 2000000 en la funcion que me determina si el numero ingresado es primo
for i in range(2,2000000):
    isCousin(i)
print(sum(divs))
