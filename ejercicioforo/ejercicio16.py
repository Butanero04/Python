cadena1 = "Frente"
cadena2 = "Alto"

resultado = cadena1 # Empezamos con la primera

# Recorremos la segunda y pegamos letra a letra
for c in cadena2:
    resultado += c

print("Concatenación manual:", resultado)