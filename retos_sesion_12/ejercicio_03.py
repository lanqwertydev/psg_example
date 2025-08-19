amigos = {"Alice", "Bob", "Charlie", "David", "Eve"}
amigos_Jess = {"Alice", "Bob", "Frank", "Grace"}
comunes = amigos.intersection(amigos_Jess)
if comunes:
    print(comunes)
else:
    print("No hay amigos comunes")
