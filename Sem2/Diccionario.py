class Sintaxis:
    instancia=0
    
    def __init__(self,dato="LLamando al constructor1"):
        self.frase=dato
        Sintaxis.instancia = Sintaxis.instancia+1
        
    def usoVariables(self):
        edad, _peso = 21, 70.5
        nombres = "Leonardo Arroba"
        dirDomiciliaria= "El Triunfo"
        Tipo_sexo = "M"
        civil=True
        
        usuario=() 
        usuario = ('Zancrow','186','zancrow1864@gmail.com')
        materias=[]
        materias = ['Programacion Web','PHP','POO']
        
        estudiante={}
        estudiante = {"nombre":"Anderson","edad":21,}
        edad= estudiante["edad"]
        estudiante["edad"]= 18
        print(usuario,usuario[0],usuario[0:2],usuario[-1])
        print(nombres,nombres[0],nombres[0:2],nombres[-1])
        print(materias,materias[2:],materias[:3],materias[::-1],materias[-2:]) 
        
ejer1 = Sintaxis()
ejer1.usoVariables()
