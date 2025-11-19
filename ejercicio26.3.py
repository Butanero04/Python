#Dibuja un ordinograma que calcula el salario neto semanal de un trabajador en función del  número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:  Las primeras 35 horas se pagan a tarifa normal.  Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.  Las tasas de impuesto son:  Los primeros 500€ son libres de impuestos.  Los siguientes 400€ tiene un 25% de impuesto.  Los restantes un 45% de impuesto.  Escribe el nombre del trabajador, salario bruto, tasas y salario neto.

horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))

tarifa_hora = float(input("Introduce la tarifa por hora: "))   
 
if horas_trabajadas > 35:
    salario_bruto = (35 * tarifa_hora) + ((horas_trabajadas - 35) * tarifa_hora * 1.5)
else:
    salario_bruto = horas_trabajadas * tarifa_hora
if salario_bruto <= 500:
    salario_neto = salario_bruto
    tasa_impuesto = 0
elif salario_bruto <= 900:
    salario_neto = salario_bruto - (salario_bruto * 0.25)
    tasa_impuesto = 0.25
else:
    salario_neto = salario_bruto - (salario_bruto * 0.45)
    tasa_impuesto = 0.45
    
nombre_trabajador = input("Introduce el nombre del trabajador: ")
print(f"Nombre del trabajador: {nombre_trabajador}")
print(f"Salario bruto: {salario_bruto}€")
print(f"Tasa de impuesto: {tasa_impuesto * 100}%")
print(f"Salario neto: {salario_neto}€")

print("Fin del programa")