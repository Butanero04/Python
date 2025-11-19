
N= float(input("Ingrese su nota y le dire que nota alfabetica ha sacado: "))

if N < 3 :
    print("Has sacado un muy deficiente")
elif N > 3 and N < 5 :
    print("Has sacado un insuficiente")
elif N > 5 and N < 6 :
    print("Has sacado un suficiente")
elif N > 6 and N < 7 :
    print("Has sacado un bien")
elif N > 7 and N < 9 :
    print("Has sacado un notable")
else:
    print("Has sacado un sobresaliente")
    
print("Fin del programa")