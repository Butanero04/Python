##21. Ejercicio. 
##Escriba un programa que  calcula el salario neto semanal de  un trabajador en función del 
##número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis: 
##• Las primeras 35 horas se pagan a tarifa normal. 
##• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal. 
##• Las tasas de impuesto son: 
##o Los primeros 500€ son libres de impuestos. 
##o Los siguientes 400€ tiene un 25% de impuesto. 
##o Los restantes un 45% de impuesto. 
##Escribe el nombre del trabajador, salario bruto, tasas y salario neto. 

def calcular_salario_neto(horas_trabajadas, tarifa_hora):
    if horas_trabajadas <= 35:
        salario_bruto = horas_trabajadas * tarifa_hora
    else:
        horas_extra = horas_trabajadas - 35
        salario_bruto = (35 * tarifa_hora) + (horas_extra * tarifa_hora * 1.5)

    if salario_bruto <= 500:
        impuesto = 0
    elif salario_bruto <= 900:
        impuesto = (salario_bruto - 500) * 0.25
    else:
        impuesto = (400 * 0.25) + ((salario_bruto - 900) * 0.45)

    salario_neto = salario_bruto - impuesto
    return salario_bruto, impuesto, salario_neto
nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
tarifa_hora = float(input("Ingrese la tarifa por hora: "))

salario_bruto, impuesto, salario_neto = calcular_salario_neto(horas_trabajadas, tarifa_hora)

print("Nombre del trabajador:", nombre)
print("Salario bruto:", salario_bruto)
print("Tasas de impuesto:", impuesto)
print("Salario neto:", salario_neto)
print("Fin del programa")