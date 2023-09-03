#DATOS
nro_ticket = 1010
nombre = "Ricardo"
sector = "Seguridad"
asunto = "Cocina"
mensaje = "No funciona la cafetera"
opcion_1 = 2
opcion_3 = "S"

lista = ['Ricardo','Carlos','Pedro','Ana','Santiago']

#MENU PRINCIPAL ALTA Y CONSULTA DE TICKET
# Repeticion

while opcion_3 != "n":# Mientras opcion_3 sea distinto de n 
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
            