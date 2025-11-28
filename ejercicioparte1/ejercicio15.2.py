#15. Ejercicio. Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales son iguales

n1= float(input("Introduce el primer numero: "))
n2= float(input("Introduce el segundo numero: "))
n3= float(input("Introduce el tercer numero: "))

if n1 > n2 and n1 > n3:
    print(n1, "es el mayor")
    if n2 < n3:
        print(n2, "es el menor")
        print(n3, "es el medio")
    else:
        print(n3, "es el menor")
        print(n2, "es el medio")
elif n2 > n1 and n2 > n3:
    print(n2, "es el mayor")
    if n1 < n3:
        print(n1, "es el menor")
        print(n3, "es el medio")
    else:
        print(n3, "es el menor")
        print(n1, "es el medio")
elif n3 > n1 and n3 > n2:
    print(n3, "es el mayor")
    if n1 < n2:
        print(n1, "es el menor")
        print(n2, "es el medio")
    else:
        print(n2, "es el menor")
        print(n1, "es el medio")
else:
    print("Son iguales")
print("Fin del programa")