#DATOS
import random
import numpy as np
nro_ticket = 1010
nombre = "Ricardo"
sector = "Seguridad"
asunto = "Cocina"
mensaje = "No funciona la cafetera"
opcion_1 = 0
opcion_2 = "S"

#MENU PRINCIPAL ALTA DE TICKET

while opcion_2 != "n":# Mientras opcion_2 sea distinto de "n"
   
 
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
            