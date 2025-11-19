#19. Ejercicio. Dibuja un ordinograma de un programa que lea tres números y nos diga cual es mayor, cual menor y cuales son iguales.

n1=int(input("Introduce el primer numero: "))
n2=int(input("Introduce el segundo numero: "))
n3=int(input("Introduce el tercer numero: "))

if n1==n2==n3:
    print("Los numeros son iguales")
elif n1==n2:
    print(f"{n1} y {n2} son iguales")   
    if n3>n1:
        print(f"{n3} es el mayor")
    else:
        print(f"{n1} es el mayor")
elif n1==n3:
    print(f"{n1} y {n3} son iguales")
    if n2>n1:
        print(f"{n2} es el mayor")
    else:
        print(f"{n1} es el mayor")
elif n2==n3:
    print(f"{n2} y {n3} son iguales")
    if n1>n2:
        print(f"{n1} es el mayor")
    else:
        print(f"{n2} es el mayor")
else:
    if n1>n2 and n1>n3:
        print(f"{n1} es el mayor")
    elif n2>n1 and n2>n3:
        print(f"{n2} es el mayor")
    else:
        print(f"{n3} es el mayor")
        
print("Fin del programa")