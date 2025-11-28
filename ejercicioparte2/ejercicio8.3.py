##8.  Ejercicio. 
##Programa que  lea 100 números no nulos y luego muestre un mensaje indicando cuántos 
##son positivos y cuantos negativos

contadorPositivos = 0
contadorNegativos = 0
for i in range(100):
    numero = int(input("Introduce un número no nulo: "))
    if numero > 0:
        contadorPositivos += 1
    else:
        contadorNegativos += 1

print(f"Has leído {contadorPositivos} números positivos y {contadorNegativos} números negativos.")