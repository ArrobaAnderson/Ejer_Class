class Sintaxis:
    instancia=0
    
    def __init__(self,dato="LLamando al constructor"):
        self.frase=dato
        Sintaxis.instancia = Sintaxis.instancia+1
        
ejer1 = Sintaxis()
ejer2 = Sintaxis()
print(ejer1.frase)
