##19. Ejercicio. 
##Programa  donde  el  usuario  "piensa"  un  número  del  1  al  100  y  el  ordenador  intenta 
##adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el 
##usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado).

print("Piensa un número del 1 al 100 y yo intentaré adivinarlo.")
bajo = 1
alto = 100
while True:
    intento = (bajo + alto) // 2
    respuesta = input(f"¿Es {intento}? (mayor/menor/igual): ")
    if respuesta == "igual":
        print(f"¡He adivinado tu número! Es {intento}.")
        break
    elif respuesta == "mayor":
        bajo = intento + 1
    elif respuesta == "menor":
        alto = intento - 1
    else:
        print("Por favor, responde con 'mayor', 'menor' o 'igual'.")
        continue
    