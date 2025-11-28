
n= int(input("Ingrese la dimensión de la figura (número entero positivo): "))
mitad = n // 2

for i in range(n):
    for j in range(n):
       
        if i == mitad or j == mitad or i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  