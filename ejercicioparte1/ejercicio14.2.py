##14. Ejercicio. 
##Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales.

n1= float(input("Introduce el primer numero: "))
n2= float(input("Introduce el segundo numero: "))

if n1 > n2:
    print(n1, "es el mayor")
elif n1 < n2:
    print(n2, "es el mayor")
else:
    print("Son iguales")
print("Fin del programa")