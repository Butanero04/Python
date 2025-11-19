negativo = 0
contador = 0

while contador <= 100:
    N = int(input(f"Introduce el número {contador + 1} (no puede ser cero): "))
    
    if N == 0:
        print("No se permiten números nulos (cero). Intenta de nuevo.")
        continue
    
    if N < 0:
        negativo += 1
    
    contador += 1

if negativo > 0:
    print(f"He leído {negativo} números negativos")
else:
    print("No he leído ningún número negativo")
    