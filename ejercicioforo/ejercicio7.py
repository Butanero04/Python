texto = "gato"
viejo = "g"
nuevo = "p"
resultado = ""

for c in texto:
    if c == viejo:
        resultado += nuevo
    else:
        resultado += c

print(f"De '{texto}' a '{resultado}'")