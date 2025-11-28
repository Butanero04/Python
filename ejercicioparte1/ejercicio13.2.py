##13.ejercicio. 
##Escriba un programa que lea dos números y lo visualiza en orden ascendente.

n1= float(input("Introduce el primer numero: "))
n2= float(input("Introduce el segundo numero: "))

if n1 > n2:
    print(n2, n1)
else:
    print(n1, n2)
print("Fin del programa")