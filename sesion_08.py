## Tuplas

## no es necesario el uso de parentesis pero si es una buena practica. se usan , para separarlas

mi_tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5)

print (mi_tupla)

#funcion Tuple

prueba = tuple("hola")  #separa cada cadena en un indice

print (prueba)

print (prueba[2])

tupla_mixta = (1, 2, "yes", True)

print (tupla_mixta[3], type (tupla_mixta[3]))

print (tupla_mixta[-1])

print (tupla_mixta[1:3:])

print (mi_tupla[0:5:])  #slicing en tuplas  Se excluye el 5

nueva_tupla = (10, 11, 12)
suma_de_tupla = (mi_tupla + nueva_tupla)
print(suma_de_tupla)

abecedario = ("a", "b", "c", "d", "e")
primera_letra, segunda_letra, tercera_letra, cuarta_letra, quinta_letra= abecedario   #asignacion multiple de valores
print (abecedario)   #debe coincidir el numero de indices

print (primera_letra)

print (mi_tupla.count(5))
print(nueva_tupla.index(11))

print("Funciones en las tuplas")

print(len(abecedario))

print (max(abecedario))
print (min(mi_tupla))
print (sum(suma_de_tupla))

print ("tuplas anidadas")
tupla_anidada = (1, 2, 3, (4, 5, 6,))
print (tupla_anidada[3][1])