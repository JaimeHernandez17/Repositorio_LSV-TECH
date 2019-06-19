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
        print("Whatsapp: {whats}".format(**i[3]))
        print("Telegram: {teleg}".format(**i[3]))
    print("\n-------------------------------------------------------------------------")


ids = [1]
vec_phone = []
vec_extracell = []


def ingresar_datos():

    estado = True
    extracell = []
    id = ids[len(ids) - 1]
    ids.append(id + 1)
    idcontacto = id
    name = input("Ingrese su nombre: ")

    while estado:
        phone = input("Ingrese su telefono: ")
        if len(vec_phone) != 0 and phone in vec_phone:
            print("\nEl telefono {} ya ha sido registrado. Ingrese otro".format(phone))
        else:
            estado = False
            vec_phone.append(phone)

    n = int(input("ingrese el numero de telefonos extras que tiene: "))
    if n != 0:
        for i in range(n):
            estado= True
            while estado:
                cel = input("Ingrese el numero de telefono #{}: ".format(i + 1))
                if len(vec_extracell) != 0 and cel in vec_extracell or cel in vec_phone or cel in extracell:
                    print("\nEl telefono {} ya ha sido registrado. Ingrese otro".format(cel))
                else:
                    estado = False
                    extracell.append(cel)

    direccion = input("Ingrese su direccion: ")
    whats = input("Si tiene whatsapp ingrese 1 sino presione 0: ")
    if whats == '1':
        whatsapp = True
    elif whats == '0':
        whatsapp = False
    tele = input("Si tiene telegram ingrese 1 sino presione 0: ")
    if tele == '1':
        telegram = True
    elif tele == '0':
        telegram = False

    return name, phone, idcontacto, extracell, direccion, whatsapp, telegram

estado = True

while estado:
    opt = input("""1) Ingresar contactos
2) Mostrar contactos
3) Salir
""")
    if opt < '0' or opt > '3' or not opt.isdigit():
        print("\nIngrese una opcion valida\n")
        continue
    elif opt == '1':
        estado2 = True
        while estado2:
            estado3 = True
            phones = []
            name, phone, idcontacto, extracell, direccion, whats, teleg = ingresar_datos()
            phones.append(phone)
            phones.extend(extracell)
            guardarContacto(idcontacto, name, phones, direccion=direccion,whats=whats,teleg=teleg)
            while estado3:
                opt = input("""\n1) Para ingresar otro contacto
2) Para dejar de ingresar contactos
""")
                if opt < '0' or opt > '2' or not opt.isdigit():
                    print("\nIngrese una opcion valida\n")
                    continue
                elif opt == '1':
                    estado3 = False

                elif opt == '2':
                    estado3 = False
                    estado2 = False
    elif opt == '2':
        if len(agenda) == 0:
            print("\nNo hay registros\n")
        else:
            listarContactos(agenda)
            print("")
    elif opt == '3':
        break

print("\n")