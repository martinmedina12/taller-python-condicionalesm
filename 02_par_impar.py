# Par o impar + mayoría de edad
num=int(input("Ingrese un numero"))
num=num%2
if num==0:
    print("Numero par")
else:
    print("Numero impar")
edad=int(input("Ingrese su edad"))
if edad>=18:
    print("Mayor de edad")
else: 
    print("Menor de edad")

