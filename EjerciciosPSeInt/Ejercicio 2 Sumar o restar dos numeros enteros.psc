Algoritmo Suma_resta
	// Declaro las variables y los tipos de datos
	Definir numero1,numero2, resultado Como Entero
	
	// Ingresar los dos numeros enteros
	Escribir "Ingrese el primer número: "
	Leer numero1
	
	Escribir "Ingrese el segundo un número: "
	Leer numero2
	
	// Determinar si es suma o resta y mostrar el resultado en pantalla
	Si(numero1 < numero2)Entonces
		resultado <- numero1+numero2
		Escribir 'La suma de ',numero1,' + ',numero2,' es igual a: ',resultado; 
	SiNo
		resultado <- numero1-numero2
		Escribir 'La resta de ',numero1,' - ',numero2,' es igual a: ',resultado;
	FinSi
	
FinAlgoritmo