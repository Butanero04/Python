##20. Ejercicio. 
##Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la 
##calificación alfabética, escribiendo el siguiente resultado (switch). • De 0 a < 3 Muy Deficiente. • De 3 a < 5 Insuficiente. 
##• De 5 a < 6 Suficiente. • De 6 a < 7 Bien. • De 7 a <9 Notable. • De 9 a 10 Sobresaliente.

def calificacion_alfabetica(numerica):
    if 0 <= numerica < 3:
        return "Muy Deficiente"
    elif 3 <= numerica < 5:
        return "Insuficiente"
    elif 5 <= numerica < 6:
        return "Suficiente"
    elif 6 <= numerica < 7:
        return "Bien"
    elif 7 <= numerica < 9:
        return "Notable"
    elif 9 <= numerica <= 10:
        return "Sobresaliente"
    else:
        return "Calificación inválida"

calificacion = float(input("Ingrese una calificación numérica entre 0 y 10: "))
resultado = calificacion_alfabetica(calificacion)
print("La calificación alfabética es:", resultado)
print("Fin del programa")