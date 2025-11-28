n= int(input("Ingrese la dimensión de la figura (número entero positivo): "))
mitad = n // 2

for i in range(n):
    for j in range(n):
        
        if i == mitad or j == mitad:
            print("*", end=" ")
        
        elif i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print(".", end=" ")
        
        else:
            print(" ", end=" ")
    print()