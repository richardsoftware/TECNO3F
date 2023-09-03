1#DATOS
import random

nro_ticket = 1010
nombre = "Ricardo"
sector = "Seguridad"
asunto = "Cocina"
mensaje = "No funciona la cafetera"
opcion_1 = 0
opcion_2 = "S"
opcion_3 = "S"

#MENU PRINCIPAL ALTA Y CONSULTA DE TICKET
# Repeticion

while opcion_1 != 3:# Mientras opcion_1 sea distinto de 3
    print("Hola. Bienvenido al Sistema de Ticket")
    print("1 - Generar un nuevo Ticket")
    print("2 - Leer un Ticket")
    print("3 - Salir")
    opcion_1 = int(input("ingrese su opcion: "))

    if opcion_1 == 1:
 #       while opcion_2 != 2 :# Mientras opcion_2 sea distinto de N
            print("Ingrese los datos para Generar un nuevo Ticket")

            nro_ticket = random.randint(1000, 9999) # número aleatorio de ticket entre 1000 y 9999.
            nombre = input("ingrese su Nombre: ")
            sector = input("ingrese su Sector: ")
            asunto = input("ingrese Asunto: ")
            mensaje = input("ingrese su Mensaje: ")

            print("=============================")
            print("Se genero el siguiente ticket")
            print("=============================")
                 
            print(f"Su nombre: {nombre}        Nro. de Ticket: {nro_ticket}")
            print(f"Sector: {sector}")
            print(f"Asunto: {asunto}")
            print(f"Mensaje: {mensaje}")
            print("            Recordar el número de ticket")

            opcion_2 = input("Desea generar un nuevo ticket (S/N): ")
            print(opcion_2)


    elif opcion_1 == 2:
#        while opcion_3 != 2:# Mientras opcion_3 sea distinto de N
            print("=============================")
            print("    Consulta de ticket")
            print("=============================") 
   
            nro_ticket = int(input("ingrese numero de ticket: "))
                
            print(f"Su nombre: {nombre}        Nro. de Ticket: {nro_ticket}")
            print(f"Sector: {sector}")
            print(f"Asunto: {asunto}")
            print(f"Mensaje: {mensaje}")

            opcion_3 = input("Desea consultar otro ticket (S/N): ")
            print(opcion_3)

    elif opcion_1 == 3:
        print("Salida")
                  
    else:
        print("Error en su seleccion")
