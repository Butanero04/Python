texto = "Clave1234Hola9"
contador = 0

for c in texto:
    if '0' <= c <= '9':
        contador += 1

print(f"Hay {contador} números en la cadena.")