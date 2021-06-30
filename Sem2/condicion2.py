class Condicion:
    
    def __init__(self,num1=6,num2=8):
        self.numero1= num1
        self.numero2= num2
        numero= self.numero1+self.numero2
        self.numero3= numero
        
    def usoIf(self):
        print(self.numero3)
        
print("instancia de la clase") 
cond1= Condicion(70,94)
cond2= Condicion()
print(cond2.numero3)
cond1.usoIf()
cond2.usoIf()
print("Gracias por su visita")
