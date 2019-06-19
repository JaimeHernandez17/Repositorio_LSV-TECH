#Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono, tendras que ir pidiendo
#mas datos hasta que yo decida

dic = {}

def confirmar_datos(name,phone):
    if name in dic or phone in dic:
        return False
    else:
        return True


vec_phone = []

def ingresar_datos():

    name = input("Ingrese su nombre: ").lower()
    phone = input("Ingrese su telefono: ").lower()
    vec_phone.append(phone)

    return name, phone

while True:
    datos = ingresar_datos()
    name = datos[0]
    phone = datos[1]
    if confirmar_datos(name,phone):
        dic.setdefault(name,phone)
        x = input("Para seguir ingresando presione cualquier numero, sino presione 1")
        if x == '1':
            break
        else:
            continue
    else:
        print("Los datos recien ingresados ya están en el diccionario, ingrese otros")

print("\n")

for k,v in dic.items():
    print(k," ", v)

print("\nHay ",len(dic.keys())," registros en el diccionario")

