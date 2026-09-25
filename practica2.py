"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches

class Coches:
    #todos van a tener color azul y asi, esto es cuando esten todos iguales, no todos van a ser color azul, para que sea dinamico tienen que estar dentro de un metodo constructor
    #marca= "VMW"
    #color="azul" pero sise pueden poner asi tambien
    def __init__(self, color, marca, velocidad):
        #color= color
        #marca= marca
        #velocidad=velocidad #no sabe si hace referencia a los atributos entonces se utiliza asi:
        #this: tambien se puede usar
        self.__color= color
        self.__marca= marca
        self.__velocidad=velocidad  #representacion temporal, entonces esto no coincide, se dejo publico y queremos que sea privado
        #guion bajo= antes del atributo para hacerlo privado

        def acelerar(self):
            #pass para que no haga nada (regrese nada)

            self.__velocidad+=1

        def frenar(self):
            #pass
            self.__velocidad-=1

        def tocar_claxon(self):
            #pass
            return "pi pi pi pi"
            

        #si fuera protegido = def _acelerar  o __acelerar
        #no se pueden utilizar los atributos por que son privados

        

coche1=Coches("Blanco", "VMW", 220)
coche2=Coches("Azul", "Nissan", 180)


#print(f"el color del coche 1 es:{coche1.__color}")error cuando algo pase con los encapsulados, cuando sea privado {coche.__color}= privado, se tiene que utilizar adentro de la clase, no afuera

print(f"el claxon del coche uno, hace: ") 
coche1.tocar_claxon()

print(f"el claxon del coche dos, hace: ") 
coche2.tocar_claxon()


#metodos get y metodos 
#se ejecuta el metodo, imprime y luego da un salto de linea, y como ya lo ejecuto te pone None


#modelar:representar (pensar)
#diagramacion: lo que representa, todos los metodos con paretensesis
#pass= metodo que no hace nada, 
# -: encapsulamiento




#Instanciar o crear objetos de la clase Coches






