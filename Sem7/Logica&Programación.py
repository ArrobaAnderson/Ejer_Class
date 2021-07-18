class Ejercicios:
    def __init__(self):
        pass
    
    def parImpar(self,numero):
        if numero%2 == 0:
            print("{} es Par".format(numero))
        else:
            print("{} es Impar".format(numero))

    def perfecto1(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+1
        if numero == acu:
                print("{} es perfecto".format(numero))
        else:
                print("{} no es perfecto".format(numero))


    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu=acu+1
        return acu

#Divisores
    def divisores(self,num):
        cont=1
        divisores=[]
        while cont< num:
            rec= num % cont
            if rec==0:
                divisores.append(cont)
            cont=cont+1
        print(divisores)
        
    
class Programacion(Ejercicios):
    def __init__(self):
        pass
    
    
    def divisores(self,num):
        divisores=[]
        for cont in range(1,num):
            rec= num % cont
            if rec==0:
                divisores.append(cont)
        return divisores
                
#ejer=Ejercicios()
# num=int(input("ingrese un numero: "))
# print("llamada 1")
# resp = ejer.perfecto2(num)
# if num == resp:
#     print("{} es perfecto".format(numero))
# else:
#     print("{} no es perfecto".format(numero))
      
                
# ejer = Ejercicios()
# num = int(input("Ingrese un numero: "))
# print("llamada 1")
# ejer.perfecto1(num)
# input()
# lista = [3,5,6,8,28]
# print("llamada 2")
# for num in lista:
#      ejer.perfecto1(num)
# input()
# print("llamada 3")
# ejer.perfecto1(23)


#Guardar datos en una lista
# ejer=Ejercicios()
# lista = [3,5,6,8,28]
# print("llamada 2")
# perfectos=[]
# for num in lista:
#     if ejer.perfecto2(num) == num:
#        perfectos.append (num)
# print(perfectos)


#prog1 = Programacion()
# num=28
# acumdivisor=prog1.perfecto2(num)
# if acumdivisor== num:
#     print(num,"es perfecto")
# else:
#     print(num,"no es perfecto")
# numeros=[3,6,24,28]
# perfectos=[]
# for numero in numeros:
#     if prog1.perfecto2(numero)== numero:
#         perfectos.append(numero)
# print(perfectos)


prog1 = Programacion()
div = prog1.divisores(6)
lista = [1,2]
lista2 = lista+div
print(lista2)