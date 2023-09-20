#TP TA TE TI
# Funcion Dibujar Tablero
def dibujar_matriz():
    print("   ___ ___ ___        ___ ___ ___")
    print("  | 1 | 2 | 3 |      | %c | %c | %c |" % (matriz[0][0],matriz[0][1],matriz[0][2]))    
    print("  |___|___|___|      |___|___|___|")    
    print("  | 4 | 5 | 6 |      | %c | %c | %c | " % (matriz[1][0],matriz[1][1],matriz[1][2]))    
    print("  |___|___|___|      |___|___|___|")  
    print("  | 7 | 8 | 9 |      | %c | %c | %c | " % (matriz[2][0],matriz[2][1],matriz[2][2]))
    print("  |___|___|___|      |___|___|___|")
    print("")

# Funcion  Validar el estado de la jugada
def validar(trn):
    global resultado
    # Horizontal y Vertical
    for i in range(0,3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != " " or matriz[0][i] == matriz[1][i] == matriz[2][i] != " ":
            resultado = "Gana " + trn
            return True
    # Diagonal
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != " " or matriz[0][2] == matriz[1][1] == matriz[2][0] != " ":
        resultado = "Gana " + trn
        return True
    # Todo lleno
    if " " not in matriz[0] and " " not in matriz[1] and " " not in matriz[2]:
        resultado = "Empate"
        return True
    # Por Default
    return False

# Funcion Nuevo Juego
def jugar_nuevo():

    for i in range(0,3):
        matriz[i][0] = " " 
        matriz[i][1] = " " 
        matriz[i][2] = " "
        
# Programa
respuesta = "S"
jugada = 0
juego = False
X = 0
Y = 0
resultado = ""
matriz = [["","",""],["","",""],["","",""]]

print("=====================================")
print("        JUGAR  TA-TE-TI              ")
print("=====================================")

while respuesta.upper() != "N":
    try:
        Turno = "X"
        jugar_nuevo()
        juego = False
        # Jugadas hasta Ganador o Empate
        if respuesta.upper() == "S":
            while juego == False:
                dibujar_matriz()
                print("Juega ",Turno," ",end = "")
                # exception del valor cuando es ENTER ''
                try:
                    jugada=int(input("donde juega?(1-9): "))
                except ValueError:
                    print("No es un numero. Seleccione una opcion correcta!")
                except KeyboardInterrupt:
                    print("No es un numero. Seleccione una opcion correcta!")
                else:
                    if jugada <= 9 and jugada >= 1:
                        jugada = jugada - 1
                        Y = jugada / 3
                        X = jugada % 3
                    X = int(X)
                    Y = int(Y)
                    if matriz[Y][X] == " ":
                        matriz[Y][X] = Turno
                        juego = validar(Turno)
                        if Turno == "X":
                            Turno = "O"
                        else:
                            Turno = "X"
                    else:
                        print("Casilla ocupada, Intente otra jugada!")
                    # Cambio de turno
        if resultado != "" :
            print("*************************************")
            print("           Fin de la Jugada!!!!!!!!!!")
            print("*************************************")
            print(resultado)
            print("*************************************")
            dibujar_matriz()
        respuesta = input("Jugar Otra vez? (S/N): ")
        resultado = ""
    except KeyboardInterrupt:
        print ("Selecione una opcion correcta!")
        respuesta = ""
        resultado = ""
print("GAME OVER. Gracias por Jugar!!!")
