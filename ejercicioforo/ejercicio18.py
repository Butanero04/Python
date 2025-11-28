texto = "Abecedario"
consonantes = ""
vocales = "aeiouAEIOU"

for c in texto:
    # Si es letra Y NO es vocal
    if c.isalpha() and c not in vocales:
        consonantes += c

print("Solo consonantes:", consonantes)