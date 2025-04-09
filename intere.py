prestamo = int(input("Dime el valor del prestamo: "))
interes = float(input("Dime el interes: "))
tot = prestamo + (prestamo * interes / 100)
print(f"El total a pagar es: {tot}")