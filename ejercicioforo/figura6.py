n = int(input("Ingrese la dimensión de la figura (número entero positivo): "))
mitad = n // 2

for i in range(n):
    for j in range(n):
        
        if j == 0 or j == n - 1:
            print("*", end="")
        
        elif (i == j or i + j == n - 1) and i <= mitad:
            print("*", end="")
        else:
            print(" ", end="")
    print()