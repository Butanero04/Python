
from math import pi

longitudr= float(input("Introduce la longitud del radio y te dare la longitud de la cincurferencia, el area del circulo y el volumen de la esfera: "))

diametro= longitudr * 2

longitudc= pi * longitudr

area= pi * (longitudr ** 2)

volumen= (4/3) * pi * (longitudr ** 3)

print("El diametro es: ", diametro)
print("La longitud de la circunferencia es: ", longitudc)
print("El area del circulo es: ", area)
print("El volumen de la esfera es: ", volumen)