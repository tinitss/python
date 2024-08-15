class Carro:
    velocidad  = 0 #Atributo de clase
    
    #Constructor
    def __init__(self, marca, modelo): #Atributos de instancia
        self.marca = marca
        self.moddelo = modelo     
    
    def acelerar(self, kph):
        self.velocidad += kph
        print(f"Aceleró. Velocidad: {self.velocidad}")
        
    def frenar(self):
        self.velocidad = 0
        print(f"Frenó. Velocidad: {self.velocidad}")
    
    
    
    



    
    
    
    
    