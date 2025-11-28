texto = input("Texto en minúsculas: ")
resultado = ""

for c in texto:
    # Si el carácter está entre 'a' y 'z'
    if 'a' <= c <= 'z':
        # Restamos 32 al valor ASCII para obtener la mayúscula
        codigo_ascii = ord(c) - 32
        resultado += chr(codigo_ascii)
    else:
        resultado += c

print("Mayúsculas:", resultado)