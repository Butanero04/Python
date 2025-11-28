##7.  Ejercicio. 
##3Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún 
##número negativo o no.

haLeidoNegativo = False

for i in range(100):
    numero = int(input("Introduce un número: "))
    if numero < 0:
        haLeidoNegativo = True
        break

if haLeidoNegativo:
    print("Has leído algún número negativo.")
else:
    print("No has leído ningún número negativo.")
        