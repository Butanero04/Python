##24. Ejercicio. 
##Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día 
##de  la  semana;  si  el  día  es  martes  o  jueves,  se  realizará  un  descuento  del  15%  por  la  compra. 
##Visualizar el descuento y el total a pagar por la compra.

monto_compra = float(input("Ingrese el monto de compra: "))
dia_semana = input("Ingrese el día de la semana: ")
if dia_semana.lower() in ["martes", "jueves"]:
    descuento = monto_compra * 0.15
    total_a_pagar = monto_compra - descuento
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total a pagar: ${total_a_pagar:.2f}")
else:
    print("No se aplicará ningún descuento en este día.")
print("Fin del programa")