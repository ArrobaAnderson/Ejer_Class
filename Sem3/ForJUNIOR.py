class For:
    def __init__(self):
        pass
    
    def usoFor(self):
        listaNotas = [(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum=0
        cont=0
        for notas in listaNotas:
            print(notas)
            acumparcial=0
            contparcial=0
            for nota in notas:
                acumparcial +=nota
                contparcial +=1
                acum=acum+nota
                cont=cont+1
            print(acumparcial/len(notas))
        print(acum/cont)
bucle = For()
bucle.usoFor()
        