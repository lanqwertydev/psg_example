comidas = {"carne" : {"animales":["leon", "tigre"]}, "frutas" : {"animales": ["panda", "mono"] }}
print (comidas)

comidas.update({"croquetas":{"animales":["perros", "gatos"]}})

print (comidas)

print ( "carne" in comidas)

comidas.pop("frutas")
print (comidas)


