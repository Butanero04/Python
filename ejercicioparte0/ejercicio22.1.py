positivo=0
negativo=0
contador=0

while contador <= 100:
    N=int(input(f"Introduce el numero {contador+1}: "))
    
    if N==0:
        print("No se permiten numeros nulos (cero). Intenta de nuevo.")
    
        continue
    if N>0:
        positivo+=1
    else:
        negativo+=1
        
        
    contador= contador + 1   
    
        
print(f"He leido {positivo} numeros positivos y {negativo} numeros positivos")