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
     
        print("\nDiccionario de alumnos")
        print(listaAlumnos)
        acum=0
        
        for alumnos in listaAlumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor,type,end=" ")
                if clave == 'final':
                    acum=acum+valor
            print()
        print("Promedio", acum/len(listaAlumnos))

bucle = For()
bucle.usoFor()