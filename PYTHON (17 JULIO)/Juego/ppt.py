import random


lista = ["piedra", "papel", "tijera"]
maquina = random.choice(lista)


otra_vez = True
while otra_vez == True:
    
    usuario = None
    while usuario not in lista:
        print("* -- Opción inválida -- *")
        usuario =  input("Ingrese piedra, papel o tijera: ").lower()
        
    print(f"Maquina: {maquina}")
    print(f"Usuario: {usuario}")

    if maquina == usuario:
        print()
        print("Empate, otra vez")
    elif (maquina == "piedra" and usuario == "papel") or (maquina == "tijera" and usuario == "piedra") or (maquina == "papel" and usuario == "tijera"):
        print()
        print("Ganaste")
    elif (maquina == "piedra" and usuario == "tijera") or (maquina == "papel" and usuario == "piedra") or (maquina == "tijera" and usuario == "papel"):
        print()
        print("Perdiste")
    else:
        print("* -- Opción inválida -- *")

if input("Otra vez? S/N").lower() != "s":
    otra_vez = False