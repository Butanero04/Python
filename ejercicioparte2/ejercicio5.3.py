##Programa que muestre en líneas separadas lo siguiente: ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA, 
##WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A. 

abecedario = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
longitud = len(abecedario)

for i in range(longitud):
    print(abecedario[i:])   

