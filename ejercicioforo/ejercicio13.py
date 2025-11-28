texto = "  Hola   mundo  "
sin_espacios = ""

for c in texto:
    if c != " ":
        sin_espacios += c

print(f"Continua: {sin_espacios}")