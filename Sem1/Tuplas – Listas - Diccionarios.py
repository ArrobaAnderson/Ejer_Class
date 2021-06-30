#Colecciones: LISTAS – TUPLAS - DICCIONARIOS

# Tuplas – Listas - Diccionarios
usuario = ('dchiki', '1234', 'chiki@gmail.com')
materias = ['Python', 'PHP', 'POO', 'Go']
docente = {'nombre':'Daniel','edad':50,'fac':'faci'}
print(usuario[0], materias[1], docente['nombre'])
print(usuario[0:2], docente.keys(), docente.values())
materias.append('Programacion Movil')
docente['sexo'], docente['edad']='M', 51
print(materias,docente)
tupla,lista,diccionario=(), [], {}
