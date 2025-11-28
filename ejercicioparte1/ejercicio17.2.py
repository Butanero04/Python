##17. Ejercicio. 
##Escriba  un  programa  que  simule  un  inicio  de  sesión  solicitando  el  nombre  de  usuario  y 
##contraseña,  y  mostrar  un  mensaje  en  pantalla,  inicio  de  sesión  correcto/  nombre  de  usuario incorrecto 

usuario_correcto= "admin"
contrasena_correcta= "1234"

usuario= input("Introduce tu nombre de usuario: ")
contrasena= input("Introduce tu contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Inicio de sesion correcto")
else:
    print("Nombre de usuario incorrecto")
print("Fin del programa")