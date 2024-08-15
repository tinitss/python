#IF - ELIF - ELSE
'''
edad = int (input("Digite su edad:"))
if edad == 100:
    print("Usted tiene 100 años") 
elif edad >= 18:
    print("Usted es mayorcit@ de edad")
else:
    print("Usted en menorcill@")  


#Ciclos
for i in range(4):
    print(i) 


x = 8
while x < 14:
    print(x)
    x += 1
'''

#Ciclos anidados
filas = int (input("Número de filas: "))
cols = int (input("Número de columnas: "))
s = input ("Símbolo: ")

    

for a in range (filas):
    for b in range (cols):
        print(s, end=" ")
    print()
    
    
