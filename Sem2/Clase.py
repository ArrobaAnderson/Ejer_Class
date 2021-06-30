class Sintaxis:
    instancia=0
    
    def _init_(self,dato=""):
        self.frase=dato
        Sintaxis.instancia = Sintaxis.instancia+1
        
ejer1 = Sintaxis()
ejer2 = Sintaxis()
        