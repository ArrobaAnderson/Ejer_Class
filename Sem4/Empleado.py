from cargo2 import cargo

class Empleado:
    secuencia=0
    def __init__(self,nom="",sue=0,car=None):
        self.codigo=self.generarCodigo()
        self.nombre=nom 
        self.sueldo=sue 
        self.cargoEmp=car
        
    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia
    
    def mostrar(self):
        print("Codigo:{} Nombre:{} Cargo({}):{}".format(self.codigo,self.nombre,self.cargoEmp.codigo,self.cargoEmp.descripcion))
        
        
cargo1 = cargo("Docente")
emp1 = Empleado("Leonardo",1864,cargo1)
emp1.mostrar()
