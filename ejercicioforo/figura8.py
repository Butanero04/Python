n = int(input("Ingrese la altura de la figura (número entero positivo): "))


for i in range(n):
    espacios = " " * (n - 1 - i)
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)


for i in range(n - 2, -1, -1):
    espacios = " " * (n - 1 - i)
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)