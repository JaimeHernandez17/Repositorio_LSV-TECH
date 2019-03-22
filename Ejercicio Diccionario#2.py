nomina = []
salario_basico_mensual = 850000
aux_trans = 72250
neto_pagado = 0

while True:

    name = input("Nombre: ")
    num_sal = int(input("Numero de salarios mensuales: "))
    dt = int(input("Dias trabajados: "))
    hed = int(input("Horas extras diurnas: "))
    hn = int(input("Horas nocturnas: "))
    hen = int(input("Horas extras nocturnas: "))
    hodof = int(input("Horas ordinarias dominicales o festivos: "))
    heddof = int(input("Horas extras diarias dominicales o festivos: "))
    hendof = int(input("Horas extras nocturnas dominicales o festivos: "))
    salario_mensual= num_sal * salario_basico_mensual
    cesantias = round((salario_mensual * dt)/360)
    intereses_sobre_cesantias = round((cesantias * dt * 0.12)/360)
    prima_servicios = round((salario_mensual * 180)/360)
    vacaciones = round((salario_basico_mensual * dt)/720)
    liquidacion = cesantias+intereses_sobre_cesantias+prima_servicios+vacaciones
    valor_hora_ordinaria = round(salario_mensual / 240)
    hed_c = round(valor_hora_ordinaria * 1.25 * hed)
    hn_c = round(valor_hora_ordinaria * 1.35 * hn)
    hen_c = round(valor_hora_ordinaria * 1.75 * hen)
    hodof_c = round(valor_hora_ordinaria * 1.75 * hodof)
    heddof_c = round(valor_hora_ordinaria * 2 * heddof)
    hendof_c = round(valor_hora_ordinaria * 2.5 * hendof)
    total_paga = liquidacion+hed_c+hn_c+hen_c+hodof_c+heddof_c+hendof_c

    dic = dict(zip(['Nombre','SM','HED','HN','HEN','HODoF','HEDDoF','HENDOF','Liquidación','Neto pagado'],[name,salario_mensual,[hed,hed_c],[hn,hn_c],[hen,hen_c],[hodof,hodof_c],[heddof,heddof_c],[hendof,hendof_c],[cesantias,intereses_sobre_cesantias,vacaciones,prima_servicios],total_paga]))

    if num_sal <= 2:
        total_paga += aux_trans
        dic.setdefault('Aux transporte',aux_trans)

    neto_pagado += total_paga

    nomina.append(dic)

    print("\n")

    x = input("Para seguir ingresando presione cualquier numero, sino presione 1")
    if x == '1':
        break
    else:
        continue

print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
for i in range(len(nomina)):
    print(nomina[i])
    print("\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("Neto pagado: ", neto_pagado)