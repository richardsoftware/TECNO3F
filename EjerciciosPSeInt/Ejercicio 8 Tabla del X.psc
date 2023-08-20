Algoritmo Tabla_X
	Definir i, resultado, multiplicador Como Entero
	
	// -- Tabla del X
	Escribir "Tablas de Multiplicar"
	Escribir "Ingrese número: "
	Leer multiplicador
	Escribir "Tabla de multiplicar del ", multiplicador;
		
	Para i<-1 Hasta 10 Hacer
		
		resultado=i*multiplicador
		
		Escribir multiplicador,'X',i," = " , resultado;
		
	FinPara
	
FinAlgoritmo
