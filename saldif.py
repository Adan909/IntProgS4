nomb = str(input("Dime tu nombre: "))
Apell=  str(input("Dime tu apellido: "))
hortrab = float(input("Dime las horas trabajadas: "))
prechor = int(input("Cuanto ganas por hora?: "))
sueld_bruto = hortrab * prechor
IR = (hortrab * prechor) * 0.05
sueldo = (hortrab * prechor) - IR
print(f"Hola {nomb} {Apell}, tu sueldo bruto es de {sueld_bruto} \nDescontando el ir, en total seria {IR} \nTu sueldo total seria de {sueldo} ")
print("Gracias por usar el programa")