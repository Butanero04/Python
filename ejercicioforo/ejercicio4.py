texto = "banana"
nueva_cadena = ""

for c in texto:
    if c != "a":
        nueva_cadena += c  # Añadimos solo si no es 'a'

print(f"Original: {texto}")
print(f"Filtrada: {nueva_cadena}")