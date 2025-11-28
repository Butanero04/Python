##16. Ejercicio. 
##Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene.

num= int(input("Introduce un numero entre 0 y 99999: "))
if num < 0 or num > 99999:
    print("El numero no esta en el rango solicitado.")
else:
    print("El numero tiene", len(str(num)), "cifras.")
print("Fin del programa")
