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
            
        for pos,valor in enumerate(datos):
            print(pos,valor)
       
        for clave,valor in docente.items():
            print(clave,valor,end=" ")
        
        for notas in listaNotas:
            for nota in notas:
                print(nota,end=" ")
            print("Saliendo el for interno")
            
bucle = For()
bucle.usoFor()