class For:
    def __init__(self):
        pass
    
    def usoFor(self):
        nombre = "Jose"
        datos = ["Jose", 50, True]
        numeros = (2,5,6,4,1)
        docente = {'nombre':'Jose','Edad':50,'fac':'faci'}
        listaNotas = [(30,40),(20,40),(50,40)] 
        listaAlumnos = [{"nombre":"Lucas","final":70},{"nombre":"Gissela","final":60},{"nombre":"Alex","final":90}]
        for elem in datos:
            print(elem,end=" ")
        print()
        for elem in nombre:
            print(elem,end=" ")

bucle = For()
bucle.usoFor()
