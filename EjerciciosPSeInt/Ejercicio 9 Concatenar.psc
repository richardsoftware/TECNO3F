Algoritmo Concatenar_palabras
	
	// Declaro las variables y los tipos de datos
	Definir palabra1, palabra2 Como Caracter
	Definir size1, size2 Como Entero
	
	// Ingresar las palabras
	Escribir "Ingrese la primer palabra: "
	Leer palabra1
	
	Escribir "Ingrese la segunda palabra: "
	Leer palabra2
	
	size1=longitud(palabra1)
	size2=longitud(palabra2)
	
	// Determinar cual es mas larga
	
	Si(size1 < size2)Entonces
		Escribir "La segunda palabra es mas larga, Concatenacion invertida"
		Escribir palabra2, palabra1;
	Sino
		Escribir "La primera palabra es mas larga, Concatenacion Simple"
		Escribir palabra1, palabra2;
	Finsi
	
FinAlgoritmo