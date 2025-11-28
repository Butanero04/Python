texto = "Aprender Python"
resultado = ""
vocales = "aeiouAEIOU"

for c in texto:
    if c in vocales:
        resultado += "*"
    else:
        resultado += c

print("Censurado:", resultado)