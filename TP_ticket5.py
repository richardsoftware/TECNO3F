#Sistema de Tickets
import pickle, sys, os, random

#funcion MENU
def seleccionar_opcion_menu():
    print()
    print("          Hola. Bienvenido al Sistema de Ticket")
    print()
    print("          1 - Generar un nuevo Ticket")
    print("          2 - Consultar un Ticket")
    print("          3 - Salir")
    print()
    opcion_menu = int(input("          Ingrese su opcion: "))

    return opcion_menu

#Funcion Ingresar Ticket
def ingresar_ticket():
    opcion_2 = "S"
    while opcion_2.upper()!="N": # Mientras opcion_2 sea distinto de "n" o "N"

        print()
        print("Ingrese los datos para generar un nuevo Ticket")
        print()
        soyundiccionario["nombre"] = input("Ingrese su nombre: ")
        soyundiccionario["sector"] = input("Ingrese su sector: ")
        soyundiccionario["asunto"] = input("Ingrese su asunto: ")
        soyundiccionario["mensaje"] = input("Ingrese su mensaje: ")
        soyundiccionario["ticket"] = str(random.randint(1000, 9999)) # número aleatorio de ticket entre 1000 y 9999.soyundiccionario

        #guardar datos en archivo y mostrar en pantalla
        ticket = soyundiccionario
        guardar = soyundiccionario["ticket"]# número aleatorio de ticket entre 1000 y 9999.
        with open (guardar, "wb") as f:#guardar es el nombre del archivo(numero del ticket) WB Write-Binary
            pickle.dump(ticket, f) #

        print(f"""

        =================================================
                 Se genero el siguiente Ticket
        =================================================
                 
        Su nombre: {soyundiccionario["nombre"]}        Nro. de Ticket: {soyundiccionario["ticket"]}
        Sector: {soyundiccionario["sector"]}
        Asunto: {soyundiccionario["asunto"]}
        Mensaje: {soyundiccionario["mensaje"]}
        Ticket: {guardar}

                      Recordar el número de ticket

        """)
        opcion_2 = input("Desea generar un nuevo ticket (S/N): ")

    return print(opcion_2)


#Funcion Consultar Ticket Funciona bien
def consultar_ticket():

    opcion_3 = "S"
    while opcion_3.upper()!="N": # Mientras opcion_3 sea distinto de "n" o "N"

        print("=============================")
        print("    Consulta de ticket")
        print("=============================") 

        #leer el archivo
        abrir = input("Ingrese numero de Ticket: ")#abro el archivo nombre (numero de ticket)
        with open (abrir, "rb") as f: #abro el archivo
            ticket2 = pickle.load(f)

        print(f"""

        =================================================================
                           Datos de su Ticket
        =================================================================
                 
        Su nombre: {ticket2["nombre"]}        Nro. de Ticket: {abrir}
        Sector: {ticket2["sector"]}
        Asunto: {ticket2["asunto"]}
        Mensaje: {ticket2["mensaje"]}
        Ticket: {ticket2["ticket"]}

        """)

        opcion_3 = input("Desea consultar otro ticket (S/N): ")
       
    return print(opcion_3)


#Comienza el Programa asigno valores

opcion_1 = 0
opcion_2 = "S"
opcion_3 = "S"
#Defino el Diccionario Datos Ticket
soyundiccionario = {
    "nombre" : "Juan Perez",
    "sector":"Tecnologia",
    "asunto" : "PC",
    "mensaje" : "No funciona",
    "ticket" : "1000"
}

#MENU PRINCIPAL ALTA Y CONSULTA DE TICKET
# Repeticion

while opcion_1 != 3:# Mientras opcion_1 sea distinto de 3
    
    opcion_1 =seleccionar_opcion_menu()

    if opcion_1 == 1:
 #       while opcion_2 != 2 :# Mientras opcion_2 sea distinto de N
         ingresar_ticket()

    elif opcion_1 == 2:
#        while opcion_3 != 2:# Mientras opcion_3 sea distinto de N
         consultar_ticket()
     
    elif opcion_1 == 3:
        print("Salida")
                  
    else:
        print("Error en su seleccion")
