Algoritmo Mayor_deTres
	// Declaro las variables y los tipos de datos
	Definir numero1,numero2,numero3 Como Entero
	
	// Ingresar los tres numeros
	Escribir "Ingrese el primer n�mero: "
	Leer numero1
	
	Escribir "Ingrese el segundo n�mero: "
	Leer numero2
	
	Escribir "Ingrese el tercer n�mero: "
	Leer numero3
	
	Escribir 'Los numeros ingresados son: ',numero1,' ',numero2,' y ',numero3;
	
	// Determinar el mayor de los tres numeros
	Si(numero1 > numero2 y numero1 > numero3)Entonces
		Escribir "El primer n�mero es Mayor"
	Sino
		Si (numero2 > numero1 y numero2 > numero3)Entonces
			Escribir "El segundo n�mero es Mayor"
		Sino
			Si (numero3 > numero1 y numero3 > numero2)Entonces
				Escribir "El tercer n�mero es Mayor"
			Sino Escribir"Los numeros son iguales"
			Finsi
		Finsi
	Finsi
	
FinAlgoritmo
