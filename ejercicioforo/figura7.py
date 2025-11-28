n = int(input("Ingrese la altura de la figura (número entero positivo): "))


for i in range(n - 1, -1, -1):
    
    print(" " * (n - 1 - i), end="")
    

    if i == n - 1: 
        print("*" * (2 * i + 1))
    elif i == 0:   
        print("*")
    else:
        
        linea = "*"
       
        for k in range(2 * i - 1):
            
            if i % 2 != 0: 
                if k % 2 == 0: 
                    linea += " "
                else: 
                    linea += "*"
            else:
                linea += " "
      
        linea += "*"
        print(linea)