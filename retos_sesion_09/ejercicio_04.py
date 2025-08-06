productos = ["Leche", "Pan", "Sardina", "huevo"]
precios = [7, 2, 8, 2]

productos.append("Arroz") 
productos.append("Mantequilla") 
productos.append("Mayonesa") 
productos.append("Palta") 
productos.append("comino")
print(productos)

precios.append(7)
precios.append(8)
precios.append(9)
precios.append(10)
precios.append(45)
print (precios)

precios.remove(7)
productos.remove("Leche")

print ("el precio del pan es " + str(precios[0]))
print("el precio del huevo es " + str(precios[2]))

print (max(precios))
print (min(precios))

print (len(productos))

print(sum(precios))

precios.sort
print (precios)
productos.sort
print(productos)

precios.clear()
print (precios)
productos.clear()
print(productos)
