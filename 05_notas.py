
n1=float(input("Ingrese la primera nota"))
if 0<=n1<=100:
    n2=float(input("Ingrese la segunda nota"))
    if 0<=n2<=100:
        n3=float(input("Ingrese la tercera nota"))
        if 0<=n3<=100:
            prom=(n1+n2+n3)/3
            if 90<=prom<=100:
                tipo="Excelente"
            elif 80<=prom<90:
                tipo="Muy bueno"
            elif 70<=prom<80:
                tipo="Bueno"
            elif 60<=prom<=70:
                tipo="Supletorio"
            else:
                tipo="Reprobado"
            print(f"Nota 1: {n1:,.2f}")
            print(f"Nota 2: {n2:,.2f}")
            print(f"Nota 3: {n3:,.2f}")
            print(f"Promedio: {prom:,.2f}")
            print(f"Clasificación final: {tipo}")
        else:
            print("Error: nota inválida")
    else:
        print("Error: nota inválida")
else:
    print("Error: nota inválida")