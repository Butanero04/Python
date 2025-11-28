texto = "HoLa MunDo"
contador = 0

for c in texto:
    # Comparamos rangos de caracteres directamente
    if 'A' <= c <= 'Z':
        contador += 1

print(f"Hay {contador} letras mayúsculas.")