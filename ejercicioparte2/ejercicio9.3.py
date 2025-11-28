##9.  Ejercicio. 
##Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego 
##muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos. 

contadorPositivos = 0
contadorNegativos = 0  
haLeidoNegativo = False

while True:
    numero = int(input("Introduce un número no nulo: "))
    if numero == 0:
        break
    if numero > 0:
        contadorPositivos += 1
    else:
        contadorNegativos += 1
        haLeidoNegativo = True

if haLeidoNegativo:
    print("Has leído algún número negativo.")
else:
    print("No has leído ningún número negativo.")

print(f"Has leído {contadorPositivos} números positivos y {contadorNegativos} números negativos.")