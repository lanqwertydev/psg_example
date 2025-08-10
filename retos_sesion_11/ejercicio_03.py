tupla = (("perro", 1), ("gato", "2"), ("aves", [6, 7]))


diccionario = dict(tupla)

print (diccionario)

aves = diccionario.pop("aves")

print (aves)
print (diccionario)

diccionario["gato"] = 3
print (diccionario)