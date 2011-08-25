'''
Created on 25/08/2011

@author: santiago
'''
class Persona:
    def __init__(self,nombre,edad,ciudad):
        self.nombre = nombre
        self.edad = edad,
        self.ciudad = ciudad

class BinaryFileVariableLengthManager:
    registry_separator = '\n'
    field_separator = ';'
    def __init__(self,filename):
        self.f = open(filename,'ab')
    
    def writePersona(self,persona):
        str = "%s%s%s%s%s%s" % (persona.nombre,self.field_separator,persona.edad,self.field_separator,persona.ciudad,self.registry_separator)
        self.f.write(str)


file_name = "gdd_ej1_tp1.data"
m = BinaryFileVariableLengthManager(file_name)
m.writePersona(Persona("Juan",20,"La Plata"))
"""
tmp_folder = "/tmp/"
try:
    f = open(file_name,'ab')
    f.write("Chau\n")
except IOError:
    print("Ocurrio un error")
"""