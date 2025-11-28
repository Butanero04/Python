##19. Ejercicio. 
##Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares, 
##con el siguiente menú de opciones:    Bienvenido a su Cajero Virtual 1. Ingresar dinero en cuenta 2. Retirar dinero de la cuenta 3. Salir

saldo= 1000
print("Bienvenido a su Cajero Virtual")
print("1. Ingresar dinero en cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Salir")
opcion= int(input("Introduce una opcion: "))
if opcion == 1:
    ingreso= float(input("Introduce la cantidad a ingresar: "))
    saldo += ingreso
    print("El saldo actual es:", saldo)
elif opcion == 2:  
    retiro= float(input("Introduce la cantidad a retirar: "))
    if retiro > saldo:
        print("No hay suficiente saldo en la cuenta")
    else:
        saldo -= retiro
        print("El saldo actual es:", saldo)
elif opcion == 3:
    print("Gracias por usar su Cajero Virtual")
else:
    print("Opcion incorrecta")
print("Fin del programa")