##26. Ejercicio.  En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados: 
##Si los tres dados son seis, mostrar el mensaje “Excelente”  Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”  Si un dado se obtiene seis, mostrar el mensaje “Regular” 
##Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”  (Use el control switch).  

dado1 = int(input("Ingrese el valor del primer dado (1-6): "))
dado2 = int(input("Ingrese el valor del segundo dado (1-6): "))
dado3 = int(input("Ingrese el valor del tercer dado (1-6): "))
seis_count = 0
if dado1 == 6:
    seis_count += 1
if dado2 == 6:
    seis_count += 1
if dado3 == 6:
    seis_count += 1
switcher = {
    3: "Excelente",
    2: "Muy bien",
    1: "Regular",
    0: "Pésimo"
}
mensaje = switcher.get(seis_count, "Error en la entrada de dados")
print(f"Resultado: {mensaje}")
print("Fin del programa")

