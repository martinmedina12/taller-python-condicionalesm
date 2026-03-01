# Descuento tienda
sub=float(input("Ingrese el subtotal"))
tipo=input("¿Es cliente VIP o Regular?")
if tipo=="VIP":
    des=sub*0.15
elif tipo=="regular":
    if sub >=100:
        des= sub*0.05
    else:
        des=0
Total=sub-des
print(f"Subtotal: ${sub:,.2f}")
print(f"Descuento: ${des:,.2f}")
print(f"Total: ${Total:,.2f}")

