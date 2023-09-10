#ARRAY Listas, Tuplas, Diccionarios

Lista = ["Andres","Carlos","Eugenio"]
print(Lista)
print(type(Lista))
print(Lista[1])

Tupla_dias = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print(Tupla_dias)
print(type(Tupla_dias))
print(Tupla_dias[4])

Primer_diccionario = dict()
print(Primer_diccionario)
print(type(Primer_diccionario))

#prueba

lis = ['Buenos Aires','Brasilia','Asunción','Montevideo','Santiago','Lima','Caracas','Bogotá']
print(lis)

dicc = {  'Ciudad': lis, 
'País': ['Brasil','Ecuador','Uruguay','Chile','Perú','Venezuela','Colombia','Méjico','Uruguay','España'], 
'Continente' : ['América','América','América','América','América','América','América','América','América','Europa']}

print(dicc)

print(dicc.keys())
print(dicc['Ciudad'])