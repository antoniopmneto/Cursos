
segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

minutos = segundos // 60
segundosResto = segundos % 60
horas = minutos // 60
minutosResto = minutos % 60
dias = horas // 24
horasResto = horas % 24


print(f"{dias} dias, {horasResto} horas, {minutosResto} minutos e {segundosResto} segundos.")
