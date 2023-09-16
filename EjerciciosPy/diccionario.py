# Diccionario.
import pickle, sys, os, random

soyundiccionario = {
    "nombre" : "Carlos",
    "apellido":"Fernandez",
    "edad" : 33,
    4:"piscis",
    "pais" : "Argentina"
}

ticket = soyundiccionario
guardar = str(random.randint(1000, 9999)) # número aleatorio de ticket entre 1000 y 9999.soyundiccionario
with open (guardar, "wb") as f:
    pickle.dump(ticket, f)

#abrir =
#with open (abrir, "rb") as f:
#    ticket2 = pickle.load(f)
#print(ticket2)     

print(soyundiccionario.items())
for i,x in soyundiccionario.items():
    print(i,x)

print(soyundiccionario.keys())
for i in soyundiccionario.keys():
    print(soyundiccionario[i])

print(type(soyundiccionario))
print(soyundiccionario)
suma = 250
print(f"El resultado de la suma es {suma}")

print(f"""

PERFIL

Nombre: {soyundiccionario["nombre"]}
Apellido: {soyundiccionario["apellido"]}
Edad: {soyundiccionario["edad"]}
Signo: {soyundiccionario[4]}

""")