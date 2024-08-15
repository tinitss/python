from carro import Carro

carro1 = Carro("Audi", 2021)
print(f"Mi carro es marca {carro1.marca}")
print(f"Mi carro es modelo {carro1.moddelo}")
print(f"Velocidad inicial {carro1.velocidad}")
carro1.acelerar(30)
carro1.acelerar(50)
carro1.frenar()
