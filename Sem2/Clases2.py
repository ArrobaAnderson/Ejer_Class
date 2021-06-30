class Sintaxis:
    instancia=0
    
    def __init__(self,dato="LLamando al constructor1"):
        self.frase=dato
        Sintaxis.instancia = Sintaxis.instancia+1

print("Sintaxis antes de instancia es: {}".format(Sintaxis.instancia))
ejer1 = Sintaxis()
print("Sintaxis de ejer1 es: {}".format(Sintaxis.instancia))
ejer2 = Sintaxis("instancia2")
print(ejer1.frase)
print("Sintaxis de ejer2 es: {}".format(Sintaxis.instancia))
print("Sintaxis nuevamente de ejer1 es: {}".format(Sintaxis.instancia))
print(ejer2.frase)
