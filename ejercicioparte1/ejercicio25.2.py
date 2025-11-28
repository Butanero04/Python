##25. Ejercicio.
##La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el 
##postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre 
##el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el control switch). 
##Facultad	Importe de matrícula	Mensualidad Ing. de Sistemas	350	650 Derecho	300	550
##Ing. Naviera	300	500 Ing. Pesquera	310	460 Contabilidad	280	490 Administración	360	520

nombre_postulante = input("Ingrese el nombre del postulante: ")
facultad = input("Ingrese la facultad a estudiar (Ing. de Sistemas/Derecho/Ing. Naviera/Ing. Pesquera/Contabilidad/Administración): ")
importe_matricula = 0
mensualidad = 0
switcher = {
    "Ing. de Sistemas": (350, 650),
    "Derecho": (300, 550),
    "Ing. Naviera": (300, 500),
    "Ing. Pesquera": (310, 460),
    "Contabilidad": (280, 490),
    "Administración": (360, 520)
}
if facultad in switcher:
    importe_matricula, mensualidad = switcher[facultad]
else:
    print("Facultad no válida.")
igv = importe_matricula + mensualidad
monto_final = importe_matricula + mensualidad + igv
print(f"Nombre del postulante: {nombre_postulante}")
print(f"Facultad: {facultad}")
print(f"Importe de matrícula: {importe_matricula}")
print(f"Mensualidad: {mensualidad}")
print(f"IGV (18%): {igv}")
print(f"Monto final a pagar: {monto_final}")
print("Fin del programa")