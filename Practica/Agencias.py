class Agencia:
    agencias = []

    def __init__(self, codigo, nombre, direccion, lista_conductores):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.conductores = lista_conductores


class Conductor:

    def __init__(self, identificacion, codigo, nombre, apellido, sexo, edad, nacionalidad, codigo_agencia):
        self.identificacion = identificacion
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.codigo_agencia = codigo_agencia


class Turista:

    def __init__(self, identificacion, nombre, apellido, nacionalidad, sexo, edad):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.sexo = sexo
        self.edad = edad


class Tour:

    def __init__(self, codigo, destino, fecha, costo, duracion, codigo_conductor, lista_turistas):
        self.codigo = codigo
        self.destino = destino
        self.fecha = fecha
        self.costo = costo
        self.duracion = duracion
        self.codigo_conductor = codigo_conductor
        self.turistas = lista_turistas


class Acciones:

    def mayorDuracionPorMes(datosTour):
        aux = {}
        for i in datosTour:
            fecha1 = i.fecha.split("/")
            mayorDuracion = 0
            for j in datosTour:
                fecha2 = j.fecha.split("/")
                if fecha1[1] == fecha2[1] and fecha1[2] == fecha2[2]:
                    if int(i.duracion) <= int(j.duracion):
                        mayorDuracion = int(j.duracion)
            meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiempre',
                     'Octubre', 'Noviembre', 'Diciembre']
            mes = int(fecha1[1]) - 1
            if mes not in aux.keys():
                aux.setdefault(meses[mes], mayorDuracion)
        print("\nTours que mas duraron en cada mes\n")
        for k, v in aux.items():
            print("En el mes de {} la mayor duracion fue de {} ".format(k, v))

    def agruparToursPorMes(datosTour):
        aux = {}
        for i in datosTour:
            fecha1 = i.fecha.split("/")
            aux2 = []
            for j in datosTour:
                fecha2 = j.fecha.split("/")
                if fecha1[1] == fecha2[1] and fecha1[2] == fecha2[2]:
                    aux2.append(j.__dict__)
            meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiempre',
                     'Octubre', 'Noviembre', 'Diciembre']
            mes = int(fecha1[1]) - 1
            if mes not in aux.keys():
                aux.setdefault(meses[mes], aux2)
        print(
            "\n---------------------------------------------------------------------------------------------------------------------------------------------------------")
        for k in aux.keys():
            print("Tours en el mes de {}: \n".format(k))
            numerodetours = 0
            for v in aux[k]:
                print(v)
                numerodetours = numerodetours + 1
            if numerodetours == 1:
                print("\nHubo 1 tour")
            else:
                print("\nHubo {} tours".format(numerodetours))
            print(
                "\n---------------------------------------------------------------------------------------------------------------------------------------------------------")

    def totalConductores(conductores):
        print("\nEl numero total de conductores es de: {}\n".format(len(conductores)))
        print(
            "---------------------------------------------------------------------------------------------------------------------------------------------------------")

    def totalTuristas(turistas):
        print("\nEl numero total de turistas es de: {}\n".format(len(turistas)))
        print(
            "---------------------------------------------------------------------------------------------------------------------------------------------------------")

    def agruparToursPorAgencia(tours, agencias):
        aux = {}

    def agruparTuristasPorNacionalidadySexo(self):
        pass


agencias = [Agencia('1', 'Agencia Poseidon', 'Bocagrande', ['123', '234']),
            Agencia('2', 'Agencia Oasis', 'Boquilla', ['456'])]

conductores = [Conductor('123', '1', 'Fernando', 'Perez', 'M', '23', 'Colombia', '1'),
               Conductor('234', '2', 'Luisa', 'Benitez', 'F', '26', 'Colombia', '1'),
               Conductor('456', '3', 'Paula', 'Polo', 'F', '28', 'Argentina', '2')]

turistas = [Turista('11', 'Steve', 'Rogers', 'USA', 'M', '25'), Turista('22', 'Tony', 'Stark', 'USA', 'M', '32'),
            Turista('33', 'Pepper', 'Pops', 'Inglaterra', 'F', '25'),
            Turista('44', 'Natasha', 'Romanovv', 'Rusia', 'F', '23')]

tours = [Tour('1', 'Brasil', '03/06/2018', '20000', '2', '123', ['11', '22']),
         Tour('2', 'Colombia', '02/12/2018', '50000', '3', '234', ['33', '44']),
         Tour('3', 'Argentina', '04/12/2018', '25000', '5', '234', ['22', '33']),
         Tour('4', 'Chile', '04/06/2018', '35000', '7', '456', ['22', '33', '11']),
         Tour('5', 'Venezuela', '05/05/2018', '15000', '3', '123', ['22', '33']),
         Tour('6', 'Ecuador', '02/05/2018', '35000', '1', '456', ['33'])]

acciones = Acciones
acciones.mayorDuracionPorMes(tours)
acciones.agruparToursPorMes(tours)
acciones.totalConductores(conductores)
acciones.totalTuristas(turistas)
acciones.agruparToursPorAgencia(tours, agencias)