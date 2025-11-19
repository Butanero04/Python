n1=int(input("Introduce un numero para decirte cual es el mayor o si son iguales: "))
n2=int(input("Introduce otro numero para decirte cual es el mayor o si son iguales: "))

if n1==n2:
    print(f"Los numeros {n1} y {n2} son iguales")
elif n1>n2:
    print(f"{n1} es mayor que {n2}")
else:
    print(f"{n2} es mayor que {n1}")
    
print("Fin del programa")