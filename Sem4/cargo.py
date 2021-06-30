class Cargo:
    def __init__(self):
        self.codigo=99
        self.descripcion="Sin cargo"
        
Cargo1 = Cargo()
print("Cargo1",Cargo1.codigo,Cargo1.descripcion)
Cargo2 = Cargo()
Cargo2.codigo=1
Cargo2.descrpcion="Docente"
print("Cargo2",Cargo2.codigo,Cargo2.descripcion)
Cargo3 = Cargo()
Cargo3.descripcion="Conserje"
print("Cargo3",Cargo3.codigo,Cargo3.descripcion)