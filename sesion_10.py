print ("conjuntos")

print ("Mutables, no ordenados no duplicados")

enteros  = {1, 2, 3, 4, 5}
print (enteros)
cadenas = {"salteña", "papas", "mayonesa", "kepchu", "lechuga"}
print (cadenas)
conjunto_mixto = {True, 1, 3, "mana"}   #True es tomando como 1
print (conjunto_mixto)

print ("conjuntos vacios")
conjunto_vacio = set()
print (conjunto_vacio)

print ("Conjunto a partir de una cadena")
cadena = "Hola perras"

hola = set(cadena)
print (hola)

tupla = ("asl menos la se usar", 2, 34)

latupla = set(tupla)
print(latupla)

print ("Conjuntos por comprension")
compresion = {x for x in "manza" "pera" "drogas" "manza" "pera"}
print (compresion)

print ("metodos de adicion")
print (cadenas)
cadenas.add("platano")
print(cadenas)

cadenas.update(["soda", "helado"])   #update es para listas, mas de un conjunto
print (cadenas)

print ("Metodos de eliminación")

cadenas.remove("soda")  #Remove va a fallar si no encuentra el valor

cadenas.discard("soda")  #No da error si no lo encuentra

print (cadenas.pop()) #saca una aleatoria

print ("Metodo .clear( elimina todos los elementos)")

print ("Metodos de operaciones")

print ("union")
union = enteros.union(cadenas) 
print (union)

print ("intersection")
enteros2 = {5, 6, 7, 8, 9}
interseccion = enteros.intersection(enteros2)   #Devuelve el valor que se repite en ambos conjuntos
print (interseccion)

diferencia = enteros.difference(enteros2)
print (diferencia)
diferencia2 = enteros2.difference(enteros)
print (diferencia2)
print ("diferencia simetroca")
diferencia_simetrica = enteros.symmetric_difference(enteros2)
print (diferencia_simetrica)

print ("asignacion con operadores")
enteros.intersection_update(enteros2)  #Asigna el valor de la interseccion al primer conjunto
print (enteros)

enteros.difference_update(enteros2)  #Asigna la diferencia en el primer conjunto
print (enteros)

print ("difference update")
numeros1 = {1, 2, 3, 4}
numeros2 = {1, 2, 4, 5}   #lo que hay en el primero pero no en e segun se guarda en el primero
numeros1.difference_update(numeros2)
print (numeros1)

print ("Symetric difference update")
numeros3 = {3, 6, 7, 2}
numeros3.symmetric_difference_update(numeros2)
print (numeros3)  


print ("Métodos de busqueda")
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {6, 7, 8, 9, 10}
conjunto3 = {6, 7, 9}

print (conjunto3.issubset(conjunto2))   #Los valores del conjunto 3 estan en el conjunto 2?

print (conjunto3.issuperset(conjunto2)) #lo mismo pero al revez. el conjunto 3 contiene al conjunto 2?

print (conjunto1.isdisjoint(conjunto3)) #Los conuntos no contienen valores en comun? True

print ("Métodos de copia")
copia = conjunto1.copy()
print (copia)

print (len(conjunto1))
print (max(conjunto1))
print (min(conjunto1))
print (sum(conjunto1))

print ("Operadores con conjuntos")
print ("operadores de adicion")

conjunto1 |= conjunto2
print (conjunto1)

print (conjunto1 == conjunto2)
print(conjunto1 != conjunto3)
print (conjunto1 < conjunto3) # conjunto 1 esta en conjunto 3?
print (conjunto1 < conjunto3)
print (conjunto1 > conjunto3)
print (conjunto1 >= conjunto3)

print ("Operadores para operaciones con conjuntos")
conjunto4 = {11, 12, 13}

union = conjunto1 | conjunto4   #basciamente suma los conjuntos
print (union)
interseccion = conjunto1 & conjunto2
print (interseccion)
diferencias = conjunto1 - conjunto4
print (diferencias)

difersimetric = conjunto1 ^ conjunto4
print (difersimetric)

print ("operadores con asignacion con operadores")
print ("Basicamente lo mismo que el anterior pero asignando el valor al primero")

print ("conjuntos anidados se pueden si el contenido de conjuntos sean frozenset()")

