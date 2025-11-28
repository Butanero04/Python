##15. Ejercicio.  Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos 
##la altura de la pirámide por teclado.

altura = int(input("Introduce la altura de la pirámide invertida: "))
for i in range(altura, 0, -1):
    
    for j in range(altura - i):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        print("*", end="")
    print()
