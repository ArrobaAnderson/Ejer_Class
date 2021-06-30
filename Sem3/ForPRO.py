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
     
        listaNotas = [(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum,cont=0,0
        for notas in listaNotas:
            print(notas)
            acumparcial=0
            for nota in notas:
                acumparcial +=nota
            cont=cont+len(notas)
            acum=acum+acumparcial
            print("Pracial:{} PromParcial:{}".format(acumparcial,acumparcial/len(notas)))
        print("TotalGeneral:{} PromGeneral:{}".format(acum,acum/cont))
bucle = For() 
bucle.usoFor()
