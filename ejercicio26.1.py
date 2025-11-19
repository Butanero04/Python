H= float(input("Ingrese el número de horas trabajadas: "))
C= float(input("Ingrese el costo por hora: "))


if H > 35:
    SalarioNeto = 35 * C + (H - 35) * C * 1.5
else:
    SalarioNeto = H * C

if SalarioNeto < 500:
    print (f"El salario neto es:, {SalarioNeto}")
elif SalarioNeto < 900:
    A = (SalarioNeto - 500) * 0.25
    SalarioNeto= A + SalarioNeto
    print (f"El salario neto es:, {SalarioNeto}")
elif SalarioNeto >= 900:
    B = (SalarioNeto - 500) * 0.25
    C = (SalarioNeto - 900) * 0.45 
    
    SalarioNeto= B + C + SalarioNeto
    
    
    



