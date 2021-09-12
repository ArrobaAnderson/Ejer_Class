class Matriz:
    def __init__(self,matriz):
        self.matriz = matriz
        
    def ingresar(self,dato):
        pass
    
    def presentar(self):
        for fila in range(len(numeros)):
            columna = numeros[fila]
            for col in range(len(columna)):
                print(columna[fila][col],end=" ")
            print()

numeros = [[50,37,95],[23,85,70],[26,71,69]]
mat = Matriz(numeros)
mat.presentar()