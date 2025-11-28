texto = input("Introduce una frase: ")
vocales = "aeiouAEIOU"
contador = 0

for c in texto:
    if c in vocales: # Verifica si el carácter actual está en la cadena de vocales
        contador += 1

print("Número de vocales:", contador)