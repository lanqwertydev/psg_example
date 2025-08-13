print ("Diccionarios")

print ("Mutables, no ordenados, indexados")

diccionario = {"perro" : 1, "gato" : 2, "ave" : 3}

print (diccionario)

print ("diccionarios vacios")

diccionario_vacio = dict()  # O simplemente usando {}

print (diccionario_vacio)

print ("Diccionario a partir de una lista anidada")

lista_anidada = [["perro", 1], ["gato", 2], ["pez", 3]]   #Tienen que ser pares o dara errores
print (lista_anidada)
diccionario_lista_anidada = dict(lista_anidada)
print (diccionario_lista_anidada)

print ("Diccionario a partir de una tupla sigue las mismas reglas")

print ("Indexacion y Slicing")

print(diccionario["gato"])

print ("tambien puedes cambiar el valor de la clave")

diccionario["perro"] = 4
print (diccionario)
print ("Si no existe la clave, se genera una nueva")
diccionario["pez"] = 5

print (diccionario)

print ("del , se usa para eliminar")
del diccionario["ave"]
print (diccionario)

print ("Concatenacion de diccionarios")
print ("No se puede concatenar con + ni repetir con *")


print ("Metodos de adicion")
print ("Metodos de acceso")

perrito = diccionario.get("perro")
print (perrito)

print ("items")                #Pueden servir para ver el lugar de los elementos de un diccionario
items = diccionario.items()
print (items)
items = list(items)
print (items)
print (items[1], type(items[1]))

print ("Keys te devuelve una lista de claves") 
claves = diccionario.keys()
print (claves, type(claves))
claves = list(claves)
print (claves, type (claves))

print ("values() te devuelve una lista con los valores del diccionrio")
valores = diccionario.values()
print (valores, type(valores))
valores = list(valores)
print (valores, type(valores))

print ("Metodos de adicion")
print ("update(diccionario)")
diccionario.update({"ave":2, "perro":7})
print (diccionario)

print ("Metodos de eliminacion")
print ("metodo clear() vacia el diccionario")
print ("metodo pop()")
elgato = diccionario.pop("gato")
print (diccionario)

print ("popitem() elimina el ultimo item si esta vacio da error")
diccionario.popitem()
print (diccionario)

print ("copia")

copia = diccionario.copy()

print (copia)

print ("Funciones en diccionarios")

print (len(diccionario))
print ("perro" in diccionario)
print ("perro" not in diccionario)

iterador = iter(diccionario.items())   #el iterador es una manera de recorrer el codigo
siguiente = next(iterador)
print (siguiente)
siguiente = next(iterador)
print (siguiente)


