texto = input("Introduce texto: ")
caracter_buscar = input("¿Qué carácter buscas? ")
contador = 0

for c in texto:
    if c == caracter_buscar:
        contador += 1

print(f"El carácter '{caracter_buscar}' aparece {contador} veces.")