#Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono, tendras que ir pidiendo
#mas datos hasta que yo decida

agenda = []


def guardarContacto(id, nombre, telefono, **kwargs):
    list = [id,nombre,telefono,kwargs]
    agenda.append(list)


def listarContactos(*args):
    for i in args[0]:
        print("\n---------------------------------------------------------------------")
        print("ID: {}".format(i[0]))
        print("Nombre: {}".format(i[1]))
        print("Telefonos: {}".format(i[2]))
        print("Direccion: {direccion}".format(**i[3]))
        print("Whatsapp: {whatsapp}".format(**i[3]))
        print("Telegram: {telegram}".format(**i[3]))
    print("\n-------------------------------------------------------------------------")


def confirmar_datos(name,phone):
    if name in agenda or phone in agenda:
        return False
    else:
        return True


vec_phone = []

ids = [1]


def ingresar_datos():

    whatsapp = False
    telegram = False
    name = input("Ingrese su nombre: ").lower()
    phone = input("Ingrese su telefono: ").lower()
    id = ids[len(ids)-1]
    ids.append(id+1)
    idcontacto = id
    extracell = []
    n = int(input("ingrese el numero de telefonos extras que tiene: "))
    if n != 0:
        for i in range(n):
            cel = input("Ingrese el numero de telefono #{}: ".format(i+1))
            extracell.append(cel)
    vec_phone.append(phone)
    direccion = input("Ingrese su direccion: ")
    whats = input("Si tiene whatsapp ingrese 1 sino presiono otro numero: ")
    if whats == '1':
        whatsapp = True
    else:
        whatsapp = False
    tele = input("Si tiene telegram ingrese 1 sino presiono otro numero: ")
    if tele == '1':
        telegram = True
    else:
        telegram = False

    return name, phone, idcontacto, extracell, direccion, whatsapp, telegram


while True:
    phone = []
    datos = ingresar_datos()
    name = datos[0]
    phone.append(datos[1])
    idcontacto = datos[2]
    extracell = datos[3]
    phone.extend(extracell)
    direc = datos[4]
    whats = datos[5]
    teleg = datos[6]
    if confirmar_datos(name,phone):
        guardarContacto(idcontacto,name,phone,direccion=direc,whatsapp=whats,telegram=teleg)
        x = input("Para seguir ingresando presione cualquier numero, sino presione 1: ")
        if x == '1':
            break
        else:
            continue
    else:
        print("Los datos recien ingresados ya estan en el diccionario, ingrese otros")

print("\n")

listarContactos(agenda)
