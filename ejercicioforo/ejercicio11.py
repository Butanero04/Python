texto = "Murcielago"
resultado = ""
vocales = "aeiouAEIOU"

for c in texto:
    if c in vocales:
        resultado += c + c  # Concatenamos dos veces
    else:
        resultado += c

print("Resultado:", resultado)