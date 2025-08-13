print ("Condicionales")

print ("if si se cumple una condicion, la condicion debe ser un booleano")

print ("inicio")
numero = 2    #int(input("Introduzca su numero: "))
if numero % 2 == 0:
    print ("el numero es par")
else:
    print ("Es impar")
print ("fin")

print ("tu numero es positivo, negativo o cero?")

# numero1 = int (input("Escribe tu número: "))
# if numero1 > 0:
#     print ("Es positivo")
# elif numero1 < 0:
#     print ("Tu numero es negativo")
# else:
#     print ("Tu número es cero")
# print ("fin")

# print ("Operador ternario")
# condicion = False
# resultado = "Es verdad" if condicion else "es falso"

#print (resultado)

numero1 = 3 # int (input("Coloca tu numero: "))
resultado = "Es par" if numero1 % 2 == 0 else "es impar"
# print (resultado)

# print ("Dividiendo")
# dividendo = 3 #int( input("Introduzca el número a dividir: "))
# divisor = 3 #int(input("El numero divisor: "))
# if divisor:
#     print (dividendo/divisor)
# else:
#     print("El numero es 0")

# temperatura = int(input("Introduzca la temperatura: "))
# if temperatura > 30:
#     print ("Enciente el ventilador")
# elif temperatura < 20:
#     print ("apagar ventilador")
# else:
#     print ("Temperatura perfecta")

# cesta = int(input("manzanas: "))
# if cesta:
#     print (cesta)
# else:
#     print ("comprando dos manzanas")

# animal = {"especie" : "perro", "nombre":"Firulais", "mamifero": False}

# if animal["mamifero"]:
#     print ("Es mamifero")
# else:
#     print("No es mamifero")

balones1 = {"futbol", "basquetball", "volleyball"} 
balones2 = {"americano", "tenis", "pingpong"}

balones = balones1.intersection(balones2)

if balones:
    print(balones)
else:
    print("No hay nada en comun")



    


