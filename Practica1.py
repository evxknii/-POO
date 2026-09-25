"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado

def area_rectangulo(base, altura):
    return base * altura
print(area_rectangulo(5,3))


#Implementar el paradigma Orientado a Objetos (OO)
class Rectangulo:
    def __init__(self, base, altura):
        self.base= base
        self.altura=altura 

    def area(self):
        return self.base * self.altura


rect= Rectangulo(5,3)
print(rect.area())
    
#los atributos si pueden ir dentro de una clase, los atributos dde la clase tienen que ir del metodo contructor, los metodos se invocan a partir del objeto



class Rectangulos:
    def area(self, base, altura): #metodos normales llevan self
        areaR= base * altura
        return areaR

rectangulo1=Rectangulos() # esto es para crear o instanciar un objeto "rectangulo1" de la clase "rectangulos" 
print(f"El area del rectangulo es: {rectangulo1.area(5,6)}")

#atributos: variables, van a estar inicializados, inicianilizacion a=3, a= true,etc. por que el primer valor que agarra una variable,
#void: cuando el metodo no regresa nada, se llama diagramas uml por que son lenguaje unificado.
#cuando no lleva nada de parametro es cuando hay un metodo constructor, metodos: publico o protegidos se puede usar. (hacer dos objetos por la misma clase)
#metodo constructor= valor inicial cuando es hecho, self: que un atributo es de la clase, y se le asigna el parametro que se recibe.
#publico: cuando no lleva ningun guion bajo, si lleva un guion bajo es protegido, dos guion bajo: privado, no se hereda.
#diagrama signo de gato cuando lleva un guion, examen del proximo lunes: en hoja de papel. para que la clase funcione debe de tener un metodo y un atributo