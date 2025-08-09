Mochilero1 = {"Paris", "Londres", "Nueva York", "Tokio", "Peru", "Chile", "Colombia", "Bolivia"}

Mochilero2 = {"Londres", "Roma", "Nueva York", "Sidney", "Argentina", "Brasil", "Panama", "Bolivia"}

conjunto = Mochilero1.symmetric_difference(Mochilero2)

print (conjunto)

ciudades_compartidas = Mochilero1 & Mochilero2

print (ciudades_compartidas)
