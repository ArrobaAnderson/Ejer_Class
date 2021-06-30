#Funciones en Python - DEF

'''Funciones sin retorno'''
def vocales(frase):
    for car in frase:
        if car in('a', 'e', 'i', 'o', 'u'):
            print(car)
