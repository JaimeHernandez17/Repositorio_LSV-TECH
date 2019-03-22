kilometros = float(input("Ingrese el total de kilometros recorridos: "))
precio_por_litro = float(input("Ingrese el valor de la gasolina por litro: "))
dinero_gastado = float(input("Ingrese el dinero en gasolina gastado: "))
tiempo_horas = int(input("Ingrese el tiempo que se ha tardado en horas: "))
tiempo_minutos = int(input("Ingrese el tiempo que se ha tardado en minutos: "))


litros_gasolina = dinero_gastado/precio_por_litro
gasolina_por_k = (litros_gasolina / kilometros)
gasolina_por_100k = gasolina_por_k * 100
cambio_euro_k =  round(((dinero_gastado / kilometros)/ 3512),2)
cambio_euro_100k =  round(((cambio_euro_k*100)/ 3512),5)
hora_s = tiempo_horas * 3600
minuto_s = tiempo_minutos * 60
tiempo_total = hora_s + minuto_s
velocidad_media_hora = kilometros/(tiempo_total/3600)
metros = kilometros*1000
velocidad_media_segundos = metros/tiempo_total

print("\nConsumo de gasolina en litros por cada 100 km: ",gasolina_por_100k,"l")
print("Consumo de gasolina en litros por cada km: ", gasolina_por_k,"l")
print("Consumo de gasolina en euros por cada 100 km: ",cambio_euro_100k," euros")
print("Consumo de gasolina en euros por cada km: ",cambio_euro_k, "euros")
print("velocidad media en km/h: ",velocidad_media_hora, " km/h")
print("velocidad media en m/s: ", round(velocidad_media_segundos,2), " m/s")


