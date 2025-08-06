print ("Lista de enteros")
mi_lista = [1, 2, 3, 4, 5]
print (mi_lista)

lista_mixta = [1, "hola", 3.14, "mundo", 5]
lista_vacia = []

nueva = list("Hola Mundo")
print (nueva)

tupla = (1, 2, 3, 4)
listtupla = list (tupla)
print (type(listtupla)) 

lista = listtupla[:2:]
print (lista)

listamixta = mi_lista + nueva   # concatenar listas
print (listamixta)

print ("Metodos de lista")

caja = ("manzana", 1, "platano", 3, 4, 5, 6, "manzana", 3, 3, "uva")

print("metodos de busqueda")
print (caja.index("platano"))    #index busca

print (caja.count("manzana"))
print (caja.count(3))

print ("metodos de adición")

listtupla.insert(3, "cinco")   #insert() no edita un indice, hace un espacio
print(listtupla)

listtupla.append(6)   #agarra el valor y lo añade al final de la lista
print(listtupla)

print ("extend")
listtupla.extend(":3")    #amplia la lista con estructuras o cadenas
listtupla.extend(caja)
print (listtupla)

print ("metodos de eliminacion")
listtupla.remove("manzana")   #.remove() solo elimina la primera aparicion del valor
print(listtupla)

basura = listtupla.pop(2)  #saca el indice 2
print (listtupla)          #
basura = listtupla.pop()   # saca el ultimo elemento
print (basura)

print ("metodos de ordenamiento")

numeros = [8, 9, 4, 1, 2, 3, 4, 5, 6]
numeros.sort()
print (numeros)
numeros.sort(reverse=True)
print (numeros)

numeros2 = [2, 5, 7, 3, 1, 0]
numeros2.reverse()               #lo ordena alrevez
print (numeros2)

numeros3 = numeros2[:]   #copy()
numeros3[0] = 4
print (numeros3)
print (numeros2)

print("Funciones con listas")
print(len(numeros2))
print(max(numeros2))
print(min(numeros2))
print(sum(numeros2))

print("comparacion de listas")

print("in, not in")

print (3 in numeros3)
print (4 in numeros2)
print ("not in")
print (3 not in numeros3)
print (4 not in numeros2)
print ([5, 7, 3] in numeros2)  #error

print (lista is not numeros2)
print (numeros is numeros)

lista1 = [23, 45, 67, 12]
lista2 = [2, 3, 4, 5, 6]
lista3 = [2, 3, 4, 5, 6]
print ("listas de comparacion")
print ([23, 45, 67, 12] == [2, 3, 4, 5, 6])
print ([2, 3, 4, 5, 6] != [2, 3, 4, 5, 6])
print ([23, 45, 67, 12] > [2, 3, 4, 5, 6])
print ([2, 3, 4, 5, 6] >= [2, 3, 4, 5, 6])

print(lista1 == lista2)