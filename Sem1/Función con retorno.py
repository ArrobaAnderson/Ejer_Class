#Funciones en Python - DEF

'''Función con retorno'''
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ/len(notas)
