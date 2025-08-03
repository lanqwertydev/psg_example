
# comilllas_simples = 'una linea'
# comillas_dobles = "una linea"

# comillas_simples_triple = '''mas 
#                              de
#                              1 
#                             linea'''
# comillas_dobles_triple = """ mas de 
#                             1 linea"""

# print (type(str(20) ))

# #str convierte en cadena (string)

# # Escape de caracteres
# print ("el mensaje fue \" I\'m a message\"")  # \ Para usar caracteres especiales sin que errores

# print (" este mensaje esta para probar... \
#        este atributo del \\")

# print ("este \n\t este mensaje es para probar usos del \\ como caracteres especiales")

# ## Entrada input

# entrada = input("Ingrese un valor")

# print (entrada)

# print (type(int(entrada)))


# IMPORTANTE CRTL + K + C COMENTA TODOO
# Y CTR + K + U DESCOMENTA

## la entrada debe ser logica, no puedes convertir a int un float
## Los booleanos todo es True excepto el 0

## Manejo de indices

fruta = "banana"

print (fruta[2])    # Se empieza del 0

print (fruta[-6])  #los indices tambien pueden ser negativos y el ultimo indice sera -1

print ("Slicing")

ciudad = "La-Paz-Bolivia"

print (ciudad)
print("Slicing con indices positivos")
print (ciudad[0:6])
print (ciudad[0:6:2])  # el 2 es para saltar

print ("Slicing con indices negativos")

print (ciudad[-11:-2])

print (ciudad[:6])  #se puede dejar en blanco una parte para dar a entender todo el contenido

print ("Concatenacion de cadenas")

cadena1 = "hola "
cadena2 = "mundo"

print (cadena1 + " " + cadena2)

print ("Repiticion de cadenas")
cadena = "-#-"

repetida = cadena * 10

print (cadena * 10)

print (len(repetida))   #len mide la longitud de la cadena

##Metodos de cadenas

print ("Metodo cadenas")
ejemplo = "cadenas_0"

print (ejemplo.upper()) ##convierte en mayusculas

minuscula = "CADENAS"

print (minuscula.lower()) # convierte en minusculas

print (ejemplo.capitalize()) # Devuelve con la primera letra en mayuscula

ejemplo_2 = "las personAs dueRmEn en sUs caMas en 2"

print (ejemplo_2.title())  # La primera letrA de cAda paLabra sera mayuscula

print (ejemplo_2.swapcase())  # Invierte las mayusculas y minusculas

print (ejemplo_2.count("a"))  # cuenta cuantas veces se repiten

print (ejemplo_2.find("en"))  #busca el indice de la palabra a buscar de izquierda a derecha

print (ejemplo_2.rfind("en"))  # busca de derecha a izquierda

digito = 72
print (digito)
resultado = str(digito).isdigit()  # .isdigit() revisa si todos los caracteres son enteros
print (resultado)

print(ejemplo_2.isalpha())  # .isalpha() revisa si todos son str

print (ejemplo_2.isalnum())  #revisa si contienen solo letras y numeros

print (ejemplo_2.split( )) #separa las cadenas usando de metrica lo que haya en ()

abecedario = "abcdef"
print("-".join(abecedario))  #combina cadenas

print (ejemplo_2.strip("las"))  # elimina los valores dados de ambos lados (no del centro)

print (ejemplo_2.replace("en", "cambio"))  #reemplaza el antes de "," con el despues


ejemplo3 = "el valor de pi es {}"  #.format() busca el {} y le pone valor, le da formato
print (ejemplo3.format(3.1416))

ejemplo4 = "{2} es el resultado de sumar {0} y {1}"   #Para formatear varios 
print(ejemplo4.format(3, 4, 7))

ejemplo5 = "la {ciudad} siempre ha sido {calificativo} desde {fecha}"
print (ejemplo5.format(ciudad = "Paz", calificativo = "hermosa", fecha= "siempre"))

moneda = "boliviano"
pais = "Bolivia"
print (f"La moneda de {pais} es el {moneda}")  #con una "F" antes de la cadena es mas rapido
