##17. Ejercicio. 
##Programa que suma independientemente los pares y los impares de los números 
##comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas. 

suma_pares = 0
suma_impares = 0

for i in range(100, 201):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print("La suma de los números pares entre 100 y 200 es:", suma_pares)
print("La suma de los números impares entre 100 y 200 es:", suma_impares)