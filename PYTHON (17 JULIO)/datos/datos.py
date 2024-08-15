"""""
print ("Hola mundo")
nombre = input("Su nombre:")
edad = input("Su edad:")
#f-String
print(f"Hola {nombre} su edad es: {edad}")


print()
print("EJERCICIO CON DICTOINARY")
mi_dict = {
    "marca": "Audi",
    "ref": "R8",
    "modelo": 2021
}

#print (mi_dict)
##print()

for key in mi_dict:
    print(key)
print()
    
for key in mi_dict:
    print(mi_dict[key])
print()

for key, value in mi_dict.items():
     print(key, value)
print()
"""

print()
print("EJERCICIO CON SET")
mi_set = {
    "zapatos", "chanclas", "botas", "botas"
}
for c in mi_set:
    print(c)
    
