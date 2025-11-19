
numero1= int(input("Introduce el primer numero: "))
numero2= int(input("Introduce el segundo numero: "))        


    
suma = numero1 + numero2
resta = numero1 - numero2       
multiplicacion = numero1 * numero2

if numero2!=0 or numero1!=0:
    division = numero1 / numero2
else:
    print("Error: No se puede dividir entre cero.")
    exit()


print("La suma es:", suma , "la resta es", resta , "la multiplicacion es", multiplicacion , "y la division es", division)