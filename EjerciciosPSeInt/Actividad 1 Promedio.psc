Algoritmo Promedio
	//	1- El profesor comienza ingresando la primera nota del alumno.
	//	2- Luego,ingresa la segunda nota del alumno.
    //	3- Se calcula el promedio de las dos notas ingresadas.
    //	4- Se realiza una verificación para determinar si el promedio es mayor o igual a 70. Si es así, se muestra el mensaje "Promociona".
    //	5- Si el promedio es menor a 70, se realiza otra verificación para determinar si el promedio es mayor o igual a 40. Si es así, se muestra el mensaje "Aprueba".
    //	6- Si el promedio es menor a 40, se muestra el mensaje "Desaprueba".
	
	// Asignación de variables  
	Definir nota1, nota2 Como Entero
	Definir sum, prom Como Real
	
	// Ingresa las 2 notas por teclado
	
	Escribir 'Ingrese la primer Nota del Alumno: '
	Leer nota1
	Escribir 'Ingrese la segunda Nota del Alumno: '
	Leer nota2
	
	// Calculo el promedio
	prom = (nota1+nota2)/2
	
	Si (prom >= 70) Entonces
		Escribir 'El Promedio es de: '
		Escribir prom
		Escribir 'Promociona'
	SiNo
		Si (prom >= 40) Entonces
			Escribir 'El Promedio es de: '
			Escribir prom
			Escribir 'Aprueba'
		SiNo
		Escribir 'El Promedio es de: '
		Escribir prom
		Escribir 'Desaprueba'
	    FinSi
    FinSi
	
FinAlgoritmo
