#27. Ejercicio. Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que 
#van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.

notas = []
while True:
    nota = float(input("Introduce una nota (o -1 para terminar): "))
    if nota == -1:
        break
    notas.append(nota)  

if 10 in notas:
    print("Hubo al menos una nota con valor 10.")
else:
    print("No hubo ninguna nota con valor 10.")
    
print("Fin del programa")

