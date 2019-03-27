#Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono, tendras que ir pidiendo
#mas datos hasta que yo decida

class Agenda:

    agenda = []

    def guardarContacto(id, nombre, telefono, **kwargs):
        list = [id,nombre,telefono,kwargs]
        Agenda.agenda.append(list)

    def eliminarContacto(id):
        a = 0
        for i in Agenda.agenda:
            if id in i:
                Agenda.agenda.pop(a)
            else:
                a = a+1

    def editarContacto(id):
        a = 0
        for i in Agenda.agenda:
            if id in i:
                Agenda.agenda.pop(a)
                name, phone, idcontacto, extracell, direccion, whatsapp, telegram = ingresar_datos()
                phones = []
                phones.append(phone)
                phones.extend(extracell)
                Agenda.guardarContacto(id,name,phones,direccion=direccion,whats=whatsapp,teleg=telegram)
            else:
                a = a+1

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


class Contacto:

    def __init__(self,id, nombre, telefono, **kwargs):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.kwargs = kwargs


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

AgendaFacebook = Agenda

AgendaFacebook.guardarContacto(1, 'Jaime', '123', direccion='cerezos',whats='1',teleg='0')
AgendaFacebook.guardarContacto(2, 'Sandra', '234', direccion='alpes',whats='1',teleg='0')
AgendaFacebook.guardarContacto(3, 'Paula', '456', direccion='alpes',whats='1',teleg='1')
AgendaFacebook.listarContactos(AgendaFacebook.agenda)
AgendaFacebook.eliminarContacto(2)
AgendaFacebook.listarContactos(AgendaFacebook.agenda)
AgendaFacebook.editarContacto(3)
AgendaFacebook.listarContactos(AgendaFacebook.agenda)


