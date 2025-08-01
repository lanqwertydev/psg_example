print ("Tipos de booleanos")
print (True)
print (False)

# Si son subclase de los enteros  True = 1  False = 0

print (True + False)
print (True * False)
print (True * True)
print (False * False)

print (10 + True)

# == y is son diferentes
# == compara cantidad, is and is not compara objetos  uno compara numero de manzanas y el otro si son manzanas

#En variables

print ("Asignacion de variables")
x= 10
mayor_que_cero = x > 0
print (mayor_que_cero)
diferente_de_10 = x != 10
print (diferente_de_10)

print ("operadores logicos")

print (True and True)
print (True and False)
print (False or True)
print (False or False)
print (not True)
print (not False)

print ("20 es ")
numero = 20 > 0 and 20 < 100

print (numero)

nota1 = 15
nota2 = 20
nota3 = 16 

print ("apruebas?")
print (nota1 >= 59 and nota2 >= 50 and 16 >= 50)

print ("division 15 entre 3 y 5 pero no por 2" )

numero = 15


print ( numero )

print ((numero % 3 == 0 ) and numero % 5 == 0 and numero % 2 != 0)
