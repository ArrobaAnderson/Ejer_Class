class Sintaxis:
    instancia=0 #Atributos de clase
    #_init_ Metodoconstructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
    # e inicializar los atributos de la clase. Self es un objeto que representa la clase creada
    def __init__(self,dato="Llamando al constructor 2"):
        self.frase =dato #Atributo de instancia
        Sintaxis.instancia = Sintaxis.instancia+1
print("Sintaxis antes de instancia es: {}".format(Sintaxis.instancia))  
      
ejer1 = Sintaxis() #Instancia la clase sintaxis y crea el objeto ejer1 (copia de la clase)
print("Sintaxis de ejer1 es: {}".format(Sintaxis.instancia))

ejer2 = Sintaxis("instamcia 2")

print(ejer1.frase)
print("Sintaxis de ejer2 es: {}".format(Sintaxis.instancia))
print("Sintaxis nuevamente de ejer1 es: {}".format(Sintaxis.instancia))
print(ejer2.frase)
