##20. Ejercicio. 
##Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de 
##5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad 
##(utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible. 
##Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100 
##€, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque 
##sume 145 € no es el mínimo número de billetes posible).

euros = int(input("Introduce una cantidad de euros (múltiplo de 5): "))

billetes_500 = euros // 500
euros %= 500

billetes_200 = euros // 200
euros %= 200

billetes_100 = euros // 100
euros %= 100

billetes_50 = euros // 50
euros %= 50

billetes_20 = euros // 20
euros %= 20

billetes_10 = euros // 10
euros %= 10

billetes_5 = euros // 5
euros %= 5

print("Billetes necesarios:")
if billetes_500 > 0:
    print(f"{billetes_500} billete(s) de 500 €")    
if billetes_200 > 0:
    print(f"{billetes_200} billete(s) de 200 €")
if billetes_100 > 0:
    print(f"{billetes_100} billete(s) de 100 €")
if billetes_50 > 0:
    print(f"{billetes_50} billete(s) de 50 €")
if billetes_20 > 0:
    print(f"{billetes_20} billete(s) de 20 €")
if billetes_10 > 0:
    print(f"{billetes_10} billete(s) de 10 €")
if billetes_5 > 0:
    print(f"{billetes_5} billete(s) de 5 €")
if euros > 0:
    print(f"Sobran {euros} € que no se pueden representar con billetes de 5 €.")

