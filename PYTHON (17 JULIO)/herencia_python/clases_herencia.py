class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
     
    def __str__(self):
        return f"Mi nombre es: {self._nombre} y tengo {self._edad} años"
    
## SI SE PUDE REVISAR, MEJOR
    #NOMBRE
    def set_nombre(self, nom):
        self._nombre = nom
        
    def get_nombre(self):
        return self._nombre
    
    #EDAD
    def set_edad(self, edad):
        self._edad = edad
    
    def get_edad(self):
        return self._edad
    
'''
p1 = Persona("Pedro Muñoz", 21)
p1._nombre= "Juan Valdez"
print(p1)
'''

class Atleta:
    def __init__(self, deporte):
        self.deporte = deporte

class Estudiante(Persona, Atleta):
    ##HERENCIA MÚLTIPLE CON ATLETA
    # def __init__(self, nombre, edad, grado, deporte):
    #     super(Persona, Atleta).__init__(nombre, edad, deporte) 
    #     self._grado = grado        
    #     self._deporte = deporte
        
    def __init__(self, nombre, edad, grado, deporte):
        Persona.__init__(self, nombre, edad)
        Atleta.__init__(self, deporte)
        self._grado = grado
        
    #GRADO
    def set_grado(self, grado):
        self._grado = grado
    
    def get_grado(self):
        return self._grado

    def __str__(self):
        return f"Mi nombre es {self._nombre}, tengo {self._edad} años, me gradué en {self._grado}, y practico {self.deporte}"    

        # año_grado = 2021
    
estud1 = Estudiante("Andrea Matínez", 22, 2021, "Futsal")
print(estud1)
# print(f"y me gradué en {estud1.año_grado}")








