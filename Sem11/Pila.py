class Pila:
    def __init__(self):
        self.lista = []
        self.size = 5
        self.top = 0
    
    def push(self,dato):
        if self.top < self.size:
            self.lista += [dato]
            self.top += 1
        else:
            print("La lista sea llenado")
    
    def pop(self):
        if self.empty():
            return None
        else:
            top = self.lista[-1]
            self.lista = self.lista[:-1]
            self.top -= 1
            return top
        
    def longitud(self):
        return self.top
        
    def show(self):
        for top in range(self.top,-1,-1,-1):
            print("[{}]",format(self.lista[top]))            
    
    def empty(self):
        if self.top == 0:
            return True
        else:
            return False
    
pila1 = Pila()
pila1.push(4)
pila1.push(8)
pila1.push(6)
pila1.push(1)
# dato = pila1.pop()
# if dato: print("El dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")
# dato = pila1.pop()
# if dato: print("El dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")
# dato = pila1.pop()
# if dato: print("El dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")
# dato = pila1.pop()
# if dato: print("El dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")

pila1.show()
print(pila1.longitud())