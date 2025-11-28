texto = "Roma"
invertida = ""

for c in texto:
    # Ponemos el carácter NUEVO antes de lo que ya teníamos
    invertida = c + invertida 

print(f"Original: {texto} | Invertida: {invertida}")