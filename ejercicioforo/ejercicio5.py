texto = "Python"
buscar = "y"
encontrado = False

for c in texto:
    if c == buscar:
        encontrado = True
        break  # Dejamos de buscar si lo encontramos

if encontrado:
    print(f"El carácter '{buscar}' ESTÁ en la cadena.")
else:
    print(f"El carácter '{buscar}' NO está en la cadena.")