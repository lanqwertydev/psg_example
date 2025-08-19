edad = int(input("Cuantos años tienes?: "))
compra = int(input("El costo de tu compra: "))
if edad >= 18:
    if compra > 1000:
        print ("Usted recibe un descuento del 10%")
    else:
        print("obtuviste un descuento del 2%")
else:
    if compra > 500:
        print ("Obtuviste un descuento del 5%")
    else:
        print ("Obtuviste un descuento del 2%")

