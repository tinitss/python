nombre_completo = "Venancio Vargas"

nombre = nombre_completo[:8]
print(nombre)

apellido = nombre_completo[9:]
print(apellido)

nom2 = nombre_completo[::2]
print(nom2)

nom3 = nombre_completo[::-1]
print(nom3)

print()
print()

print("-- EJEMPLO SLICE --")
url = "http://www.google.com"
slice = slice(11, -4)
sitio = url[slice]
print(sitio)










