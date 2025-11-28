
n = int(input("Ingrese la altura de la figura (número entero positivo): "))



for i in range(n):
   
    print(" " * (n - 1 - i), end="")
    

    if i == 0:
        print("*")
    else:

        print("*" + " " * (2 * i - 1) + "*")


for i in range(n - 2, -1, -1):
    print(" " * (n - 1 - i), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")