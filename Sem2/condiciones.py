class Condicion:
    
    def __init__(self,num1,num2):
        self.numero1= num1
        self.numero2= num2
        numero= self.numero1+self.numero2
        self.numero3= numero
        
    def usoIf(self):
        print(self.numero3)
        
print("instancia de la clase") 
cond1= Condicion(70,94)
cond1.usoIf()
print("Gracias por su visita")
