texto = "programacion"
repetidos = ""

for i in range(len(texto)):
    caracter = texto[i]
    conteo = 0
    
    # Ciclo anidado para contar cuántas veces aparece este caracter en todo el texto
    for x in texto:
        if x == caracter:
            conteo += 1
            
    # Si aparece más de 1 vez Y no lo hemos guardado ya en 'repetidos'
    if conteo > 1:
        # Verificación manual si ya está en repetidos para no duplicarlo en el resultado
        ya_esta = False
        for r in repetidos:
            if r == caracter:
                ya_esta = True
        
        if not ya_esta:
            repetidos += caracter

print("Caracteres repetidos:", repetidos)