n = int(input("Ingrese la altura de la figura (número entero positivo): "))

for i in range(n):
    
    print(" " * (n - 1 - i), end="")
    
    
    for j in range(2 * i + 1):
        
        if j == 0 or j == 2 * i:
            print("*", end="")
        
        elif i == n - 1:
            print("*", end="")
        
        elif i % 2 != 0 and j % 2 == 0:
            print("*", end="")
        
        else:
            print(" ", end="")
    print()