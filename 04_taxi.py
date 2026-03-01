#TARIFA DE TAXI
dis=float(input("Ingrese la distancia recorrida em km:"))
while dis<=0:
    print("Distancia no valida.")
    dis=float(input("Ingrese la distancia recorrida:"))
hora=int(input("Ingrese la hora del viaje (número entre 0 y 23)"))
while hora<0 or hora>23:
    print("Distancia no valida.")
    hora=int(input("Ingrese la hora del viaje (número entre 0 y 23)"))
if 6<=hora<=19:
    horario="Diurno"
    costo=dis*0.50
elif 0<=hora<6 or 19<hora<=23:
    horario="Nocturno"
    costo=dis*0.65
if dis>10:
    rec=2
else:
    rec=0
Total=1+costo+rec
print(f"Horario: {horario}")
print(f"Distancia recorrida: {dis}km")
print(f"Total a pagar: ${Total:,.2f}")