#20. Ejercicio. Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice su factura N! siendo el factorial

N= int(input("Introduce un numero positivo para calcular su factorial: "))

factorial=1
a=1

while a<=N:
    factorial=factorial*a
    a=a+1
print(f"El factorial de {N} es {factorial}")
print("Fin del programa")