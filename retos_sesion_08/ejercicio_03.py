cadena = input ("Ingrese su palabra: ")

tupla = (cadena, )

nueva_tupla = (("¡",) +tupla + ("!",))

print (nueva_tupla)
print (nueva_tupla * 3)