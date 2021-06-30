class Sintaxis:
    instancia=0
    
    def __init__(self,dato="LLamando al constructor1"):
        self.frase=dato
        Sintaxis.instancia = Sintaxis.instancia+1
        
    
    def usoVariables(self):
        edad, _peso = 18, 70.5
        nombres = "Anderson Arroba"
        dirDomiciliaria= "El Triunfo"
        Tipo_sexo = "M"
        civil= True
        
        usuario=() 
        usuario = ('Zancrow','186','zancrow1864@gmail.com')
        print(usuario[0],nombres[7])
        
ejer1 = Sintaxis()
ejer1.usoVariables()