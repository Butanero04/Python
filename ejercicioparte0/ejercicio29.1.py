##29. Ejercicio. 
##Dibuja un ordinograma de un programa donde el usuario “piensa” un número del 1 al 100 
##y el ordenador intenta  adivinarlo. Es  decir, el ordenador irá proponiendo números una y otra 
##vez  hasta  adivinarlo  (El  usuario  deberá  indicarlo  al  ordenador  si  es  mayor  o  menor  o  igual  al 
##número pensado).

print("Piensa un numero entre 1 y 100 y yo intentare adivinarlo.")

minimo = 1
maximo = 100
intentos = 0

while True:
    intentos += 1
    numero = (minimo + maximo) // 2
    respuesta = input(f"¿Es {numero}? (mayor/menor/igual): ")   

    if respuesta == "igual":
        print(f"¡He adivinado tu numero {numero} en {intentos} intentos!")
        break
    elif respuesta == "mayor":
        minimo = numero + 1
    elif respuesta == "menor":
        maximo = numero - 1
    else:
        print("Por favor, responde con 'mayor', 'menor' o 'igual'.")
print("Fin del programa")