#TP FINAL TICKETS
import random
#Funcion MENU PRINCIPAL
def seleccionar_opcion_menu():
    print("Hola. Bienvenido al Sistema de Ticket")
    print("1 - Generar un nuevo Ticket")
    print("2 - Consultar un Ticket")
    print("3 - Salir")
    opcion_menu = int(input("Ingrese su opcion: "))

    return opcion_menu

#Funcion Ingresar Ticket
def ingresar_ticket():
    opcion_2 = "S"

    while opcion_2 != "n":# Mientras opcion_2 sea distinto de "n"
   
 
        print("Ingrese los datos para Generar un nuevo Ticket")

        nro_ticket = random.randint(1000, 9999) # número aleatorio de ticket entre 1000 y 9999.
        nombre = input("Ingrese su Nombre: ")
        sector = input("Ingrese su Sector: ")
        asunto = input("Ingrese Asunto: ")
        mensaje = input("Ingrese su Mensaje: ")

        print("=============================")
        print("Se genero el siguiente ticket")
        print("=============================")
                 
        print(f"Su nombre: {nombre}        Nro. de Ticket: {nro_ticket}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print("            Recordar el número de ticket")

        opcion_2 = input("Desea generar un nuevo ticket (S/N): ")
    return print(opcion_2)

#Funcion Consultar Ticket
def consultar_ticket():

    opcion_3 = "S"

    while opcion_3 != "n":# Mientras opcion_3 sea distinto de "n"

       print("=============================")
       print("    Consulta de ticket")
       print("=============================") 
   
       nro_ticket = int(input("ingrese numero de ticket: "))
                
       print(f"Su nombre: {nombre}        Nro. de Ticket: {nro_ticket}")
       print(f"Sector: {sector}")
       print(f"Asunto: {asunto}")
       print(f"Mensaje: {mensaje}")

       opcion_3 = input("Desea consultar otro ticket (S/N): ")

    return print(opcion_3)


#Comienza el Programa asigno valores
nro_ticket = 1010
nombre = "Ricardo"
sector = "Seguridad"
asunto = "Cocina"
mensaje = "No funciona la cafetera"
opcion_1 = 0
opcion_2 = "S"
opcion_3 = "S"

#MENU PRINCIPAL ALTA Y CONSULTA DE TICKET

while opcion_1 != 3:# Mientras opcion_1 sea distinto de 3

    opcion_1 =seleccionar_opcion_menu()

    if opcion_1 == 1:       
         ingresar_ticket()

    elif opcion_1 == 2:

         consultar_ticket()
    
    elif opcion_1 == 3: #sale del menu principal
        print("Salida")
                  
    else:
        print("Error en su seleccion")
