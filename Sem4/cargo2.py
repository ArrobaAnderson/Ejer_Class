class cargo:
    secuencia=0
    def __init__(self,des="Sin cargo"):
        cargo.secuencia=cargo.secuencia+1
        self.codigo=cargo.secuencia
        self.descripcion=des

if __name__ == "__main__":   
    cargo1 = cargo()
    print("Cargo1",cargo1.codigo,cargo1.descripcion)
    cargo2 = cargo("Docente")
    cargo2.codigo=1
    print("Cargo2",cargo2.codigo,cargo2.descripcion)
    cargo3 = cargo()
    print("Cargo3",cargo3.codigo,cargo3.descripcion)
