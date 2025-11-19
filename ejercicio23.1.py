
positivo= 0
negativo= 0
N= 1

while N != 0:
    N= int(input("Introduce un número (0 para terminar): "))
    
    if N > 0:
        positivo += 1
    elif N < 0:
        negativo += 1

print(f"He leído {positivo} números positivos y {negativo} números negativos")